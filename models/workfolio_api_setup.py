# -*- coding: utf-8 -*-
from datetime import datetime
from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError, except_orm, UserError
import calendar
import math
import re


class WorkfolioAPISetup(models.Model):
    _name = 'workfolio.api.setup'
    _description = "Chatbot Channels"

    name = fields.Char(string="Title", required=True)
    extension = fields.Char(string="Extension", readonly=True)
    auth_value = fields.Char(string="Authorization Value")
    base_url = fields.Char(string="Key")



