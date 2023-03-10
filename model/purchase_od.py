from datetime import datetime
from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    purchased_id = fields.Char(string="Purchase")


    def make_purchase(self):


        for record in self:
            lines = []
            for line in record.order_line:
                val = (0,0,
                { 
                    'product_id': line.product_id.id,
                    'product_qty': line.product_uom_qty
                })
                lines.append(val)

            sale_rec_in_purchase = record.env['purchase.order'].create({
                'partner_id' : record.partner_id.id,
                'date_order' : record.date_order,
                'order_line' : lines


            })  
