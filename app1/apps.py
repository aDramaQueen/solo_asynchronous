from django.apps import AppConfig

from solo_asynchronous.constants import management_is_in_process


class App1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app1'

    def ready(self):
        # ATTENTION: Leave the imports here!!!
        from app1.models import SiteConfiguration

        if not management_is_in_process():
            print('Try to get solo model...')
            model = SiteConfiguration.get_solo()
            print(f'Got it: {model}')
