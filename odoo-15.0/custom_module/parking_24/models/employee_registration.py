from odoo import api, fields, models


class Employee_Parking(models.Model):
    _name = "employee.parking.reg"
    _description = "Employee Parking registration"
    _rec_name = 'vehicle_num'

    name = fields.Char(string='Name')
    emp_type = fields.Selection([('employee', 'Employee'), ('guest', 'Guest')], string="Employee Type")
    reg_no = fields.Char(string="Registration Number", readonly='1')
    vehicle_num = fields.Char(string="Vehicle Number")
    phone_num = fields.Integer(string="Phone No")
    email = fields.Char(string="Email")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('female', 'Female')], string="Gender")
    barcode = fields.Char(string="Barcode", compute="generate_barcode")
    # image = fields.Image(string="Image")

    @api.model
    def create(self, vals):
        vals['reg_no'] = self.env['ir.sequence'].next_by_code('employee.parking.reg')
        # print(vals)
        return super(Employee_Parking, self).create(vals)

    @api.onchange('reg_no', 'vehicle_num')
    def generate_barcode(self):
        my_str = ''
        for rec in self:
            if rec.reg_no:
                my_str = my_str + "ER "
                if rec.vehicle_num:
                    my_str = my_str + rec.vehicle_num.zfill(8)
            rec.barcode = my_str

    # employee_num = fields.Char(string="VEH", compute="based_condition")
    # def based_condition(self):
    #     if self.emp_type == 'employee':
    #         employee_id = fields.Integer(string="Employee ID")
    #     else:






