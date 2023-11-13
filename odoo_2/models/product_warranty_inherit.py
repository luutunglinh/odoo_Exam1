from odoo import api, fields, models
import datetime
from odoo.exceptions import ValidationError
import re

class ProductWarranty(models.Model):
    _inherit = 'product.template'

    product_warranty = fields.Char(string="Warranty Code", compute="_converting_time")
    date_from = fields.Date(string="Start", required = True)
    date_to = fields.Date(string="End", required=True)
    day_warranty = fields.Char(string="Day Warranty", compute="_count_day_warranty")
    check_warranty = fields.Boolean(string="Check Warranty")
    day_warranty_discount = fields.Integer("test")
    @api.constrains("date_to", "date_from")
    def _contrains_check_date(self):
        for record in self:
            if record.date_from > record.date_to:
                raise ValidationError("Date To need to be more than date Form")

    @api.depends("date_to","date_from", 'day_warranty', 'check_warranty')
    def _count_day_warranty(self):
        for record in self:
            record.day_warranty_discount = 0
            if record.date_to and record.date_to:
                rest_day = (record.date_to - datetime.date.today()).days
                if rest_day < 1:
                    record.day_warranty = "No Warranty"
                    record.check_warranty = False
                    record.day_warranty_discount = 10
                elif rest_day > 31:
                    record.day_warranty = "Warranty Time: " + str(rest_day // 31) + " Month"
                    record.check_warranty = True
                elif rest_day > 0:
                    record.day_warranty = "Warranty Time: " + str(rest_day) + "days"
                    record.check_warranty = True
                elif rest_day > 365:
                    record.day_warranty = "Warranty Time: " + str(rest_day // 365) + "years"
                    record.check_warranty = True
            else:
                record.check_warranty = False
                record.day_warranty_discount = 10
                record.day_warranty = "No Warranty"



    @api.onchange("date_to", 'date_form')
    def _converting_time(self):
        for record in self:
            if record.date_from and record.date_to:
                record.product_warranty = "PWR/"+(record.date_from).strftime("%m/%d/%Y")+"/"+(record.date_to).strftime("%m/%d/%Y")
            else:
                record.product_warranty= ''





