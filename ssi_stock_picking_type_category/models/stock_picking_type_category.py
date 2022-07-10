# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).


from odoo import fields, models


class StockPickingTypeCategory(models.Model):
    _name = "stock.picking_type_category"
    _inherit = ["mixin.master_data"]
    _description = "Picking Type Category"

    name = fields.Char(
        string="Picking Type Category",
    )
