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
    day = fields.Char(string="Day")
    day_type = fields.Char(string="Day Type")
    date = fields.Char(string="Date")
    converted_date = fields.Char(string="Date")
    in_time = fields.Datetime(string="In Time")
    out_time = fields.Datetime(string="Out Time")

    worked_second = fields.Char(string="Worked Hour")
    productive_second = fields.Char(string="Productive Hour")
    unproductive_second = fields.Char(string="Unproductive Hour")
    neutral_second = fields.Char(string="Neutral Hour")
    idle_second = fields.Char(string="Idle Hour")
    break_second = fields.Char(string="Break Hour")
    active_second = fields.Char(string="Active Hour")

    workfolio_worked_second = fields.Char(string="Worked Hour")
    workfolio_productive_second = fields.Char(string="Productive Hour")
    workfolio_unproductive_second = fields.Char(string="Unproductive Hour")
    workfolio_neutral_second = fields.Char(string="Neutral Hour")
    workfolio_idle_second = fields.Char(string="Idle Hour")
    workfolio_break_second = fields.Char(string="Break Hour")
    workfolio_active_second = fields.Char(string="Active Hour")



    wf_team_id = fields.Many2one('wf.team', string='Team')

    employee_id = fields.Many2one('hr.employee', string='Responsible Person')
    user_id = fields.Many2one('res.users', string='Responsible User')
