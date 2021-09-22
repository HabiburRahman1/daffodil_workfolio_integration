# -*- coding: utf-8 -*-
from datetime import datetime
from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError, except_orm, UserError
import calendar
import math
import re


class WorkfolioSettings(models.TransientModel):
    _inherit = "res.config.settings"
    _name = "workfolio.config.settings"
    _description = 'Chatbot Configurations'

    daffodil_workfolio_integration_auth_key = fields.Text(string="Auth Key", default="Authorization")



    @api.model
    def get_values(self):
        res = super(WorkfolioSettings, self).get_values()
        res.update(
            daffodil_workfolio_integration_auth_key = self.env['ir.config_parameter'].sudo().get_param('daffodil_workfolio_integration.auth_key'),
        )
        return res

    
    def set_values(self):
        super(WorkfolioSettings, self).set_values()
        param = self.env['ir.config_parameter'].sudo()
        param.set_param('daffodil_workfolio_integration.auth_key', self.daffodil_workfolio_integration_auth_key)
