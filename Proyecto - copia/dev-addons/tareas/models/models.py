# -*- coding: utf-8 -*-

from odoo import models, fields, api


class tareas(models.Model):
    _name = 'tareas.tareas'
    _description = 'tareas.tareas'
    
    nombre = fields.Char()
    descripcion = fields.Text()
    fechaCreacion = fields.Date()
    fechaComienzo = fields.Datetime()
    fechaFinal = fields.Datetime()
    pausada = fields.Boolean()
    horas = fields.Integer()


class sprint(models.Model):
    _name = 'tareas.sprint'
    _description = 'tareas.sprint'

    nombre = fields.Char()
    descripcion = fields.Text()
    fechaCreacion = fields.Datetime()
    fechaFinal = fields.Datetime()


# class tecnogogias(models.Model):
#     _name = 'tareas.tecnologias'
#     _description = 'tareas.tecnologias'

#     nombre = fields.Char()
#     imagen = fields.char()
#


#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
