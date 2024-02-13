# -*- coding: utf-8 -*-
# from odoo import http


# class ListaTareasModule(http.Controller):
#     @http.route('/lista_tareas_module/lista_tareas_module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lista_tareas_module/lista_tareas_module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('lista_tareas_module.listing', {
#             'root': '/lista_tareas_module/lista_tareas_module',
#             'objects': http.request.env['lista_tareas_module.lista_tareas_module'].search([]),
#         })

#     @http.route('/lista_tareas_module/lista_tareas_module/objects/<model("lista_tareas_module.lista_tareas_module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lista_tareas_module.object', {
#             'object': obj
#         })

