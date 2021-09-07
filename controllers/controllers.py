# -*- coding: utf-8 -*-
# from odoo import http


# class DaffodilWorkfolioIntegration(http.Controller):
#     @http.route('/daffodil_workfolio_integration/daffodil_workfolio_integration/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/daffodil_workfolio_integration/daffodil_workfolio_integration/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('daffodil_workfolio_integration.listing', {
#             'root': '/daffodil_workfolio_integration/daffodil_workfolio_integration',
#             'objects': http.request.env['daffodil_workfolio_integration.daffodil_workfolio_integration'].search([]),
#         })

#     @http.route('/daffodil_workfolio_integration/daffodil_workfolio_integration/objects/<model("daffodil_workfolio_integration.daffodil_workfolio_integration"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('daffodil_workfolio_integration.object', {
#             'object': obj
#         })
