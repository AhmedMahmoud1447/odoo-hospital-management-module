{
    'name': 'Hospital Management System',
    'version': '17.0.1.0.0',
    'category': 'Healthcare',
    'summary': 'Manage Patients, Doctors, and Appointments',
    'description': """Custom Odoo module for managing hospital workflows.""",
    'author': 'Ahmed',
    'depends': ['base', 'mail'],
   'data': [
        'security/ir.model.access.csv',
        'views/patient_views.xml',
        'views/doctor_views.xml',
        'views/appointment_views.xml',
        'views/menus.xml',
    ],
    'installable': True,
    'application': True,
}