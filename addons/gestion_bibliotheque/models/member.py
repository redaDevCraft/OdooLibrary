from odoo import models, fields

class Member(models.Model):
    _name = 'gestion_bibliotheque.member'
    _description = 'Library Member'
    _rec_name = 'nom' 

    nom = fields.Char(string='Nom', required=True)
    prenom = fields.Char(string='Prénom', required=True)
    nationalite = fields.Char(string='Nationalité', default='Algérienne')
    sexe = fields.Selection([
        ('homme', 'Homme'),
        ('femme', 'Femme')
    ], string='Sexe', required=True)
    date_naissance = fields.Date(string='Date de Naissance')  # Date of birth

