{
    'name': 'My Custom Module',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'views/my_model_views.xml',  
    ],
    'installable': True,  # Ensure this is set to True
    'application': True,  # Optional, makes it show in the Apps list
}
