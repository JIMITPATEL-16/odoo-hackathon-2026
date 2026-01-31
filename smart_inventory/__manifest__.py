{
    'name': 'Smart Inventory AI-Stock Sense',
    'version': '1.0',
    'category': 'Inventory',
    'summary': 'AI-driven stock aging and dead stock identification for Odoo',
    'description': """
        This module helps warehouse managers identify:
        - Dead stock (45+ days idle)
        - Slow moving items
        - Automatic stock status badges
    """,
    'author': 'Your Team Name',
    'depends': ['base', 'stock'],  # 'stock' is required to inherit inventory features
    'data': [
        'views/stock_quant_view.xml', # Ensure the path matches your XML file
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}