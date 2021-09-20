# -*- coding: utf-8 -*-
from datetime import datetime
from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError, except_orm, UserError
import calendar
import math
import re
import requests

class WorkfolioAppWebHistory(models.Model):
    _name = 'wf.app.web.history'
    _description = "Workfolio Apps and Website History"

    title = fields.Char(string="Title")
    icon = fields.Char(string="Icon")
    productivity_status = fields.Char(string="Productivity Status")
    window_title = fields.Char(string="window Title")
    total_second = fields.Char(string="Total Second")

    wf_timesheet_id = fields.Many2one('wf.timesheet', string='Timesheet')


