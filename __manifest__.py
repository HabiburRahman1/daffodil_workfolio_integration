# -*- coding: utf-8 -*-
{
    'name': 'Workfolio Integration',
    'summary': """Workfolio features and functionality integration.""",
    'description': """
Workfolio Integration
=====================
Workfolio features and functionality integration.
    """,
    'version': '13.0.1.0',
    'author': 'Md Habibur Rahman & Jeshad Khan',
    'company': 'Daffodil International University (DIU)',
    'website': 'http://pd.daffodilvarsity.edu.bd/',
    'category': 'Tools',
    'sequence': 1,
    'depends': [
        'base',
        'mail',
    ],
    'data': [
        ## Data
        'data/ir_sequence.xml',

        ## Security
        'security/security.xml',
        'security/ir.model.access.csv',

        ## View
        'views/wf_team.xml',
        'views/wf_timesheet.xml',
        'views/workfolio_api_setup_view.xml',
        'views/config_workfolio_view.xml',
        'views/menus.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'icon': "/daffodil_workfolio_integration/static/description/icon.png",
    "images": ["/static/description/banner.png"],
    "license": "OPL-1",
    "price": 0,
    "currency": "EUR",
}


