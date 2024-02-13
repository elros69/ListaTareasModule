# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class lista_tareas_module(models.Model):
#     _name = 'lista_tareas_module.lista_tareas_module'
#     _description = 'lista_tareas_module.lista_tareas_module'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

