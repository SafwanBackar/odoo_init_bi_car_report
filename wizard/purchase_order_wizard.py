from odoo import models, fields, api

class PurchaseWizard(models.TransientModel):
    _name = 'purchase.wizard'
    _description = 'PurchaseWizard'
    

    start_date = fields.Date('Start Date')
    end_date = fields.Date('End Date')
    partner_id = fields.Many2one('res.partner', string='Partner')

    def export_xls_report(self):
        data = {
            "ids": self.ids,
            "model": self._name,
            "form": {
                "start_date": self.start_date,
                "end_date": self.end_date,
                "partner_id": self.partner_id.id
            },
        }
        return self.env.ref("bi_car_report.my_xl_report_model").report_action(
            self, data=data, config=False
        )
