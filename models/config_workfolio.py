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

    daffodil_workfolio_integration_confidence_threshold = fields.Float(string="Confidence Threshold", default=45)
    daffodil_workfolio_integration_image_chatbot_avatar = fields.Binary(string='Chatbot Avatar', attachment=True, store=True, help="Set image as Chatbot Avatar.")
    daffodil_workfolio_integration_image_visitor_avatar = fields.Binary(string='Visitor Avatar', attachment=True, store=True, help="Set image as Visitor Avatar.")
    daffodil_workfolio_integration_voice_speak = fields.Boolean(string="Voice Speak")
    daffodil_workfolio_integration_voice_listen = fields.Boolean(string="Voice Listen")
    daffodil_workfolio_integration_default_message = fields.Text(string="Default Message")
    daffodil_workfolio_integration_low_confidence_message = fields.Text(string="Low Confidence Message")
    daffodil_workfolio_integration_error_message = fields.Text(string="Error Message")


    @api.model
    def get_values(self):
        res = super(WorkfolioSettings, self).get_values()
        res.update(
            daffodil_workfolio_integration_confidence_threshold = float(self.env['ir.config_parameter'].sudo().get_param('daffodil_workfolio_integration.confidence_threshold')),
            daffodil_workfolio_integration_image_chatbot_avatar = self.env['ir.config_parameter'].sudo().get_param('daffodil_workfolio_integration.image_chatbot_avatar'),
            daffodil_workfolio_integration_image_visitor_avatar = self.env['ir.config_parameter'].sudo().get_param('daffodil_workfolio_integration.image_visitor_avatar'),
            daffodil_workfolio_integration_voice_speak = self.env['ir.config_parameter'].sudo().get_param('daffodil_workfolio_integration.voice_speak'),
            daffodil_workfolio_integration_voice_listen = self.env['ir.config_parameter'].sudo().get_param('daffodil_workfolio_integration.voice_listen'),
            daffodil_workfolio_integration_default_message = self.env['ir.config_parameter'].sudo().get_param('daffodil_workfolio_integration.default_message'),
            daffodil_workfolio_integration_low_confidence_message = self.env['ir.config_parameter'].sudo().get_param('daffodil_workfolio_integration.low_confidence_message'),
            daffodil_workfolio_integration_error_message = self.env['ir.config_parameter'].sudo().get_param('daffodil_workfolio_integration.error_message'),
        )
        return res

    
    def set_values(self):
        super(WorkfolioSettings, self).set_values()
        param = self.env['ir.config_parameter'].sudo()
        param.set_param('daffodil_workfolio_integration.confidence_threshold', str(self.daffodil_workfolio_integration_confidence_threshold))
        param.set_param('daffodil_workfolio_integration.image_chatbot_avatar', self.daffodil_workfolio_integration_image_chatbot_avatar)
        param.set_param('daffodil_workfolio_integration.image_visitor_avatar', self.daffodil_workfolio_integration_image_visitor_avatar)
        param.set_param('daffodil_workfolio_integration.voice_speak', self.daffodil_workfolio_integration_voice_speak)
        param.set_param('daffodil_workfolio_integration.voice_listen', self.daffodil_workfolio_integration_voice_listen)
        param.set_param('daffodil_workfolio_integration.default_message', self.daffodil_workfolio_integration_default_message)
        param.set_param('daffodil_workfolio_integration.low_confidence_message', self.daffodil_workfolio_integration_low_confidence_message)
        param.set_param('daffodil_workfolio_integration.error_message', self.daffodil_workfolio_integration_error_message)

