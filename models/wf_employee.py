# -*- coding: utf-8 -*-
from datetime import datetime
from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError, except_orm, UserError
import calendar
import math
import re
import requests

class WorkfolioEmployee(models.Model):
    _name = 'wf.employee'
    _description = "Workfolio Employee"

    email = fields.Char(string="Email")

    wf_team_id = fields.Many2one('wf.team', string='Team')


    # total_worked_days = fields.Char(string="Total Worked Days")
    # total_worked_second = fields.Char(string="Total Worked Second")
    # total_productive_second = fields.Char(string="Total Productive Second")
    # total_unproductive_second = fields.Char(string="Total Unproductive Second")
    # total_neutral_second = fields.Char(string="Total Neutral Second")
    # total_idle_second = fields.Char(string="Total Idle Second")
    # total_break_second = fields.Char(string="Total Break Second")
    # total_active_second = fields.Char(string="Total Active Second")