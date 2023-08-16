# -*- coding: utf-8 -*-
# from odoo import http


# class ReportsHandling(http.Controller):
#     @http.route('/reports_handling/reports_handling', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/reports_handling/reports_handling/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('reports_handling.listing', {
#             'root': '/reports_handling/reports_handling',
#             'objects': http.request.env['reports_handling.reports_handling'].search([]),
#         })

#     @http.route('/reports_handling/reports_handling/objects/<model("reports_handling.reports_handling"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('reports_handling.object', {
#             'object': obj
#         })
