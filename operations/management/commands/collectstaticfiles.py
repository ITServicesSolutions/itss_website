from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Collecte les fichiers statiques'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Début de la collecte des fichiers statiques...'))
        try:
            call_command('collectstatic', interactive=False)
            self.stdout.write(self.style.SUCCESS('✅ Fichiers statiques collectés avec succès !'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'❌ Erreur lors de la collecte des fichiers statiques: {str(e)}'))
            raise
