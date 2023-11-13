from odoo import api, models, fields


class SaleOrderWarranty(models.Model):
    _inherit = "sale.order"

    amount_untaxed = fields.Monetary(string='Untaxed Amount', store=True, compute='_amount_all', tracking=5)

    amount_tax = fields.Monetary(string='Taxes', store=True, compute='_amount_all')

    amount_total = fields.Monetary(string='Total', store=True, compute='_amount_all', tracking=4)

    discount_price = fields.Monetary(string='Discount', store=True, compute='_amount_all', tracking=4)

    @api.depends('order_line.price_total', 'order_line')
    def _amount_all(self):
        """
        Compute the total amounts of the SO.
        """
        discount_price = 0
        for order in self:
            amount_untaxed = amount_tax = 0.0
            for line in order.order_line:
                discount_price += line.show_discount_estimated
                amount_untaxed += line.price_subtotal
                amount_tax += line.price_tax
            order.update({
                'amount_untaxed': amount_untaxed,
                'amount_tax': amount_tax,
                'discount_price': discount_price,
                'amount_total': amount_untaxed + amount_tax - discount_price
            })


class SaleOrderLineWarranty(models.Model):
    _inherit = 'sale.order.line'

    show_discount_estimated = fields.Monetary(string="Discount Estimated", default=0 ,compute="_compute_discount_estimated")

    # total_discount_estimated = fields.Monetary(string="Total Discount", default=0)

    day_warranty = fields.Char(string="Number day warranty", related = "product_template_id.day_warranty")

    discount_warranty = fields.Integer(related= "product_template_id.day_warranty_discount")

    @api.onchange('product_uom_qty', 'price_tax', 'price_unit')
    def _compute_discount_estimated(self):
        for record in self:
            record.show_discount_estimated = (record.price_unit * record.product_uom_qty) * (record.discount_warranty / 100.0)

