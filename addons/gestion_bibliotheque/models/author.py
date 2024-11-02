from odoo import models, fields

class Author(models.Model):
    _name = 'gestion_bibliotheque.author'
    _description = 'Author'
    _rec_name = 'nom' 


    nom = fields.Char(string='Le Nom', required=True)
    prenom = fields.Char(string='Prénom', required=True)
    nationalite = fields.Char(string='Nationalité', default='Algérien')
    sexe = fields.Selection([
        ('homme', 'Homme'),
        ('femme', 'Femme')
    ], string='Sexe', required=True)
    
    
    book_ids = fields.One2many('gestion_bibliotheque.book', 'author_id', string='Books Written')
