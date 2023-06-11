from odoo import api, fields, models


class ParkingByScanning(models.TransientModel):
    _name = "parking.wizard.inout"
    _description = "Parking by Scanning"

    scanning = fields.Char(string='Record No', widget='webcam_barcode')

    # def create_target_record(self):
    #     return {
    #         'name': 'Create New Record',
    #         'type': 'ir.actions.act_window',
    #         'res_model': 'in.out.parking',
    #         'view_mode': 'form',
    #         'target': 'new',
    #         'context': {'default_source_model_id': self.id},
    #     }

    def action_print_report_employee(self):
        for rec in self:
            print(rec.scanning)
            if rec.scanning:
                result = rec.env['in.out.parking'].search([('rec_no', '=', rec.scanning)],)
                print(result)
                if result:
                    if result.state == 'in':
                        result.action_out()
                    # elif result.state == 'out':
                        # rec.create_target_record()




