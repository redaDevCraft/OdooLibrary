from odoo import models, fields

class BorrowRecord(models.Model):
    _name = 'gestion_bibliotheque.borrow_record'
    _description = 'Borrow Record'
    _rec_name = 'id'  
    
    book_id = fields.Many2one('gestion_bibliotheque.book', string='Livre', required=True)
    member_id = fields.Many2one('gestion_bibliotheque.member', string='Membre', required=True)
    author_id = fields.Many2one('gestion_bibliotheque.author', string='Author')
    emprunt_id = fields.One2many('gestion_bibliotheque.emprunt_ligne', 'borrow_record_id', string='Emprunt')

    date_debut = fields.Date(string='Date de début', required=True)
    date_fin = fields.Date(string='Date de fin', required=True)
    rendu = fields.Selection([
        ('oui', 'Oui'),
        ('non', 'Non')
    ], string='Rendu', default='non', required=True)
