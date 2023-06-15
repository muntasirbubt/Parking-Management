from odoo import api, fields, models, _
from datetime import datetime


class InOutParking(models.Model):
    _name = "in.out.parking"
    _description = "Parking In Out"
    _rec_name = 'rec_no'
    _order = 'id desc'

    veh_num = fields.Many2one('employee.parking.reg', string='Vehicle Number', tracking=1)
    emp_type = fields.Selection(related='veh_num.emp_type', string="Employee Type")
    emp_name = fields.Char(related='veh_num.name', string="Employee Name")
    gender = fields.Selection(related='veh_num.gender', string="Gender")
    barcode = fields.Char(related="veh_num.barcode", string="Barcode")
    state = fields.Selection([('in', 'IN'), ('out', 'OUT')], string="State", default='in', readonly=True)
    entry_time = fields.Datetime(string="Entry Time", default=fields.Datetime.now, readonly=True)
    exit_time = fields.Datetime(string="Exit Time", readonly=True)
    rec_no = fields.Char(string="Record Number")

    # duration = fields.Float(string='Duration (Minute)', compute='_compute_duration')

    # def _compute_duration(self):
    #     for record in self:
    #         if record.entry_time and record.exit_time:
    #             entry_datetime = datetime.strptime(record.entry_time, '%Y-%m-%d %H:%M:%S')
    #             exit_datetime = datetime.strptime(record.exit_time, '%Y-%m-%d %H:%M:%S')
    #             duration = exit_datetime - entry_datetime
    #             record.duration = duration.total_seconds() / 60  # Convert duration to hours
    #
    #         else:
    #             record.duration = 0.0

    # def action_in(self):
    #     for rec in self:
    #         if rec.state == '':
    #             rec.state = 'in'

    def action_out(self):
        for rec in self:
            if rec.state == 'in':
                rec.state = 'out'
                print("action_out entered")
                rec.exit_time = datetime.now()
            else:
                print("Already in Out state")

    @api.model
    def create(self, vals):
        vals['rec_no'] = self.env['ir.sequence'].next_by_code('in.out.parking')
        return super(InOutParking, self).create(vals)

    @api.model
    def attendance_scan2(self, barcode):
        """ Receive a barcode scanned from the Kiosk Mode and change the attendances of corresponding employee.
            Returns either an action or a warning.
        """
        employee = self.env['in.out.parking'].search([('rec_no', '=', barcode)], limit=1)
        if employee:
            for rec in employee:
                if rec.state == 'in':
                    rec.state = 'out'
                    print("action_out entered")
                    rec.exit_time = datetime.now()
                    self.env.user.notify_success(message='State changed into IN')

                else:
                    print("Already in Out state")
                    self.env.user.notify_warning(message='Already Out state')

        return {'warning': _("")}
# class IndividualRecord(models.Model):
#     _name = "individual.record"
#     _description = "Employee Individual Record"
#
#     sl_no = fields.Integer(string="Sl.No")
#     record_id = fields.Many2one('employee.parking.reg', required=True)

