# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Teachers(models.Model):
        _name = 'academy.teachers'

        name = fields.Char()
        biography = fields.Html()

        course_ids = fields.One2many('product.template', 'teacher_id', string="Courses")
#        course_ids = fields.One2many('academy.courses', 'teacher_id', string="Courses")

class Courses(models.Model):
#       _name = 'academy.courses'
#        _inherit = 'mail.thread'
        _inherit = 'product.template'

        name = fields.Char()
        teacher_id = fields.Many2one('academy.teachers', string="Teacher")


#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
