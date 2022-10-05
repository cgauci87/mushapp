from django.apps import AppConfig

""" Auto-incrementing Primary Key """
class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'
