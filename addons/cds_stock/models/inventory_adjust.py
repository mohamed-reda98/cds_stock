# -*- coding: utf-8 -*-
from odoo import fields, models


class InventoryAdjust(models.Model):
    _inherit = 'stock.quant'

    inventory_qty = fields.Float(string="New Counted Quantity", help="The product's counted quantity.")
