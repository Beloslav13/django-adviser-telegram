from django.apps import AppConfig


class TelegramConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'telegram'

    # def __init__(self, app_name, app_module):
    #     super().__init__(app_name, app_module)
