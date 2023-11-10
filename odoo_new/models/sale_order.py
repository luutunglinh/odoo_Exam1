# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError
import json

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    partner_discount_code = fields.Char(related='partner_id.customer_discount_code', string="Discount Code", readonly=True)

    discount_vip = fields.Float(string="Discount %", related='partner_id.discount')

    amount_untaxed = fields.Monetary(string='Untaxed Amount', store=True, compute='_amount_all', tracking=5)

    amount_tax = fields.Monetary(string='Taxes', store=True, compute='_amount_all')

    amount_total = fields.Monetary(string='Total', store=True, compute='_amount_all', tracking=4)

    discount_price = fields.Monetary(string='Discount', store=True, compute='_amount_all', tracking=4)


    @api.depends('order_line.price_total','order_line','discount_vip')
    def _amount_all(self):
        """
        Compute the total amounts of the SO.
        """
        discount_price = 0
        for order in self:
            amount_untaxed = amount_tax = 0.0
            for line in order.order_line:
                discount_price += line.discount_code_vip
                amount_untaxed += line.price_subtotal
                amount_tax += line.price_tax
                print(discount_price)

            order.update({
                'amount_untaxed': amount_untaxed,
                'amount_tax': amount_tax,
                'discount_price': (amount_untaxed*(discount_price/100)),
                'amount_total': amount_untaxed + amount_tax - (amount_untaxed*(discount_price/100))
            })


class SaleOrderLineInherit(models.Model):
    _inherit = 'sale.order.line'

    discount_code_vip = fields.Float(related='order_id.discount_vip', readonly=True)

    @api.onchange('discount', 'order_id.discount_vip', 'product_id.discount_product')
    def change_discount_filed(self):
        for record in self:
            if record.order_id.discount_vip != 0.00:
                record.discount = record.order_id.discount_vip

    # @api.depends('product_uom_qty', 'discount', 'price_unit', 'tax_id')
    # def _compute_amount(self):
    #     """
    #     Compute the amounts of the SO line.
    #     """
    #     res = super(SaleOrderLineInherit, self)._compute_amount()
    #     for line in self:
    #         line.discount = line.order_id.discount_vip
    #         price = line.price_unit * (1 - (line.discount or 0.0) / 100.0)
    #         taxes = line.tax_id.compute_all(price, line.order_id.currency_id, line.product_uom_qty,
    #                                         product=line.product_id, partner=line.order_id.partner_shipping_id)
    #         line.update({
    #             'price_tax': sum(t.get('amount', 0.0) for t in taxes.get('taxes', [])),
    #             'price_total': taxes['total_included'],
    #             'price_subtotal': taxes['total_excluded'],
    #         })
    #         if self.env.context.get('import_file', False) and not self.env.user.user_has_groups(
    #                 'account.group_account_manager'):
    #             line.tax_id.invalidate_cache(['invoice_repartition_line_ids'], [line.tax_id.id])
    #     return res














