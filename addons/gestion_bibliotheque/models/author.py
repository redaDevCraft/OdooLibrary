from odoo import models, fields

class Author(models.Model):
    _name = 'gestion_bibliotheque.author'
    _description = 'Author'

    nom = fields.Char(string='Nom', required=True)
    prenom = fields.Char(string='Prénom', required=True)
    nationalite = fields.Char(string='Nationalité', default='Algérienne')
    sexe = fields.Selection([
        ('homme', 'Homme'),
        ('femme', 'Femme')
    ], string='Sexe', required=True)
    
    # One-to-many relationship to link books written by the author
    book_ids = fields.One2many('gestion_bibliotheque.book', 'author_id', string='Books Written')
