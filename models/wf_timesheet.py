# -*- coding: utf-8 -*-
from datetime import datetime
from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError, except_orm, UserError
import calendar
import math
import re
import requests

class WorkfolioTimesheet(models.Model):

    _name = 'wf.timesheet'
    _description = "Workfolio Timesheet"
    _inherit = ['mail.thread']

    email = fields.Char(string="Email")
    day = fields.Char(string="Day")
    day_type = fields.Char(string="Day Type")
    date = fields.Char(string="Date")
    in_time = fields.Datetime(string="In Time")
    out_time = fields.Datetime(string="Out Time")
    worked_second = fields.Char(string="Worked Hour")
    productive_second = fields.Char(string="Productive Hour")
    unproductive_second = fields.Char(string="Unproductive Hour")
    neutral_second = fields.Char(string="Neutral Hour")
    idle_second = fields.Char(string="Idle Hour")
    break_second = fields.Char(string="Break Hour")
    active_second = fields.Char(string="Active Hour")
    refresh_time = fields.Datetime(string="Refresh Time", track_visibility='onchange')

    wf_timesheet_id = fields.Many2one('wf.team', string='Team')

    wf_apps_web_history_ids = fields.One2many('wf.app.web.history', 'wf_timesheet_id', string='WF Employees')
    wf_screenshot_ids = fields.One2many('wf.screenshot', 'wf_timesheet_id', string='WF Screenshot')
    employee_id = fields.Many2one('hr.employee', string='Responsible Person')
    user_id = fields.Many2one('res.users', string='Responsible User')

    def refresh(self):

        self.refresh_time = datetime.now()

        team_header = {
            'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcmdhbmlzYXRpb25JZCI6ImE0ZjQ0MjIwLWY1YmMtMTFlYi05ZjQ2LTM3ZDhlY2Y5ZmE1NiIsImRhdGUiOiIyMDIxLTA4LTE0VDEwOjA4OjQ3LjYzMVoiLCJpYXQiOjE2Mjg5MzU3Mjd9.SU-T_OOBLutiPOLSEn6HiFZbTIeFLhEoFcNEZPhwR3w'}

        url = "https://api.workfolio.io/appsAndWebsitesHistory?userEmail=" + self.email + "&startDate="+ self.date + "&endDate=" + self.date

        response = requests.get(url, headers=team_header)

        app_usage_history = response.json()

        if app_usage_history:
            for data in app_usage_history['appUsageHistory']:

                app_usage_history_dict = dict()
                app_usage_history_dict['title'] = data['title']
                app_usage_history_dict['icon'] = data['icon']
                app_usage_history_dict['productivity_status'] = data['productivityStatus']
                app_usage_history_dict['window_title'] = data['windowTitle']
                app_usage_history_dict['date'] = data['date']
                app_usage_history_dict['total_second'] = data['totalSec']
                app_usage_history_dict['wf_timesheet_id'] = self.id
                is_history_exist = self.env['wf.app.web.history'].sudo().search(
                    [('title', '=', data['title']),('window_title','=',data['windowTitle'])])
                
                if is_history_exist:
                    is_history_exist.update(app_usage_history_dict)

                else:
                    self.env['wf.app.web.history'].sudo().create(app_usage_history_dict)

        url_screenshot = "https://api.workfolio.io/screenshot?userEmail=" + self.email + "&startDate=" + self.date + "&endDate=" + self.date

        response = requests.get(url_screenshot, headers=team_header)

        screenshot = response.json()

        print(screenshot)

        if screenshot:
            for data in screenshot['screenshots']:
                screenshot_dict = dict()
                screenshot_dict['image_url'] = data['imageUrl']
                screenshot_dict['thumbnail_url'] = data['thumbnailUrl']
                screenshot_dict['app_title'] = data['appTitle']
                screenshot_dict['app_icon'] = data['appIcon']
                screenshot_dict['date'] = data['date']
                screenshot_dict['wf_timesheet_id'] = self.id

                is_screenshot_exist = self.env['wf.screenshot'].sudo().search(
                    [('app_title', '=', data['appTitle']), ('date', '=', data['date'])])

                if is_screenshot_exist:
                    is_screenshot_exist.update(screenshot_dict)
                else:
                    self.env['wf.screenshot'].sudo().create(screenshot_dict)








                

        


