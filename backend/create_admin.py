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

# Supprimer tous les superusers existants
deleted = User.objects.filter(is_superuser=True).delete()
print(f"Superusers supprimes: {deleted}")

# Créer nouveau superuser
username = 'admin'
email = 'admin@fdkbois.com'
password = 'admin123'

user = User.objects.create_superuser(
    username=username,
    email=email,
    password=password
)
print(f"Superuser '{username}' cree avec succes!")
