"""Doctor model for HR Hospital."""
from odoo import api, fields, models

# pylint: disable=abstract-method


class HrHospitalDoctor(models.Model):
    """Hospital doctor records."""
    _name = 'hr.hospital.doctor'
    _description = 'Hospital Doctor'
    _order = 'name'

    name = fields.Char(required=True)
    active = fields.Boolean(default=True)

    phone = fields.Char()
    email = fields.Char()
    specialization = fields.Char()

    supervisor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
        string='Supervising Doctor',
        ondelete='set null',
    )
    supervisee_ids = fields.One2many(
        comodel_name='hr.hospital.doctor',
        inverse_name='supervisor_id',
        string='Supervised Doctors',
    )

    patient_ids = fields.One2many(
        comodel_name='hr.hospital.patient',
        inverse_name='doctor_id',
        string='Patients',
    )

    visit_ids = fields.One2many(
        comodel_name='hr.hospital.visit',
        inverse_name='doctor_id',
        string='Visits',
    )

    patient_count = fields.Integer(
        compute='_compute_patient_count',
        string='Patients Count',
    )
    visit_count = fields.Integer(
        compute='_compute_visit_count',
        string='Visits Count',
    )

    @api.depends('patient_ids')
    def _compute_patient_count(self):
        for rec in self:
            rec.patient_count = len(rec.patient_ids)

    @api.depends('visit_ids')
    def _compute_visit_count(self):
        for rec in self:
            rec.visit_count = len(rec.visit_ids)
