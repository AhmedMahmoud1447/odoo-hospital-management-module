from odoo import models, fields

class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Hospital Doctor Record'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Doctor Name', required=True, tracking=True)
    specialty = fields.Selection([
        ('cardiology', 'Cardiology'),
        ('dermatology', 'Dermatology'),
        ('pediatrics', 'Pediatrics'),
        ('general', 'General Medicine')
    ], string='Specialty', required=True)
    phone = fields.Char(string='Phone Number')
    email = fields.Char(string='Email')
    consultation_fee = fields.Float(string='Consultation Fee', default=0.0)
    
    appointment_ids = fields.One2many('hospital.appointment', 'doctor_id', string='Appointments')