# -*- coding: utf-8 -*-

from odoo import models, fields, api


class tareas(models.Model):
    _name = 'tareas2.tareas2'
    _description = 'tareas2.tareas2'
    
    nombre = fields.Char(string='Nombre', required=True, help='Introducir nombre')
    descripcion = fields.Text()
    fechaCreacion = fields.Date()
    fechaComienzo = fields.Datetime()
    fechaFinal = fields.Datetime()
    pausada = fields.Boolean()
    horas = fields.Integer()

  # Relaciones
    sprint_id = fields.Many2one('tareas2.sprint2', string='Sprint')
    tecnologias_ids = fields.Many2many('tareas2.tecnologias2', string='Tecnologías')


class sprint(models.Model):
    _name = 'tareas2.sprint2'
    _description = 'tareas2.sprint2'    

    nombre = fields.Char()
    descripcion = fields.Text()
    fechaCreacion = fields.Datetime()
    fechaFinal = fields.Datetime()

    # Relaciones
    tarea_ids = fields.One2many('tareas2.tareas2', 'sprint_id', string='Tareas')


class tecnologias(models.Model):
    _name = 'tareas2.tecnologias2' 
    _description = 'tareas2.tecnologias2'

    nombre = fields.Char()
    imagen = fields.Binary(string='Foto', attachment=True, help='Añade una imagen con max. anchura de 200 y max. altura de 200')

    # Relaciones
    tareas_ids = fields.Many2many('tareas2.tareas2', string='Tareas')
