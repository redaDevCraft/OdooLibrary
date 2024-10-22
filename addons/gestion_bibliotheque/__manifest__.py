{
    'name': 'Gestion Bibliotheque',
    'version': '1.0',
    'summary': 'Library Management System for Books and Borrowing Records',
    'description': """
        A module to manage books, members, and borrowing records in a library system.
        This includes managing the borrowing start and end dates, with nationality defaulted to Algerian.
    """,
    'author': 'Your Name',
    'website': 'http://yourwebsite.com',
    'category': 'Library Management',
    'depends': ['base'],
    'data': [
        'views/library_menu.xml',
        'security/ir.model.access.csv',
        'views/book_views.xml',
        'views/member_views.xml',
        'views/borrow_record_views.xml',
        'views/author_views.xml',
          

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
