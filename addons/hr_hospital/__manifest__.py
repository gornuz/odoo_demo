{
    'name': 'HR Hospital',
    'version': '19.0.1.0.0',
    'category': 'Human Resources',
    'summary': 'Hospital management: doctors, patients, diseases, visits',
    'license': 'LGPL-3',
    'author': 'Odoo Community Association (OCA)',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/hr_hospital_disease_data.xml',
        'views/hr_hospital_actions.xml',
        'views/hr_hospital_doctor_views.xml',
        'views/hr_hospital_patient_views.xml',
        'views/hr_hospital_disease_views.xml',
        'views/hr_hospital_visit_views.xml',
        'views/hr_hospital_menus.xml',
    ],
    'demo': [
        'demo/hr_hospital_demo.xml',
    ],
    'application': True,
}
