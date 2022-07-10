# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).


from odoo import fields, models


class StockMoveLine(models.Model):
    _name = "stock.move.line"
    _inherit = ["stock.move.line"]

    picking_type_id = fields.Many2one(
        string="Operation",
        comodel_name="stock.picking.type",
        related="move_id.picking_type_id",
        store=True,
    )
    picking_type_category_id = fields.Many2one(
        string="Picking Type Category",
        comodel_name="stock.picking_type_category",
        related="move_id.picking_type_id.category_id",
        store=True,
    )
