# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    "name": "Stock Operation Picking Type Category",
    "version": "14.0.1.0.0",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "LGPL-3",
    "installable": True,
    "depends": [
        "stock",
        "ssi_master_data_mixin",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/stock_picking_type_category_data.xml",
        "views/stock_picking_type_category_views.xml",
        "views/stock_picking_type_views.xml",
    ],
}
