from odoo import models, fields,api

class Borrower(models.Model):
    _name = 'library.borrower'
    _description = 'Borrower'

    name = fields.Char(string='Name')
    first_name = fields.Char(string='First Name')
    birth_date = fields.Date(string='Birth Date')
    state = fields.Char(string='State')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    loan_count = fields.Integer(string='Loan Count', compute='_compute_loan_count')
    loan_ids = fields.One2many('library.loan', 'borrower_id', string='Loans')

    def _compute_loan_count(self):
        for record in self:
            record.loan_count = len(record.loan_ids)

    def unlink(self):
        loan_model = self.env['library.loan']
        for borrower in self:
           
            loans = loan_model.search([('borrower_id', '=', borrower.id)])
            loans.unlink()
        return super(Borrower, self).unlink()