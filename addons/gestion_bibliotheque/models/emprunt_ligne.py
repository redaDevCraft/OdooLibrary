from odoo import models, fields

class EmpruntLigne(models.Model):
    _name = 'gestion_bibliotheque.emprunt_ligne'
    _description = 'Emprunt Ligne'

    langue = fields.Selection([
        ('francais', 'Français'),
        ('arabe', 'Arabe'),
        ('anglais', 'Anglais')
    ], string='Langue du livre', default='francais')
    isbn = fields.Char(string='ISBN', required=True)
    npr = fields.Integer(string='Nombre de pages')
    book_id = fields.Many2one('gestion_bibliotheque.book', string='Livre', required=True)
    borrow_record_id = fields.Many2one('gestion_bibliotheque.borrow_record', string='Borrow', required=True)