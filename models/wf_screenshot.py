# -*- coding: utf-8 -*-
from datetime import datetime
from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError, except_orm, UserError
import calendar
import math
import re
import requests

class WorkfolioScreenshot(models.Model):
    _name = 'wf.screenshot'
    _description = "Workfolio Screenshot"

    image_url = fields.Char(string="Image Url")
    thumbnail_url = fields.Char(string="Thumbnail Url")
    app_title = fields.Char(string="App Title")
    app_icon = fields.Char(string="App Icon")
    date = fields.Char(string="Date")

    wf_timesheet_id = fields.Many2one('wf.timesheet', string='Timesheet')


