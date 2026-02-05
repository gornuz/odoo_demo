"""Visit model for HR Hospital."""
from odoo import api, fields, models

# pylint: disable=abstract-method


class HrHospitalVisit(models.Model):
    """Hospital patient visit records."""
    _name = 'hr.hospital.visit'
    _description = 'Patient Visit'
    _order = 'visit_datetime desc, id desc'

    name = fields.Char(
        compute='_compute_name',
        store=True,
        readonly=True,
    )

    patient_id = fields.Many2one(
        comodel_name='hr.hospital.patient',
        required=True,
        ondelete='cascade',
    )
    doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
        ondelete='set null',
    )
    disease_id = fields.Many2one(
        comodel_name='hr.hospital.disease',
        ondelete='set null',
    )

    visit_datetime = fields.Datetime(
        string='Visit Date',
        default=fields.Datetime.now,
        required=True,
    )

    state = fields.Selection(
        selection=[
            ('planned', 'Planned'),
            ('done', 'Done'),
            ('cancelled', 'Cancelled'),
        ],
        default='planned',
        required=True,
    )

    symptoms = fields.Text()
    diagnosis = fields.Text()
    note = fields.Text()

    @api.depends('patient_id', 'visit_datetime')
    def _compute_name(self):
        for rec in self:
            if rec.patient_id and rec.visit_datetime:
                rec.name = (
                    f"{rec.patient_id.name} - "
                    f"{fields.Datetime.to_string(rec.visit_datetime)}"
                )
            elif rec.patient_id:
                rec.name = rec.patient_id.name
            else:
                rec.name = 'Visit'

    @api.onchange('patient_id')
    def _onchange_patient_id(self):
        for rec in self:
            if rec.patient_id and not rec.doctor_id:
                rec.doctor_id = rec.patient_id.doctor_id
