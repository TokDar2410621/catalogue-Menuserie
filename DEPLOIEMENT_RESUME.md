# 🚀 Récapitulatif - Préparation au Déploiement DKBOIS

Votre site a été préparé pour le déploiement sur **Railway.app (backend)** et **Netlify (frontend)**.

## ✅ Ce qui a été fait

### 1. Configuration Backend Django

Les fichiers suivants ont été créés/modifiés dans `backend/` :

#### Fichiers de Configuration Railway

- **`Procfile`** ✅
  - Indique à Railway comment démarrer l'application
  - Utilise `gunicorn` comme serveur WSGI

- **`runtime.txt`** ✅
  - Spécifie Python 3.13.0

- **`requirements.txt`** ✅
  - Ajout des dépendances de production :
    - `gunicorn==21.2.0` - Serveur WSGI pour production
    - `dj-database-url==2.1.0` - Configuration PostgreSQL
    - `psycopg2-binary==2.9.9` - Driver PostgreSQL
    - `whitenoise==6.6.0` - Gestion des fichiers statiques

#### Configuration Django (`settings.py`) ✅

Les modifications suivantes ont été appliquées :

1. **Variables d'environnement**
   - `SECRET_KEY` - Lecture depuis variable d'environnement
   - `DEBUG` - Contrôlé par variable d'environnement (False en production)
   - `ALLOWED_HOSTS` - Configurable via variable d'environnement

2. **Base de données**
   - Configuration automatique PostgreSQL via `DATABASE_URL`
   - Fallback sur SQLite en développement local

3. **Fichiers statiques**
   - `STATIC_ROOT` configuré pour WhiteNoise
   - `WhiteNoiseMiddleware` ajouté au middleware
   - Compression et cache automatiques

4. **CORS**
   - Configurable via variable d'environnement `CORS_ALLOWED_ORIGINS`
   - Activé uniquement en mode DEBUG en développement

5. **CSRF**
   - Configurable via variable d'environnement `CSRF_TRUSTED_ORIGINS`

### 2. Documentation

- **`backend/DEPLOYMENT.md`** ✅ - Guide complet de déploiement Railway (en français)
- **`NETLIFY_DEPLOYMENT.md`** ✅ - Guide complet de déploiement Netlify (en français)
- **`backend/.env.example`** ✅ - Exemple de variables d'environnement
- **`_redirects`** ✅ - Configuration Netlify pour les redirections

---

## 📋 Prochaines Étapes - À Faire

### Étape 1 : Pousser le Code sur GitHub

```bash
cd "c:\Users\Darius\Desktop\catalogue Menuserie"
git add .
git commit -m "Préparation pour déploiement production (Railway + Netlify)"
git push origin main
```

### Étape 2 : Déployer le Backend sur Railway

**Temps estimé : 10-15 minutes**

1. Créer un compte sur [railway.app](https://railway.app)
2. Se connecter avec GitHub
3. Créer un nouveau projet depuis votre repository
4. Configurer le **Root Directory** : `backend`
5. Ajouter une base de données **PostgreSQL**
6. Configurer les variables d'environnement (voir guide détaillé)
7. Déployer et attendre le build
8. Exécuter les migrations
9. Créer un superuser
10. Noter l'URL Railway (ex: `https://dkbois-backend.up.railway.app`)

**📖 Guide détaillé :** [backend/DEPLOYMENT.md](backend/DEPLOYMENT.md)

### Étape 3 : Mettre à Jour l'URL de l'API

**IMPORTANT :** Avant de déployer le frontend, vous devez modifier `api-config.js` :

```javascript
// Fichier : api-config.js
// Ligne 5

// Remplacer :
const API_BASE_URL = 'http://localhost:3000/api';

// Par (avec votre URL Railway réelle) :
const API_BASE_URL = 'https://votre-projet.up.railway.app/api';
```

**Ensuite, commit et push :**

```bash
git add api-config.js
git commit -m "Configuration API pour production Railway"
git push origin main
```

### Étape 4 : Déployer le Frontend sur Netlify

**Temps estimé : 5-10 minutes**

1. Créer un compte sur [netlify.com](https://www.netlify.com)
2. Se connecter avec GitHub
3. Importer le repository depuis GitHub
4. Configurer le déploiement (pas de build nécessaire)
5. Déployer
6. Personnaliser le nom du site (ex: `dkbois`)
7. Noter l'URL Netlify (ex: `https://dkbois.netlify.app`)

**📖 Guide détaillé :** [NETLIFY_DEPLOYMENT.md](NETLIFY_DEPLOYMENT.md)

### Étape 5 : Configurer CORS sur Railway

**IMPORTANT :** Une fois Netlify déployé, retournez sur Railway et ajoutez/modifiez ces variables :

| Variable | Valeur |
|----------|--------|
| `CORS_ALLOWED_ORIGINS` | `https://dkbois.netlify.app` (votre URL Netlify) |
| `CSRF_TRUSTED_ORIGINS` | `https://votre-backend.up.railway.app,https://dkbois.netlify.app` |

Railway va redéployer automatiquement.

### Étape 6 : Tester le Site en Production

1. Ouvrir `https://dkbois.netlify.app` dans le navigateur
2. Vérifier que :
   - ✅ La page charge sans erreur
   - ✅ Les données de l'API s'affichent (services, projets)
   - ✅ Pas d'erreurs CORS dans la console (F12)
   - ✅ Le changement de langue fonctionne
   - ✅ Toutes les pages fonctionnent (portfolio, about, services, contact)

---

## 🛠️ Variables d'Environnement Railway

Voici les variables à configurer dans Railway :

```env
# OBLIGATOIRE
SECRET_KEY=<générer une clé aléatoire avec : python -c "import secrets; print(secrets.token_urlsafe(50))">
DEBUG=False
DATABASE_URL=<automatiquement fourni par Railway>

# RECOMMANDÉ
ALLOWED_HOSTS=*
CORS_ALLOWED_ORIGINS=https://dkbois.netlify.app
CSRF_TRUSTED_ORIGINS=https://votre-backend.up.railway.app,https://dkbois.netlify.app
```

**Note :** `DATABASE_URL` est automatiquement créée par Railway quand vous ajoutez PostgreSQL.

---

## 📊 Coûts Estimés

### Railway (Backend)
- **Plan gratuit :** 500 heures/mois + 5$ de crédit gratuit
- **PostgreSQL :** Inclus gratuitement
- **Pour DKBOIS :** 100% gratuit si trafic modéré

### Netlify (Frontend)
- **Plan gratuit :** Illimité pour les sites statiques
- **Bande passante :** 100 GB/mois gratuit
- **Pour DKBOIS :** 100% gratuit

**Total mensuel :** 0€ avec les plans gratuits 🎉

---

## 🔍 Vérification après Déploiement

### Checklist Finale

- [ ] Backend Railway déployé et accessible
- [ ] PostgreSQL configuré sur Railway
- [ ] Migrations exécutées (`railway run python manage.py migrate`)
- [ ] Superuser créé (`railway run python manage.py createsuperuser`)
- [ ] `api-config.js` modifié avec l'URL Railway
- [ ] Frontend Netlify déployé et accessible
- [ ] Variables CORS/CSRF configurées sur Railway
- [ ] Aucune erreur CORS dans la console du navigateur
- [ ] Toutes les pages fonctionnent (index, portfolio, services, about, contact)
- [ ] Changement de langue (FR/EN) fonctionne
- [ ] Formulaire de contact envoie bien les données
- [ ] Admin Django accessible (`https://votre-backend.up.railway.app/admin/`)
- [ ] SSL/HTTPS activé (cadenas vert)

### URLs Importantes à Noter

Une fois déployé, notez ces URLs :

- **Site public :** https://dkbois.netlify.app
- **Backend API :** https://votre-projet.up.railway.app/api/
- **Admin Django :** https://votre-projet.up.railway.app/admin/
- **Dashboard :** https://votre-projet.up.railway.app/dashboard/

---

## 🆘 Problèmes Courants

### Erreur CORS

**Symptôme :** Erreur dans la console : "blocked by CORS policy"

**Solution :**
1. Vérifiez `CORS_ALLOWED_ORIGINS` dans Railway
2. Pas d'espaces, format : `https://site1.com,https://site2.com`
3. Redémarrez le service Railway

### Base de données vide

**Symptôme :** Aucune donnée sur le site

**Solution :**
```bash
railway run python manage.py migrate
railway run python populate_data.py
```

### Images manquantes

**Symptôme :** Images ne chargent pas

**Solution :**
```bash
railway run python manage.py collectstatic --noinput
```

### Page blanche Netlify

**Symptôme :** Page blanche ou erreur 404

**Solution :**
1. Vérifiez que `_redirects` existe
2. Vérifiez la console (F12) pour les erreurs
3. Vérifiez que `api-config.js` a la bonne URL

---

## 📞 Support

### Documentation
- **Railway :** https://docs.railway.app
- **Netlify :** https://docs.netlify.com
- **Django :** https://docs.djangoproject.com

### Guides dans ce Projet
- **Backend Railway :** [backend/DEPLOYMENT.md](backend/DEPLOYMENT.md)
- **Frontend Netlify :** [NETLIFY_DEPLOYMENT.md](NETLIFY_DEPLOYMENT.md)
- **Variables d'environnement :** [backend/.env.example](backend/.env.example)

---

## 🎯 Résumé en 3 Étapes

1. **Push sur GitHub** → Code prêt
2. **Railway** → Backend + PostgreSQL + Variables d'environnement
3. **Netlify** → Frontend + Mise à jour CORS

**Temps total estimé : 30-45 minutes** ⏱️

---

**Votre site sera bientôt en ligne !** 🚀

Si vous rencontrez des problèmes, consultez les guides détaillés dans `backend/DEPLOYMENT.md` et `NETLIFY_DEPLOYMENT.md`.
