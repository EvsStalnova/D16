from django.apps import AppConfig


class BulletinBoardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.bulletin_board'

    def ready(self):
        from . import signals
