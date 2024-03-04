# wasserman_core/apps.py
from django.apps import AppConfig

class WassermanCoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'wasserman_core'

    def ready(self):
        import wasserman_core.signals  # Importez les signaux ici