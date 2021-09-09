from django.apps import AppConfig


class TwitConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'twit'

    def ready(self):
        import twit.signals
