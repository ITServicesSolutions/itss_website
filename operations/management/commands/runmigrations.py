from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Exécute les migrations de la base de données'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Début de l\'exécution des migrations...'))
        try:
            call_command('migrate', interactive=False)
            self.stdout.write(self.style.SUCCESS('✅ Migrations exécutées avec succès !'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'❌ Erreur lors de l\'exécution des migrations: {str(e)}'))
            raise
