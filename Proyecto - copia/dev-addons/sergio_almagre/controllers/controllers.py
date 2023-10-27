# -*- coding: utf-8 -*-
# from odoo import http


# class SergioAlmagre(http.Controller):
#     @http.route('/sergio_almagre/sergio_almagre', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sergio_almagre/sergio_almagre/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sergio_almagre.listing', {
#             'root': '/sergio_almagre/sergio_almagre',
#             'objects': http.request.env['sergio_almagre.sergio_almagre'].search([]),
#         })

#     @http.route('/sergio_almagre/sergio_almagre/objects/<model("sergio_almagre.sergio_almagre"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sergio_almagre.object', {
#             'object': obj
#         })
