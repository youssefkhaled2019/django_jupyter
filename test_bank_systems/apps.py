from django.apps import AppConfig


class TestBankSystemsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'test_bank_systems'
    def ready(self):  #<------ import
            import test_bank_systems.signals #<------import