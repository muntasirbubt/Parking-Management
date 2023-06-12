# -*- coding: utf-8 -*-
{
    'name': 'Parking Management System',
    'version': '1.0.0',
    'category': 'Parking',
    'author': 'Muntasir',

    'sequence': -33,
    'summary': 'Parking Management System',
    'description': """ Parking Management System of a company""",
    'depends': ['base', 'web'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/sequence_data.xml',

        'wizard/all_inout_report_view.xml',
        'wizard/wizard_inout_view.xml',
        'views/employee_reg_view.xml',
        'views/in_out_view.xml',
        'report/report.xml',
        'report/all_record.xml',
        'report/registration_card_report.xml',
        'report/in_out_report.xml',
        'views/menu.xml',



    ],
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'assets': {
        'web.assets_backend': [
            'parking_24/static/src/js/parking_kiosk.js',
            'parking_24/static/src/scss/parking_style.scss',
        ],
        'web.assets_qweb': [
            'parking_24/static/src/xml/**/*',
        ],

    },
}
