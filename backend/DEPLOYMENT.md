# Guide de Déploiement - DKBOIS Backend sur Railway

Ce guide vous explique comment déployer le backend Django sur Railway.app avec PostgreSQL.

## Prérequis

- Compte GitHub (gratuit)
- Compte Railway.app (gratuit)
- Code source du projet pushé sur GitHub

## Étape 1 : Préparer le Projet

### 1.1 Vérifier les fichiers de configuration

Les fichiers suivants ont déjà été créés dans le dossier `backend/` :

- ✅ **Procfile** - Indique à Railway comment démarrer l'application
- ✅ **runtime.txt** - Spécifie la version Python (3.13.0)
- ✅ **requirements.txt** - Liste toutes les dépendances (incluant gunicorn, psycopg2-binary, etc.)
- ✅ **settings.py** - Configuré pour production avec variables d'environnement

### 1.2 Pousser le code sur GitHub

```bash
cd "c:\Users\Darius\Desktop\catalogue Menuserie"
git add .
git commit -m "Préparation pour déploiement Railway"
git push origin main
```

## Étape 2 : Créer un Compte Railway

1. Allez sur [railway.app](https://railway.app)
2. Cliquez sur **"Start a New Project"** ou **"Login"**
3. Connectez-vous avec votre compte GitHub
4. Autorisez Railway à accéder à vos repositories

## Étape 3 : Déployer le Backend Django

### 3.1 Créer un nouveau projet

1. Sur le dashboard Railway, cliquez sur **"New Project"**
2. Sélectionnez **"Deploy from GitHub repo"**
3. Choisissez votre repository **"catalogue Menuserie"** (ou le nom que vous avez donné)
4. Railway va détecter automatiquement que c'est un projet Python

### 3.2 Configurer le Root Directory

Railway doit savoir que le code Django est dans le dossier `backend/` :

1. Dans le projet Railway, cliquez sur votre service
2. Allez dans **Settings** (icône engrenage)
3. Trouvez **"Root Directory"**
4. Entrez : `backend`
5. Cliquez sur **"Save"**

### 3.3 Ajouter une Base de Données PostgreSQL

1. Dans votre projet Railway, cliquez sur **"+ New"**
2. Sélectionnez **"Database"**
3. Choisissez **"Add PostgreSQL"**
4. Railway va créer automatiquement la base de données
5. Railway va automatiquement créer la variable `DATABASE_URL` et la lier à votre service

## Étape 4 : Configurer les Variables d'Environnement

1. Cliquez sur votre service Django (pas la base de données)
2. Allez dans l'onglet **"Variables"**
3. Ajoutez les variables suivantes :

| Variable | Valeur | Description |
|----------|--------|-------------|
| `DEBUG` | `False` | Mode production (IMPORTANT) |
| `SECRET_KEY` | `[générer une clé aléatoire]` | Clé secrète Django |
| `ALLOWED_HOSTS` | `*` | Hôtes autorisés (ou domaine spécifique) |
| `CORS_ALLOWED_ORIGINS` | `https://votre-site.netlify.app` | URL frontend (à mettre à jour après déploiement Netlify) |
| `CSRF_TRUSTED_ORIGINS` | `https://votre-backend.up.railway.app` | URL backend Railway |

### Générer une SECRET_KEY sécurisée

Vous pouvez générer une clé aléatoire avec Python :

```python
import secrets
print(secrets.token_urlsafe(50))
```

Ou utilisez ce site : [Djecrety.ir](https://djecrety.ir/)

**Note :** La variable `DATABASE_URL` est automatiquement créée par Railway quand vous ajoutez PostgreSQL.

## Étape 5 : Déployer

1. Railway va automatiquement déployer votre application
2. Attendez que le build soit terminé (logs visibles dans l'onglet **"Deployments"**)
3. Une fois terminé, vous verrez **"Success"** en vert

## Étape 6 : Exécuter les Migrations

Après le premier déploiement, vous devez créer les tables dans PostgreSQL :

1. Dans votre service Railway, allez dans l'onglet **"Settings"**
2. Trouvez la section **"Deploy"**
3. Ajoutez dans **"Custom Start Command"** (si nécessaire) :
   ```
   python manage.py migrate && gunicorn dkbois_backend.wsgi --log-file -
   ```

   **OU** utilisez le **Railway CLI** (recommandé) :

   ```bash
   # Installer Railway CLI
   npm install -g @railway/cli

   # Se connecter
   railway login

   # Lier au projet
   railway link

   # Exécuter les migrations
   railway run python manage.py migrate

   # Créer un superuser (admin)
   railway run python manage.py createsuperuser

   # Collecter les fichiers statiques
   railway run python manage.py collectstatic --noinput
   ```

## Étape 7 : Obtenir l'URL de votre Backend

1. Dans Railway, cliquez sur votre service Django
2. Allez dans **"Settings"**
3. Trouvez la section **"Domains"**
4. Railway génère automatiquement une URL comme : `https://votre-projet.up.railway.app`
5. Vous pouvez aussi ajouter un **domaine personnalisé** si vous en avez un

## Étape 8 : Peupler la Base de Données (Optionnel)

Si vous voulez importer vos données initiales :

```bash
# Via Railway CLI
railway run python populate_data.py
```

**OU** via l'admin Django :
1. Créez un superuser avec `railway run python manage.py createsuperuser`
2. Accédez à `https://votre-projet.up.railway.app/admin/`
3. Ajoutez vos données manuellement

## Étape 9 : Tester l'API

Testez que votre API fonctionne :

```bash
# Remplacez par votre URL Railway
curl https://votre-projet.up.railway.app/api/projects/?lang=fr
```

Ou ouvrez dans le navigateur :
- API : `https://votre-projet.up.railway.app/api/`
- Admin : `https://votre-projet.up.railway.app/admin/`
- Dashboard : `https://votre-projet.up.railway.app/dashboard/`

## Étape 10 : Mettre à Jour le Frontend

Une fois le backend déployé, vous devez mettre à jour `api-config.js` dans votre frontend :

```javascript
// Fichier : api-config.js
const API_BASE_URL = 'https://votre-projet.up.railway.app/api';
```

## Prochaine Étape : Déployer le Frontend sur Netlify

Voir le guide [NETLIFY_DEPLOYMENT.md](../NETLIFY_DEPLOYMENT.md) pour déployer le frontend.

---

## Troubleshooting

### Problème : Build échoue avec "No module named 'dj_database_url'"

**Solution :** Vérifiez que `requirements.txt` contient toutes les dépendances :
```
gunicorn==21.2.0
dj-database-url==2.1.0
psycopg2-binary==2.9.9
whitenoise==6.6.0
```

### Problème : "DisallowedHost at /"

**Solution :** Ajoutez votre domaine Railway dans `ALLOWED_HOSTS` :
```
ALLOWED_HOSTS=votre-projet.up.railway.app,localhost
```

### Problème : Les images/fichiers statiques ne chargent pas

**Solution :** Exécutez :
```bash
railway run python manage.py collectstatic --noinput
```

### Problème : CORS errors depuis le frontend

**Solution :** Ajoutez l'URL de votre frontend Netlify dans `CORS_ALLOWED_ORIGINS` :
```
CORS_ALLOWED_ORIGINS=https://votre-site.netlify.app
```

### Problème : Base de données vide après déploiement

**Solution :** N'oubliez pas d'exécuter les migrations :
```bash
railway run python manage.py migrate
railway run python populate_data.py  # Si vous avez des données initiales
```

---

## Limites du Plan Gratuit Railway

- **500 heures par mois** d'exécution (environ 20 jours continus)
- **5$ de crédit gratuit** par mois
- **PostgreSQL inclus** gratuitement
- **500 MB de stockage** pour la base de données
- **100 GB de bande passante** par mois

**Astuce :** Si votre site a peu de trafic, 500h/mois est largement suffisant. Railway met automatiquement en veille les services inactifs pour économiser les heures.

---

## Commandes Utiles

```bash
# Voir les logs en temps réel
railway logs

# Ouvrir le service dans le navigateur
railway open

# Exécuter une commande Django
railway run python manage.py <commande>

# Accéder au shell Django
railway run python manage.py shell

# Créer une sauvegarde de la base de données
railway run python manage.py dumpdata > backup.json

# Restaurer une sauvegarde
railway run python manage.py loaddata backup.json
```

---

## Support

- **Documentation Railway :** https://docs.railway.app
- **Discord Railway :** https://discord.gg/railway
- **Documentation Django :** https://docs.djangoproject.com/

---

**Votre backend est maintenant déployé et prêt à servir votre frontend !** 🚀
