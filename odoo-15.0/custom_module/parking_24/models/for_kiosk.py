from odoo import api, fields, models


class KioskAttendance(models.Model):
    _name = 'kiosk.attendance'
    _description = 'Kiosk Attendance'

    vehicle_num = fields.Many2one('employee.parking.reg', string='Vehicle Number', store=True)
    employee_id = fields.Char(related="vehicle_num.reg_no", string="Registration Number")
    check_in = fields.Datetime(string='Check In', readonly=True)
    check_out = fields.Datetime(string='Check Out', readonly=True)
    barcode = fields.Char(string='Scanned Barcode')

    @api.model
    def action_check_in(self):
        employee = self.employee_id
        if not employee:
            return

        attendance = self.search([('employee_id', '=', employee.id), ('check_out', '=', False)])
        if attendance:
            attendance.write({'check_out': fields.Datetime.now()})

        self.create({'employee_id': employee.id, 'check_in': fields.Datetime.now()})

    @api.model
    def action_check_out(self):
        employee = self.employee_id
        if not employee:
            return

        attendance = self.search([('employee_id', '=', employee.id), ('check_out', '=', False)])
        if attendance:
            attendance.write({'check_out': fields.Datetime.now()})


