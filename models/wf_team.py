# -*- coding: utf-8 -*-
from datetime import datetime
from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError, except_orm, UserError
import calendar
import math
import re
import requests
import pytz


class WorkfolioTeam(models.Model):
    _name = 'wf.team'
    _description = "Workfolio Team"
    _inherit = ['mail.thread']

    name = fields.Char(string="Name", required=True, track_visibility='onchange')
    workfolio_team_id = fields.Char(string="Team Id", track_visibility='onchange')
    code = fields.Char(string="Code", readonly=True)
    active = fields.Boolean(string="Active", default=True)
    refresh_time = fields.Datetime(string="Refresh Time",track_visibility='onchange')

    wf_employee_ids = fields.One2many('wf.employee', 'wf_team_id', string='WF Employees')
    wf_timesheet_ids = fields.One2many('wf.timesheet', 'wf_timesheet_id', string='WF Timesheet')

    _sql_constraints = [
        ('code_unique', 'unique(code)', 'Code already exists!'),
    ]

    @api.model
    def create(self, vals):
        vals['code'] = self.env['ir.sequence'].next_by_code('wf.team')
        res = super(WorkfolioTeam, self).create(vals)
        return res

    def refresh(self):

        def convert(seconds):
            seconds = seconds % (24 * 3600)
            hour = seconds // 3600
            seconds %= 3600
            minutes = seconds // 60
            seconds %= 60

            return "%d:%02d:%02d" % (hour, minutes, seconds)

        auth_key = self.env['ir.config_parameter'].sudo().get_param('daffodil_workfolio_integration.auth_key')
        team_header = {'Authorization': auth_key}

        url = "https://api.workfolio.io/timesheets?teamId="+self.workfolio_team_id+"&startDate="+str(int(datetime.now().timestamp() * 1000))+"&endDate="+str(int(datetime.now().timestamp()*1000))

        response = requests.get(url, headers=team_header)

        for data in response.json():
            print(data)
            for current_time_sheet in data['days']:
                print(current_time_sheet)
                #current_time_sheet = data['days'][0]
                employee_time_sheet_dict = dict()
                employee_time_sheet_dict['email'] = data['email']
                employee_time_sheet_dict['day'] = current_time_sheet['day']
                employee_time_sheet_dict['day_type'] = current_time_sheet['dayType']
                employee_time_sheet_dict['date'] = current_time_sheet['date']
                employee_time_sheet_dict['converted_date'] = datetime.fromtimestamp((current_time_sheet['date']) / 1000.0, pytz.timezone("Asia/Dhaka")).strftime(
                    "%Y-%m-%d")
                if current_time_sheet['in']:
                    employee_time_sheet_dict['in_time'] = datetime.fromtimestamp((current_time_sheet['in'])/1000.0,pytz.timezone("Asia/Dhaka")).strftime("%Y-%m-%d %H:%M:%S")

                if current_time_sheet['out']:
                    employee_time_sheet_dict['out_time'] = datetime.fromtimestamp((current_time_sheet['out'])/1000.0,pytz.timezone("Asia/Dhaka")).strftime("%Y-%m-%d %H:%M:%S")

                employee_time_sheet_dict['worked_second'] = convert(current_time_sheet['workedSec'])
                employee_time_sheet_dict['productive_second'] = convert(current_time_sheet['productiveSec'])
                employee_time_sheet_dict['unproductive_second'] = convert(current_time_sheet['unproductiveSec'])
                employee_time_sheet_dict['neutral_second'] = convert(current_time_sheet['neutralSec'])
                employee_time_sheet_dict['idle_second'] = convert(current_time_sheet['idleSec'])
                employee_time_sheet_dict['break_second'] = convert(current_time_sheet['breakSec'])
                employee_time_sheet_dict['active_second'] = convert(current_time_sheet['activeSec'])
                employee_time_sheet_dict['wf_team_id'] = self.id


                res_user = self.env['res.users'].sudo().search([('email', '=', employee_time_sheet_dict['email'])],
                                                               limit=1)
                if res_user:
                    employee_time_sheet_dict['employee_id'] = res_user.employee_id.id
                    employee_time_sheet_dict['user_id'] = res_user.id


                is_employee_exist = self.env['wf.employee'].sudo().search(
                    [('email', '=', employee_time_sheet_dict['email'])])
                if is_employee_exist:
                    is_employee_exist.update(employee_time_sheet_dict)
                else:
                    self.env['wf.employee'].sudo().create(employee_time_sheet_dict)



                is_timesheet_exist = self.env['wf.timesheet'].sudo().search(
                    [('email', '=', employee_time_sheet_dict['email']),('date','=',employee_time_sheet_dict['date'])])
                employee_time_sheet_dict['wf_timesheet_id'] = employee_time_sheet_dict.pop('wf_team_id')

                if is_timesheet_exist:
                    is_timesheet_exist.update(employee_time_sheet_dict)
                else:
                    self.env['wf.timesheet'].sudo().create(employee_time_sheet_dict)
        self.refresh_time = datetime.now()




    @api.model
    def fields_view_get(self, view_id=None, view_type='tree', toolbar=False, submenu=False):
        res = super(WorkfolioTeam, self).fields_view_get(view_id=view_id, view_type=view_type,
                                                              toolbar=toolbar, submenu=submenu)

        # for checking team is updated or not and create team if its not updated
        if res['name'] == 'wf.team.tree.view':

            auth_key = self.env['ir.config_parameter'].sudo().get_param('daffodil_workfolio_integration.auth_key')
            team_header = {'Authorization' : auth_key}

            url = 'https://api.workfolio.io/team'

            try:
                response = requests.get(url, headers=team_header)
                for data in response.json():

                    team_info = dict()
                    team_info['workfolio_team_id'] = data['teamId']
                    team_info['name'] = data['teamName']

                    bool_team = self.env['wf.team'].sudo().search([('workfolio_team_id', '=', data['teamId'])])
                    if not bool_team:
                        self.env['wf.team'].sudo().create(team_info)

            except Exception as e:
                return res

        return res