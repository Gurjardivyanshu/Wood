from odoo import api, fields, models
from datetime import datetime

class Wood(models.Model):
    _name = "wood"

    date = fields.Datetime("Date")
    so_no = fields.Integer("So. No.")
    buyer = fields.Char("Buyers order no.")
    contracter = fields.Char("Contractor")
    product = fields.Char("Product")
    state = fields.Char("State")
    image = fields.Binary("Image")
    stock_qty = fields.Float("Stock Qty")
    qty = fields.Float("Qty")
    wood_ids = fields.One2many("requisition.lines", "wood_id", string="Requisition01")


class RequisitionLines(models.Model):
    _name = "requisition.lines"
    # product = fields.Char("Product")
    product_id = fields.Many2one("product.product","Product")
    # uom = fields.Many2one("wood")
    warehouse_id = fields.Many2one("stock.warehouse","Warehouse")
    wood_id = fields.Many2one("wood", string="Wood")
