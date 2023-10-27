# -*- coding: utf-8 -*-

from odoo import models, fields, api


class sergio_almagre(models.Model):
    _name = 'sergio_almagre.task'
    _description = 'sergio_almagre.sergio_almagre'

    name = fields.Char()
    fecha = fields.Datetime()
    descripcion = fields.Char()

    
    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    # description = fields.Text()

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
