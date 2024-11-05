from odoo import models, fields, api

class EmpWizard(models.TransientModel):
    _name = 'library.empwizard'
    _description = 'Wizard to add borrow records'

    borrower_id = fields.Many2one('res.partner', string='Borrower', required=True)
    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', required=True)

    @api.model
    def default_get(self, fields):
        res = super(EmpWizard, self).default_get(fields)
        return res

    def add_borrow(self):
        borrow_record = self.env['library.borrow_record'].create({
            'borrower_id': self.borrower_id.id,
            'start_date': self.start_date,
            'end_date': self.end_date,
        })
        
        borrow_lines = []
        books = self.env['library.book'].search([])
        for book in books:
            borrow_lines.append((0, 0, {
                'book_id': book.id,
                'borrow_record_id': borrow_record.id,
            }))
        
        borrow_record.write({'borrow_line_ids': [(6, 0, [line[2]['book_id'] for line in borrow_lines])]})
        
        return {'type': 'ir.actions.act_window_close'}