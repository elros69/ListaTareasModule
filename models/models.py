# -*- coding: utf-8 -*-

from odoo import models, fields, api

#Definimos el modelo de datos
class lista_tareas(models.Model):
    #Nombre y descripcion del modelo de datos
    _name = 'lista_tareas.lista'
    _description = 'Modelo de la lista de tareas'
    _rec_name="tarea"
    
    tarea = fields.Char()       
    prioridad = fields.Integer()
    urgente = fields.Boolean(compute="_value_urgente", store=True)
    realizada = fields.Boolean()
    fecha_inicio = fields.Date(
        string='Patata',
        default=fields.Date.context_today,
    )
    @api.depends('prioridad')
    def _value_urgente(self):
        #Para cada registro... (recordamos, self es el modelo, no un registro)
        for record in self:
            #Si la prioridad es mayor que 10, se considera urgente, en otro caso no lo es
            if record.prioridad>10:
                record.urgente = True
            else:
                record.urgente = False
