# -*- coding: utf-8 -*-
{
    'name': "Daffodil Workfolio Integration",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Md Habibur Rahman",
    'website': "http://pd.daffodilvarsity.edu.bd/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'mail',
                ],

    # always loaded
    'data': [
        ## Security
        'security/ir.model.access.csv',
        'security/security.xml',

        ## Data
        'data/ir_sequence.xml',
        'data/ir_config_parameter_data.xml',

        ## View
        'views/wf_team.xml',
        'views/wf_timesheet.xml',
        'views/workfolio_api_setup_view.xml',
        'views/config_workfolio_view.xml',
        'views/menus.xml',
        'views/templates.xml',


    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
