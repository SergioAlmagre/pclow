# -*- coding: utf-8 -*-
# from odoo import http


# class Tareas2(http.Controller):
#     @http.route('/tareas2/tareas2', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tareas2/tareas2/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tareas2.listing', {
#             'root': '/tareas2/tareas2',
#             'objects': http.request.env['tareas2.tareas2'].search([]),
#         })

#     @http.route('/tareas2/tareas2/objects/<model("tareas2.tareas2"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tareas2.object', {
#             'object': obj
#         })
