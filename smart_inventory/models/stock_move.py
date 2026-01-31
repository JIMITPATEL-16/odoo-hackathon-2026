from odoo import models, fields, api
from datetime import date

class StockQuant(models.Model):
    _inherit = 'stock.quant'

    # 1. Define the fields
    days_since_last_move = fields.Integer(string="Days Idle", compute="_compute_stock_aging")
    stock_status = fields.Selection([
        ('fast', 'Fast Moving'),
        ('slow', 'Slow Moving'),
        ('dead', 'Dead Stock')
    ], string="Inventory Health", compute="_compute_stock_aging", store=True)

    # 2. The Logic (The "Brain" of your hackathon project)
    @api.depends('in_date', 'inventory_date')
    def _compute_stock_aging(self):
        today = date.today()
        for record in self:
            if record.in_date:
                # Calculate the difference in days
                delta = (today - record.in_date.date()).days
                record.days_since_last_move = delta
                
                # Logic for status
                if delta <= 15:
                    record.stock_status = 'fast'
                elif 15 < delta <= 45:
                    record.stock_status = 'slow'
                else:
                    record.stock_status = 'dead'
            else:
                record.days_since_last_move = 0
                record.stock_status = 'fast'