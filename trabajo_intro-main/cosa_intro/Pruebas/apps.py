from django.apps import AppConfig


class PruebasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Pruebas'

class pruebasConfig(AppConfig):
    name = 'pruebas'

    def ready(self):
    	import pruebas.signals
