# -*- coding: utf-8 -*-
from datetime import datetime
from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError, except_orm, UserError
import calendar
import math
import re
import requests


class WorkfolioTeam(models.Model):
    _name = 'wf.team'
    _description = "Workfolio Team"

    name = fields.Char(string="Name", required=True)
    workfolio_team_id = fields.Char(string="Team Id")
    code = fields.Char(string="Code", readonly=True)
    active = fields.Boolean(string="Active", default=True)

    _sql_constraints = [
        ('code_unique', 'unique(code)', 'Code already exists!'),
    ]

    @api.model
    def create(self, vals):
        vals['code'] = self.env['ir.sequence'].next_by_code('wf.team')
        res = super(WorkfolioTeam, self).create(vals)
        return res

    @api.model
    def fields_view_get(self, view_id=None, view_type='tree', toolbar=False, submenu=False):
        res = super(WorkfolioTeam, self).fields_view_get(view_id=view_id, view_type=view_type,
                                                              toolbar=toolbar, submenu=submenu)

        # for checking team is updated or not and create team if its not updated
        if res['name'] == 'wf.team.tree.view':

            team_header = {'Authorization' : 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcmdhbmlzYXRpb25JZCI6ImE0ZjQ0MjIwLWY1YmMtMTFlYi05ZjQ2LTM3ZDhlY2Y5ZmE1NiIsImRhdGUiOiIyMDIxLTA4LTE0VDEwOjA4OjQ3LjYzMVoiLCJpYXQiOjE2Mjg5MzU3Mjd9.SU-T_OOBLutiPOLSEn6HiFZbTIeFLhEoFcNEZPhwR3w'}

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