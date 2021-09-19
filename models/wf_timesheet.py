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

    email = fields.Char(string="Email")
    day = fields.Char(string="Total Worked Days")
    day_type = fields.Char(string="Total Worked Days")
    date = fields.Char(string="Total Worked Second")
    in_time = fields.Char(string="Total Worked Second")
    out_time = fields.Char(string="Total Worked Second")
    worked_second = fields.Char(string="Total Productive Second")
    productive_second = fields.Char(string="Productive Second")
    unproductive_second = fields.Char(string="Unproductive Second")
    neutral_second = fields.Char(string="Neutral Second")
    idle_second = fields.Char(string="Idle Second")
    break_second = fields.Char(string="Break Second")
    active_second = fields.Char(string="Active Second")

    wf_timesheet_id = fields.Many2one('wf.team', string='Team')
