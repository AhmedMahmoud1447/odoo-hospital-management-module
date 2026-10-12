from odoo import models, fields, api, _
from odoo.exceptions import UserError

class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Hospital Appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Appointment Reference', required=True, readonly=True, default=lambda self: _('New'))
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True, tracking=True)
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor', required=True, tracking=True)
    appointment_date = fields.Datetime(string='Appointment Date', default=fields.Datetime.now, required=True)
    
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')
    ], string='Status', default='draft', tracking=True)

    # رابط الفاتورة المنشأة
    invoice_id = fields.Many2one('account.move', string='Invoice', readonly=True)

    # إنشاء Sequence تلقائي للموعد (مثل APP0001)
    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment') or _('New')
        return super(HospitalAppointment, self).create(vals)

    # أكشن لتأكيد الموعد وإنشاء الفاتورة
    def action_confirm(self):
        for rec in self:
            rec.state = 'confirmed'
            # إنشاء فاتورة عميل تلقائياً في موديول החسابات (account.move)
            invoice = self.env['account.move'].create({
                'move_type': 'out_invoice',
                'partner_id': rec.patient_id.id, # يمكنك إضافة مقترن للعميل أو ربطه بالـ Partner
                'invoice_date': fields.Date.today(),
                'invoice_line_ids': [(0, 0, {
                    'name': f"Consultation Fee - Dr. {rec.doctor_id.name}",
                    'quantity': 1,
                    'price_unit': rec.doctor_id.consultation_fee,
                })]
            })
            rec.invoice_id = invoice.id