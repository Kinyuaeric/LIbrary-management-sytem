{
'name': 'Library Management System',
'description': 'Manage library book catalogue and lending',
'author': 'Eric Kinyua',
'category': 'extra tools',
'depends': ['base'],
'application': True,
'installable': True,   
'data': [
  'security/library_security.xml',
  'security/ir.model.access.csv',
  'views/library_menu.xml', 
  'views/book_view.xml', 
  'views/book_list_template.xml',
  'reports/library_book_report.xml',
  'reports/library_book_sql_report.xml',

  ]
}