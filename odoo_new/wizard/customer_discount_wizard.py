from odoo import api, fields, models, tools
import logging
from odoo.exceptions import ValidationError
import re

_logger = logging.getLogger(__name__)


class CustomerDiscountWizard(models.TransientModel):
    _name = "customer.discount.wizard"
    _description = "Wizard Customer VIP"

    customer_discount_code = fields.Char('Discount Code')
    code_valid = fields.Boolean('Sale code Valid', default=False)

    def multi_update_discount(self):
        ids = self.env.context['active_ids']
        customers = self.env['res.partner'].browse(ids)
        check = self.__check_discount_value(value=self.customer_discount_code)
        if self.customer_discount_code and check:
            new_data = {
                "customer_discount_code": self.customer_discount_code,
                "customer_check": check
            }
            customers.write(new_data)
        else:
            raise ValidationError("Vip format is not allowed, please re-enter ex: 'VIP_integer' ")


    @api.model
    def __check_discount_value(self, value):
        if len(value) < 5:
            return False
        else:
            first = value[0:4]
            last = value[4:]
            if first == "VIP_" and last.isdigit() and len(last) < 3:
                return True
            else:
                return False