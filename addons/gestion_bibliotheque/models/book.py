from odoo import models, fields

class Book(models.Model):
    _name = 'gestion_bibliotheque.book'
    _description = 'Book'
    _rec_name = 'isbn' 
    
    
    
    
    titre = fields.Char(string='Titre', required=True)
    langue = fields.Selection([
        ('francais', 'Français'),
        ('arabe', 'Arabe'),
        ('anglais', 'Anglais')
    ], string='Langue du livre', default='francais')
    isbn = fields.Char(string='ISBN', required=True)
    npr = fields.Integer(string='Nombre de pages') 
    img = fields.Binary(string='Image') 
    libre = fields.Boolean(string='Disponible', default=True)  

    
    author_id = fields.Many2one('gestion_bibliotheque.author', string='Author')
    emprunt_id = fields.One2many('gestion_bibliotheque.emprunt_ligne', 'book_id', string='Emprunt')
    
