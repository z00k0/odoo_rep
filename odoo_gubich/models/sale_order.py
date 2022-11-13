from odoo import api, fields, models, _
import random
import json

from odoo.exceptions import ValidationError


class TestField(models.Model):
    _inherit = "sale.order"

    def _get_random_number(self):
        return random.randint(0, 99)

    test_field = fields.Char(string="Test", default=_get_random_number, readonly=False, states={'draft': [('readonly', False)], 'sent': [('readonly', True)], 'sale': [('readonly', True)]})

    @api.onchange('date_order', 'tax_totals_json')
    def _compute_test_field(self):
        for record in self:
            if record.test_field:
                quot_date = record.date_order.strftime("%d/%m/%Y, %H:%M:%S")
                amount_total_json = json.loads(record.tax_totals_json)
                amount_total = amount_total_json.get("formatted_amount_total")
                record.test_field = f"{amount_total} - {quot_date}"

    @api.constrains("test_field")
    def calc_length(self):
        for record in self:
            print(f"on_change: {record.test_field=}")
            if record.test_field and len(record.test_field) > 50:
                raise ValidationError(_("Длина текста должна быть меньше 50 символов!"))


