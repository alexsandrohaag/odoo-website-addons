{
    'name': 'Product Multi-Image Carousel',
    'category': 'Website',
    'version': '10.0.0.1',
    'author': 'Luke Branch and Cristian Sebastian Rocha, extended by HGSOFT',
    'depends': ['product', 'sale', 'website_sale'],
    'data': [
        'views/product_images.xml',
        'views/website_product_image_carousel.xml',
        'views/theme.xml',
        'security/ir.model.access.csv',
    ],
    'application': True,
    'installable': False,
}
