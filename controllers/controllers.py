# -*- coding: utf-8 -*-
from odoo import http


class Academy(http.Controller):
    @http.route('/academy/academy/', auth='public' , website='true')
    def index(self, **kw):
        Teachers = http.request.env['academy.teachers']
        return http.request.render('academy.index', {
            'teachers': Teachers.search([])
        })

#    @http.route('/academy/<name>/', auth='public', website=True)
#    def teacher(self, name):
#        return '<h1>{}</h1>'.format(name)

#to ensure it takes only an integer
#    @http.route('/academy/<int:id>/', auth='public', website=True)
#    def teacher(self, id):
#        return '<h1>{} ({})</h1>'.format(id, type(id).__name__)


# Odoo provides an additional converter called model which provides records 
# directly when given their id.
# http://localhost:8069/academy/3/
    @http.route('/academy/<model("academy.teachers"):teacher>/', auth='public', website=True)
    def teacher(self, teacher):
        return http.request.render('academy.biography', {
            'person': teacher
        })



#class Academy(http.Controller):
#     @http.route('/academy/academy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#        return http.request.render('academy.index', {
#            'teachers': ["Diana Padilla", "Jody Caroll", "Lester Vaughn"],
#        })

       

#     @http.route('/academy/academy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('academy.listing', {
#             'root': '/academy/academy',
#             'objects': http.request.env['academy.academy'].search([]),
#         })

#     @http.route('/academy/academy/objects/<model("academy.academy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('academy.object', {
#             'object': obj
#         })
