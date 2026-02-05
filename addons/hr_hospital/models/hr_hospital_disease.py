"""Disease model for HR Hospital."""
from odoo import fields, models

# pylint: disable=abstract-method


class HrHospitalDisease(models.Model):
    """Hospital disease master data."""
    _name = 'hr.hospital.disease'
    _description = 'Disease (Master Data)'
    _order = 'name'

    name = fields.Char(required=True)
    code = fields.Char()
    description = fields.Text()

    patient_ids = fields.Many2many(
        comodel_name='hr.hospital.patient',
        relation='hr_hospital_patient_disease_rel',
        column1='disease_id',
        column2='patient_id',
        string='Patients',
    )
