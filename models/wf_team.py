# -*- coding: utf-8 -*-
from datetime import datetime
from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError, except_orm, UserError
import calendar
import math
import re


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
        print("I am not working")
        print(vals['code'])
        return res

    # @api.model
    # def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
    #     res = super(ChrimsAccountGroup, self).fields_view_get(view_id=view_id, view_type=view_type,
    #                                                           toolbar=toolbar, submenu=submenu)
    #     return res