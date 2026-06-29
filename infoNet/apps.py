from django.apps import AppConfig

class InfonetConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'infoNet'

    def ready(self):
        import infoNet.translation

# class InfonetConfig(AppConfig):
#     name = 'infoNet'
