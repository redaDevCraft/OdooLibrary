{
    'name': 'Library Management',
    'version': '1.0',
    'summary': 'Manage library authors, books, borrowers, and loans',
    'description': 'A module to manage a library with authors, books, borrowers, and loans.',
    'category': 'Library',
    'depends': ['base','website'],
    'data': [
    'security/library_security.xml',
    'security/ir.model.access.csv',
    'views/library_menu.xml',
    'views/author_views.xml',
    'views/book_views.xml',
    'views/borrower_views.xml',
    'views/loan_views.xml',
    'views/loan_line_views.xml',
    'views/empwizard_views.xml',
    'views/reset_empwizard-views.xml',
    'reports/authors_report/author_report.xml',
    'reports/authors_report/author_template.xml',
    'reports/borrowers_report/borrower_template.xml',
    'reports/borrowers_report/borrower_report.xml' ,
     'reports/loans_report/loan_template.xml',
    'reports/loans_report/loan_report.xml' ,
    
   
   
    

    ],

    'installable': True,
    'application': True,
}
