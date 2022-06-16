{
    
'name': 'Library Website',
'description': 'Create and check book checkout requests.',
'author': 'Whizzy Eric',
'depends': [
    'library_checkout',
    'website',
    ],

'data': [
    'security/ir.model.access.csv',
    'security/library_security.xml',
    'views/library_member.xml',
    'views/helloworld_template.xml',
    'website_assets.xml',
    'views/checkout_template.xml',
    'views/book_list_template.xml',
   ],

# 'installable':True  

}
  
