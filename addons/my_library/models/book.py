from odoo import models, fields

class Book(models.Model):
    _name = 'library.book'
    _description = 'Book'

    title = fields.Char(string='Title')
    language = fields.Selection([('fr', 'French'), ('ar', 'Arabic'), ('en', 'English')], string='Language')
    isbn = fields.Char(string='ISBN')
    page_count = fields.Integer(string='Page Count')
    cover_image = fields.Binary(string='Cover Image')
    author_id = fields.Many2one('library.author', string='Author')
    loan_line_ids = fields.One2many('library.loan.line', 'book_id', string='Loan Lines')
