#!/bin/bash
# Script de démarrage Railway avec migrations automatiques

echo "🚀 Starting Django application..."

# Exécuter les migrations
echo "📦 Running migrations..."
python manage.py migrate --noinput

# Collecter les fichiers statiques
echo "📂 Collecting static files..."
python manage.py collectstatic --noinput

# Créer le superuser admin automatiquement
echo "👤 Creating admin user..."
python create_admin.py

# Démarrer gunicorn
echo "✅ Starting gunicorn..."
gunicorn dkbois_backend.wsgi --log-file -
