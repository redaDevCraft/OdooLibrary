from odoo import models, fields

class Book(models.Model):
    _name = 'gestion_bibliotheque.book'
    _description = 'Book'
    _rec_name = 'titre'  # Set the display name to the titre field

    titre = fields.Char(string='Titre', required=True)
    langue = fields.Selection([
        ('francais', 'Français'),
        ('arabe', 'Arabe'),
        ('anglais', 'Anglais')
    ], string='Langue du livre', default='francais')
    isbn = fields.Char(string='ISBN', required=True)
    npr = fields.Integer(string='Nombre de pages')  # Number of pages
    img = fields.Binary(string='Image')  # Image of the book
    libre = fields.Boolean(string='Disponible', default=True)  # Availability

    # Many-to-one relationship to link the book to its author
    author_id = fields.Many2one('gestion_bibliotheque.author', string='Author')
