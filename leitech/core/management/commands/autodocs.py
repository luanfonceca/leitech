from django.core.management.base import BaseCommand
import os

class Command(BaseCommand):
    help = 'Create the autodocs using Epydoc.'

    def handle(self, *args, **options):
        os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
        has_errors = os.system('epydoc . -o ../docs/doc_code')
        if has_errors:
            raise CommandError(
                '\nDocumentation was not properly created.'
            )
        else:
            self.stdout.write(
                '\nDocumentation was successfully created.'
            )
