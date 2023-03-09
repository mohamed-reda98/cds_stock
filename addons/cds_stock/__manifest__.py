# -*- coding: utf-8 -*-
{
    'name': "CDS Stock Module",
    'summary': """
    """,
    'description': """
    """,
    'author': "CDS Solutions SRL",
    'website': "www.cdsegypt.com",
    'contributors': [
        'Ramadan Khalil <rkhalil1990@gmail.com>',
    ],
    'version': '0.1',
    'depends': ['base', 'sale', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/inventory_adjust_inherit.xml',
    ],
    "pre_init_hook": None,
    "post_init_hook": None,
}
