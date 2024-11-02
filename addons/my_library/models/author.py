from odoo import models, fields

class Author(models.Model):
    _name = 'library.author'
    _description = 'Author'

    name = fields.Char(string='Last Name')
    first_name = fields.Char(string='First Name')
    birth_date = fields.Date(string='Birth Date')
    nationality = fields.Char(string='Nationality')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    book_ids = fields.One2many('library.book', 'author_id', string='Books')
