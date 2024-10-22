from odoo import models, fields

class BorrowRecord(models.Model):
    _name = 'gestion_bibliotheque.borrow_record'
    _description = 'Borrow Record'

    book_id = fields.Many2one('gestion_bibliotheque.book', string='Livre', required=True)
    member_id = fields.Many2one('gestion_bibliotheque.member', string='Membre', required=True)
    date_debut = fields.Date(string='Date de début', required=True)
    date_fin = fields.Date(string='Date de fin', required=True)
    rendu = fields.Selection([
        ('oui', 'Oui'),
        ('non', 'Non')
    ], string='Rendu', default='non', required=True)
