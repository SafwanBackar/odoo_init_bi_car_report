from datetime import datetime
from odoo import models


class PurchaseReportxlsx(models.AbstractModel):
    _name = "report.bi_car_report.my_xl_report"
    _inherit = "report.report_xlsx.abstract"

    def generate_xlsx_report(self, workbook, data, lines):
        sheet = workbook.add_worksheet("Purchase Report")
        start_date = data["form"]["start_date"]
        end_date = data["form"]["end_date"]
        partner_id = data["form"]["partner_id"]

        heading_format = workbook.add_format({'bold':1,'align':'center','border':2,})
        table_content_head_format = workbook.add_format({'align':'center','border':2})
        my_right_format = workbook.add_format({'border':1,})
        table_bottom_format = workbook.add_format({'bottom':2,})
        
        po_ids = self.env['purchase.order'].search([('date_approve','>=',start_date),('date_approve','<=',end_date),('partner_id', '=', partner_id)])    

        sheet.write('C4', po_ids.company_id.name , heading_format)
        sheet.set_column('D:D', 25)
        sheet.set_column('C:C', 20)
        sheet.set_column('A:A', 12)
        sheet.set_column('B:B', 12)
        sheet.write('A6', start_date)
        sheet.write('A7', end_date)
        sheet.write('A9', "SL No", table_content_head_format)
        sheet.write('B9', "Vendor", table_content_head_format)
        sheet.write('C9', "Date", table_content_head_format)
        sheet.write('D9', "Product", table_content_head_format)
        sheet.write('E9', "Unit", table_content_head_format)
        sheet.write('F9', "Price", table_content_head_format)
        row = 10
        sl = 1
        for po_id in po_ids:
            sheet.write('A%s' %row, sl, my_right_format)
            sheet.write('B%s' %row, po_id.partner_id.name, my_right_format)
            # print('$$$$$$$$$$$$$$$$$$$$$$')
            sheet.write('C%s' %row, po_id.date_order.strftime("%d-%m-%y"), my_right_format)
            for line in po_id.order_line:
                sheet.write('D%s' %row, line.product_id.name, my_right_format)
                sheet.write('E%s' %row, line.price_unit, my_right_format)
                sheet.write('F%s' %row, line.price_subtotal, my_right_format)
                row += 1
            sl += 1
        
        
        
        
        
        
        
        
        
        
        # sheet.write('F10', "", my_right_format)
        # sheet.write('F11', "", my_right_format)
        # sheet.write('F12', "", my_right_format)
        # sheet.write('F13', "", my_right_format)
        # sheet.write('F14', "", my_right_format)
        # sheet.write('F15', "", my_right_format)
        # sheet.write('A15', "", table_bottom_format)
        # sheet.write('B15', "", table_bottom_format)
        # sheet.write('C15', "", table_bottom_format)
        # sheet.write('D15', "", table_bottom_format)
        # sheet.write('E15', "", table_bottom_format)
        # sheet.write('F15', "", table_bottom_format)
        