# Guide de déploiement avec endpoints API et management commands

## Ce qui a été créé

### 1. Custom Management Commands
Des commandes Django personnalisées, utilisables via `manage.py` :
- `python manage.py runmigrations` - Exécute les migrations
- `python manage.py collectstaticfiles` - Collecte les fichiers statiques
- `python manage.py createbackup` - Crée un backup du projet

### 2. Endpoints API sécurisés
Une app `operations` avec les endpoints suivants :
- `GET /api/operations/` - Statut et description des endpoints
- `POST /api/operations/run-migrations/` - Exécute les migrations (via management command)
- `POST /api/operations/collect-static/` - Collecte les fichiers statiques (via management command)
- `POST /api/operations/create-backup/` - Crée un backup du projet (via management command)

### 🔒 Sécurité
Tous les endpoints nécessitent :
- Une authentification JWT avec un compte **administrateur**
- Le header `Authorization: Bearer <votre-token>`

## Configuration du workflow GitHub

### Étape 1: Obtenir un token JWT
1. Connectez-vous avec un compte administrateur
2. Obtenez un token JWT via l'API d'authentification
3. Gardez ce token précieusement

### Étape 2: Ajouter le secret à GitHub
1. Allez dans votre dépôt → Settings → Secrets and Variables → Actions
2. Ajoutez un nouveau secret nommé `DEPLOYMENT_API_TOKEN`
3. Collez votre token JWT comme valeur

### Étape 3: Utilisation automatique
Le workflow GitHub appellera automatiquement ces endpoints après le déploiement FTP.

## Utilisation manuelle (si nécessaire)

### Via les endpoints API :
```bash
# Exécuter les migrations
curl -X POST https://it-servicegroup.com/api/operations/run-migrations/ \
  -H "Authorization: Bearer VOTRE_TOKEN" \
  -H "Content-Type: application/json"

# Collecter les fichiers statiques
curl -X POST https://it-servicegroup.com/api/operations/collect-static/ \
  -H "Authorization: Bearer VOTRE_TOKEN" \
  -H "Content-Type: application/json"

# Créer un backup
curl -X POST https://it-servicegroup.com/api/operations/create-backup/ \
  -H "Authorization: Bearer VOTRE_TOKEN" \
  -H "Content-Type: application/json"
```

### Via manage.py (si vous avez accès SSH) :
```bash
python manage.py runmigrations
python manage.py collectstaticfiles
python manage.py createbackup
```

## Structure des fichiers créés

```
itss_website/
├── operations/
│   ├── __init__.py
│   ├── apps.py
│   ├── urls.py
│   ├── views.py
│   └── management/
│       ├── __init__.py
│       └── commands/
│           ├── __init__.py
│           ├── runmigrations.py
│           ├── collectstaticfiles.py
│           └── createbackup.py
└── DEPLOYMENT.md  # Ce fichier
```

## Pourquoi cette architecture ?

1. **Management commands** : Code propre, réutilisable, testable, Django-style
2. **Endpoints API** : Permet d'exécuter les commandes sans accès SSH
3. **Sécurité** : Seulement les admins peuvent exécuter ces opérations

