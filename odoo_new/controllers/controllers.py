# -*- coding: utf-8 -*-
# from odoo import http


# class OdooNew(http.Controller):
#     @http.route('/odoo_new/odoo_new', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_new/odoo_new/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_new.listing', {
#             'root': '/odoo_new/odoo_new',
#             'objects': http.request.env['odoo_new.odoo_new'].search([]),
#         })

#     @http.route('/odoo_new/odoo_new/objects/<model("odoo_new.odoo_new"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_new.object', {
#             'object': obj
#         })
