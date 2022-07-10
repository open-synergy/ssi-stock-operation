# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).


from odoo import fields, models


class StockPickingType(models.Model):
    _name = "stock.picking.type"
    _inherit = ["stock.picking.type"]

    category_id = fields.Many2one(
        string="Category",
        comodel_name="stock.picking_type_category",
        ondelete="restrict",
    )
