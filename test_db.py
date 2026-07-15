import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'itss.settings')
django.setup()
from django.apps import apps

for model in apps.get_models():
    print(f"Testing model: {model.__name__}")
    try:
        list(model.objects.all()[:1])  # Récupère juste le premier objet
        print(f"✓ OK")
    except Exception as e:
        print(f"✗ ERROR: {type(e).__name__} - {e}")