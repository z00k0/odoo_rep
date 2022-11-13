# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Odoo Gubich',
    'version': '15.0.0.0.1',
    'category': 'Tools',
    'author': 'Denis Gubich',
    'summary': 'Odoo testcase',
    'description': """
Odoo Gubich testcase
    """,
    'depends': ['sale'],
    'data': [
        'views/sale_order_view.xml',
        'reports/sale_report_inherit.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'assets': {},
    'license': 'AGPL-3',
}
