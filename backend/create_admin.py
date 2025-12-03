#!/usr/bin/env python
"""
Script pour créer automatiquement un superuser Django
Exécuté automatiquement au déploiement Railway
"""
import os
import django

# Utiliser DATABASE_PUBLIC_URL si disponible (pour railway run en local)
# Sinon DATABASE_URL (normal en production Railway)
if 'DATABASE_PUBLIC_URL' in os.environ and 'DATABASE_URL' in os.environ:
    # On est en railway run local, utiliser l'URL publique
    os.environ['DATABASE_URL'] = os.environ['DATABASE_PUBLIC_URL']

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dkbois_backend.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Informations du superuser (à configurer via variables d'environnement)
username = os.environ.get('ADMIN_USERNAME', 'admin')
email = os.environ.get('ADMIN_EMAIL', 'admin@dkbois.com')
password = os.environ.get('ADMIN_PASSWORD', 'admin123456')  # Changez en production !

# Créer le superuser seulement s'il n'existe pas
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(
        username=username,
        email=email,
        password=password
    )
    print(f"✅ Superuser '{username}' créé avec succès !")
else:
    print(f"ℹ️  Superuser '{username}' existe déjà.")
