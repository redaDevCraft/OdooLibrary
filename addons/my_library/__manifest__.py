{
    'name': 'Library Management',
    'version': '1.0',
    'summary': 'Manage library authors, books, borrowers, and loans',
    'description': 'A module to manage a library with authors, books, borrowers, and loans.',
    'category': 'Library',
    'depends': ['base'],
    'data': [
    'security/ir.model.access.csv',
    'views/library_menu.xml',
    'views/author_views.xml',
    'views/book_views.xml',
    'views/borrower_views.xml',
    'views/loan_views.xml',
    'views/loan_line_views.xml',
],

    'installable': True,
    'application': True,
}
