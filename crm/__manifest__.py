# -*- coding: utf-8 -*-
{
    'name': "crm",

    'summary': """
         Module to create a contact""",

    'description': """
        Module to create a contact from the tab of a crm initiative from a button
    """,

    'author': "Xmarts",
    'Collaborators': 'Gilberto Santiago Acevedo',
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','crm'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}