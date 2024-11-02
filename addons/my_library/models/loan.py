from odoo import models, fields, api

class Loan(models.Model):
    _name = 'library.loan'
    _description = 'Loan'

    borrower_id = fields.Many2one('library.borrower', string='Borrower')
    start_date = fields.Date(string='Start Date', default=fields.Date.today)
    end_date = fields.Date(string='End Date')
    returned = fields.Selection([('yes', 'Yes'), ('no', 'No')], string='Returned', default='no')
    loan_line_ids = fields.One2many('library.loan.line', 'loan_id', string='Loan Lines')

    @api.onchange('end_date')
    def _onchange_end_date(self):
        for record in self:
            if record.end_date == fields.Date.today():
                record.returned = 'yes'
