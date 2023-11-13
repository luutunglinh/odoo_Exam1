# -*- coding: utf-8 -*-
# from odoo import http


# class Odoo2(http.Controller):
#     @http.route('/odoo_2/odoo_2', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_2/odoo_2/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_2.listing', {
#             'root': '/odoo_2/odoo_2',
#             'objects': http.request.env['odoo_2.odoo_2'].search([]),
#         })

#     @http.route('/odoo_2/odoo_2/objects/<model("odoo_2.odoo_2"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_2.object', {
#             'object': obj
#         })
