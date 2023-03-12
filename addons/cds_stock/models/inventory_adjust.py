# -*- coding: utf-8 -*-
from odoo import fields, models, api


class InventoryAdjust(models.Model):
    _inherit = 'stock.quant'

    # inventory_quantity = fields.Float(help="The product's counted quantity.")
