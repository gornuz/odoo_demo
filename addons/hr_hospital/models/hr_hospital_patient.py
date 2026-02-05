"""Patient model for HR Hospital."""
from odoo import api, fields, models

# pylint: disable=abstract-method


class HrHospitalPatient(models.Model):
    """Hospital patient records."""
    _name = 'hr.hospital.patient'
    _description = 'Hospital Patient'
    _order = 'name'

    name = fields.Char(required=True)
    active = fields.Boolean(default=True)

    birthdate = fields.Date()
    gender = fields.Selection(
        selection=[
            ('male', 'Male'),
            ('female', 'Female'),
            ('other', 'Other'),
        ],
        default='other',
    )

    phone = fields.Char()
    email = fields.Char()

    doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
        string='Attending Doctor',
        ondelete='set null',
    )

    disease_ids = fields.Many2many(
        comodel_name='hr.hospital.disease',
        relation='hr_hospital_patient_disease_rel',
        column1='patient_id',
        column2='disease_id',
        string='Diseases',
    )

    visit_ids = fields.One2many(
        comodel_name='hr.hospital.visit',
        inverse_name='patient_id',
        string='Visits',
    )

    visit_count = fields.Integer(
        compute='_compute_visit_count',
        string='Visits Count',
    )

    note = fields.Text()

    @api.depends('visit_ids')
    def _compute_visit_count(self):
        for rec in self:
            rec.visit_count = len(rec.visit_ids)
