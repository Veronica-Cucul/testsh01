from odoo import api, fields, models, _


class ResPartner(models.Model):
    _inherit = "res.partner"

    note = fields.Char(string="Note")