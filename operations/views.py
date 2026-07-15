import os
import shutil
import io
from datetime import datetime
from django.conf import settings
from django.core.management import call_command
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
import logging

logger = logging.getLogger(__name__)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def run_migrations(request):
    """
    Exécute les migrations Django.
    Seulement accessible par les administrateurs.
    """
    try:
        logger.info("Début de l'exécution des migrations")
        out = io.StringIO()
        
        call_command('runmigrations', stdout=out, stderr=out)
        
        output = out.getvalue()
        logger.info("Migrations exécutées avec succès")
        return Response({
            'success': True,
            'message': 'Migrations exécutées avec succès',
            'output': output
        })
    except Exception as e:
        logger.error(f"Exception lors de l'exécution des migrations: {str(e)}")
        return Response({
            'success': False,
            'message': f'Erreur: {str(e)}'
        }, status=500)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def collect_static(request):
    """
    Collecte les fichiers statiques.
    Seulement accessible par les administrateurs.
    """
    try:
        logger.info("Début de la collecte des fichiers statiques")
        out = io.StringIO()
        
        call_command('collectstaticfiles', stdout=out, stderr=out)
        
        output = out.getvalue()
        logger.info("Fichiers statiques collectés avec succès")
        return Response({
            'success': True,
            'message': 'Fichiers statiques collectés avec succès',
            'output': output
        })
    except Exception as e:
        logger.error(f"Exception lors de la collecte des fichiers statiques: {str(e)}")
        return Response({
            'success': False,
            'message': f'Erreur: {str(e)}'
        }, status=500)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_backup(request):
    """
    Crée un backup du projet.
    Seulement accessible par les administrateurs.
    """
    try:
        logger.info("Début de la création du backup")
        out = io.StringIO()
        
        call_command('createbackup', stdout=out, stderr=out)
        
        output = out.getvalue()
        logger.info("Backup créé avec succès")
        return Response({
            'success': True,
            'message': 'Backup créé avec succès',
            'output': output
        })
    except Exception as e:
        logger.error(f"Exception lors de la création du backup: {str(e)}")
        return Response({
            'success': False,
            'message': f'Erreur: {str(e)}'
        }, status=500)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_operations_status(request):
    """
    Retourne la liste des endpoints disponibles.
    Seulement accessible par les administrateurs.
    """
    return Response({
        'operations': [
            'POST /api/operations/run-migrations/',
            'POST /api/operations/collect-static/',
            'POST /api/operations/create-backup/'
        ],
        'description': 'Endpoints pour les opérations de déploiement. Nécessite une authentification administrateur.'
    })
