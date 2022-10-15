from django.apps import AppConfig

""" Auto-incrementing Primary Key """
class AdminAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'admin_app'
