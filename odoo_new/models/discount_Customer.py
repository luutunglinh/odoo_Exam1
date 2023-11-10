# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError
import re

class discountCustommer(models.Model):
    _inherit = 'res.partner'

    customer_discount_code = fields.Char(string='Customer Discount Code')
    discount = fields.Float(string="Discount %", compute="compute_discount")
    customer_check = fields.Boolean()

    # @api.constrains('customer_discount_code')
    # def _check_code(self):
    #     for record in self:
    #         if record.customer_discount_code and not re.match(r'^VIP_\d+$', record.customer_discount_code):
    #             raise ValidationError("Mã VIP phải có định dạng 'VIP_' theo sau là số nguyên.")

    @api.onchange('customer_discount_code','discount','customer_check')
    def compute_discount(self):
        for record in self:
            if record.customer_discount_code:
                first = record.customer_discount_code[:4]
                last = record.customer_discount_code[4:]
                if first == 'VIP_' and last.isdigit():
                    record.discount = float(last)
                    record.customer_check = True
                else:
                    record.discount = 0.00
                    record.customer_check = False
            else:
                record.discount = 0.00
                record.customer_check = False






