from odoo import api, fields, models


class CustomerParkingReport(models.TransientModel):
    _name = "customer.parking.report"
    _description = "Customer Parking Report"

    emp_rec_id = fields.Many2one("employee.parking.reg", string='Employee')
    date_form = fields.Date(string='Date From')
    date_to = fields.Date(string='Date To')
    type = fields.Selection([('employee', 'Employee'), ('guest', 'Guest')], string="Employee Type")

    def action_print_report_employee(self):
        domain = []
        type = self.type
        if type:
            domain += [('emp_type', '=', type)]
        rec_id = self.emp_rec_id
        if rec_id:
            domain += [('veh_num', '=', rec_id.id)]
        date_form = self.date_form
        if date_form:
            domain += [('entry_time', '>=', date_form)]
        date_to = self.date_to
        if date_to:
            domain += [('exit_time', '<=', date_to)]

        records = self.env['in.out.parking'].search_read(domain)
        data = {
            'record': records,
        }
        return self.env.ref('parking_24.report_employee_inout').report_action(self, data=data)
