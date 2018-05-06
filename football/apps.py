from django.apps import AppConfig


class FootballConfig(AppConfig):
    name = 'football'
    verbose_name = 'Football Application'

    def ready(self):
        import football.signals