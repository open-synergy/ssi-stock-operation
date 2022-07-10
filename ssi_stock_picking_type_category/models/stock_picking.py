# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).


from odoo import fields, models


class StockPicking(models.Model):
    _name = "stock.picking"
    _inherit = ["stock.picking"]

    picking_type_category_id = fields.Many2one(
        string="Picking Type Category",
        comodel_name="stock.picking_type_category",
        related="picking_type_id.category_id",
        store=True,
    )
