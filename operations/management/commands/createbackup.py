import os
import shutil
from datetime import datetime
from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Crée un backup du projet'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Début de la création du backup...'))
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_dir = os.path.join(settings.BASE_DIR.parent, f'backup_{timestamp}')
        
        try:
            # Créer le répertoire de backup
            os.makedirs(backup_dir, exist_ok=True)
            self.stdout.write(f'📁 Répertoire de backup créé: {backup_dir}')
            
            # Copier le projet
            self.stdout.write('📦 Copie du projet en cours...')
            shutil.copytree(
                settings.BASE_DIR,
                os.path.join(backup_dir, 'itss_website'),
                ignore=shutil.ignore_patterns(
                    '.git', '__pycache__', '*.pyc', '*.pyo',
                    'venv', 'env', '.venv', '.env',
                    'staticfiles', 'media', 'tmp', '*.log',
                    'node_modules'
                )
            )
            
            # Backup de la base de données si c'est SQLite
            if settings.DATABASES['default']['ENGINE'] == 'django.db.backends.sqlite3':
                db_path = settings.DATABASES['default']['NAME']
                if os.path.exists(db_path):
                    self.stdout.write('💾 Sauvegarde de la base de données SQLite...')
                    shutil.copy2(db_path, os.path.join(backup_dir, 'db.sqlite3'))
            
            self.stdout.write(self.style.SUCCESS(f'✅ Backup créé avec succès: {backup_dir}'))
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'❌ Erreur lors de la création du backup: {str(e)}'))
            raise
