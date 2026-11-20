from django.apps import AppConfig
import os
from dotenv import load_dotenv

class BackendConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backend'

    def ready(self):
        import backend.signals
        """
        импортируем сигналы
        
        """
load_dotenv()