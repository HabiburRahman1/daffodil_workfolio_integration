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
    in_time = fields.Char(string="In Time")
    out_time = fields.Char(string="Out Time")
    worked_second = fields.Char(string="Worked Second")
    productive_second = fields.Char(string="Productive Second")
    unproductive_second = fields.Char(string="Unproductive Second")
    neutral_second = fields.Char(string="Neutral Second")
    idle_second = fields.Char(string="Idle Second")
    break_second = fields.Char(string="Break Second")
    active_second = fields.Char(string="Active Second")
    refresh_time = fields.Datetime(string="Refresh Time", track_visibility='onchange')

    wf_timesheet_id = fields.Many2one('wf.team', string='Team')

    wf_apps_web_history_ids = fields.One2many('wf.app.web.history', 'wf_timesheet_id', string='WF Employees')

    def refresh(self):

        self.refresh_time = datetime.now()

        team_header = {
            'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcmdhbmlzYXRpb25JZCI6ImE0ZjQ0MjIwLWY1YmMtMTFlYi05ZjQ2LTM3ZDhlY2Y5ZmE1NiIsImRhdGUiOiIyMDIxLTA4LTE0VDEwOjA4OjQ3LjYzMVoiLCJpYXQiOjE2Mjg5MzU3Mjd9.SU-T_OOBLutiPOLSEn6HiFZbTIeFLhEoFcNEZPhwR3w'}

        url = "https://api.workfolio.io/appsAndWebsitesHistory?email=" + self.email + "?startDate="+ self.date + "?endDate=" + self.date

        response = requests.get(url, headers=team_header)

        print(response.json())
        app_usage_history = response.json()
        for data in app_usage_history['appUsageHistory']:
            print(data)


