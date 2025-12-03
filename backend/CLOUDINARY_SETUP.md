# Configuration Cloudinary pour DKBOIS

Ce guide vous explique comment configurer Cloudinary pour le stockage des images du site DKBOIS.

## 1. Créer un compte Cloudinary GRATUIT

1. Allez sur [https://cloudinary.com/users/register_free](https://cloudinary.com/users/register_free)
2. Inscrivez-vous avec votre email
3. Vérifiez votre email et activez le compte

## 2. Récupérer vos identifiants

Une fois connecté à votre dashboard Cloudinary :

1. Allez dans **Dashboard** (page d'accueil)
2. Vous verrez une section **Account Details** avec :
   - **Cloud Name** : `dxxxxx` (votre nom de cloud)
   - **API Key** : `123456789012345` (votre clé API)
   - **API Secret** : `aBcDeFgHiJkLmNoPqRsTuVwXyZ` (votre secret API)

⚠️ **Ne partagez JAMAIS votre API Secret publiquement !**

## 3. Configurer sur Railway (Production)

1. Allez dans votre projet Railway : [https://railway.app](https://railway.app)
2. Sélectionnez votre service backend
3. Allez dans l'onglet **Variables**
4. Ajoutez ces 3 variables d'environnement :

```
CLOUDINARY_CLOUD_NAME=votre_cloud_name
CLOUDINARY_API_KEY=votre_api_key
CLOUDINARY_API_SECRET=votre_api_secret
```

5. Railway redéploiera automatiquement

## 4. Configurer en local (Développement)

### Option A : Fichier .env (Recommandé)

1. Créez un fichier `.env` dans le dossier `backend/` :

```bash
# Cloudinary Configuration
CLOUDINARY_CLOUD_NAME=votre_cloud_name
CLOUDINARY_API_KEY=votre_api_key
CLOUDINARY_API_SECRET=votre_api_secret
```

2. Le fichier `.env` est déjà dans `.gitignore`, vos secrets sont protégés

### Option B : Variables d'environnement Windows

Ouvrez PowerShell et exécutez :

```powershell
$env:CLOUDINARY_CLOUD_NAME="votre_cloud_name"
$env:CLOUDINARY_API_KEY="votre_api_key"
$env:CLOUDINARY_API_SECRET="votre_api_secret"
```

⚠️ Ces variables disparaissent quand vous fermez PowerShell

## 5. Tester la configuration

### Test local :

```bash
cd backend
python manage.py shell
```

Dans le shell Python :

```python
from django.core.files.storage import default_storage
print(default_storage.__class__.__name__)
# Devrait afficher: MediaCloudinaryStorage

# Test d'upload
from django.core.files.base import ContentFile
test_file = ContentFile(b"test content", name="test.txt")
path = default_storage.save('test_upload.txt', test_file)
print(f"Fichier uploadé à: {path}")
```

### Vérifier sur Cloudinary :

1. Allez sur [https://cloudinary.com/console/media_library](https://cloudinary.com/console/media_library)
2. Vous devriez voir vos fichiers uploadés

## 6. Limites du plan gratuit

✅ **Plan gratuit Cloudinary inclut :**
- 25 GB de stockage
- 25 GB de bande passante par mois
- Transformations d'images illimitées
- CDN global
- HTTPS sécurisé
- Largement suffisant pour DKBOIS !

## 7. Utilisation dans l'admin Django

Une fois configuré, l'upload d'images dans l'admin Django se fera automatiquement sur Cloudinary :

1. Allez sur http://localhost:3000/admin/ (local) ou votre URL Railway (prod)
2. Créez ou éditez un projet/service
3. Uploadez une image
4. L'image sera automatiquement stockée sur Cloudinary
5. L'URL sera du type : `https://res.cloudinary.com/votre-cloud/image/upload/...`

## 8. Migration des images existantes (optionnel)

Si vous avez déjà des images en local à migrer :

```bash
cd backend
python manage.py shell
```

```python
from portfolio.models import Project, Service
import cloudinary.uploader

# Exemple pour migrer les images des projets
for project in Project.objects.all():
    if project.image and hasattr(project.image, 'path'):
        # Upload to Cloudinary
        result = cloudinary.uploader.upload(project.image.path)
        project.image = result['url']
        project.save()
        print(f"Migrated: {project.title}")
```

## Troubleshooting

### Erreur : "Must supply cloud_name"
- Vérifiez que les variables d'environnement sont bien définies
- Redémarrez le serveur Django après avoir ajouté les variables

### Erreur : "Invalid credentials"
- Vérifiez que vous avez copié correctement API_KEY et API_SECRET
- Attention aux espaces en début/fin de ligne

### Les images ne s'affichent pas
- Vérifiez les URLs retournées par l'API
- Assurez-vous que CORS est configuré sur Cloudinary (normalement activé par défaut)

## Support

- Documentation Cloudinary Django : [https://cloudinary.com/documentation/django_integration](https://cloudinary.com/documentation/django_integration)
- Support Cloudinary : [https://support.cloudinary.com](https://support.cloudinary.com)
