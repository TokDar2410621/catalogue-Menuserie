# Guide de Déploiement - DKBOIS Frontend sur Netlify

Ce guide vous explique comment déployer le frontend (HTML/CSS/JS) sur Netlify.

## Prérequis

- Backend déployé sur Railway (voir [backend/DEPLOYMENT.md](backend/DEPLOYMENT.md))
- URL du backend Railway (ex: `https://votre-projet.up.railway.app`)
- Compte GitHub (gratuit)
- Compte Netlify (gratuit)

## Étape 1 : Mettre à Jour l'URL de l'API

Avant de déployer, vous devez mettre à jour `api-config.js` avec l'URL de votre backend Railway.

### 1.1 Modifier api-config.js

Ouvrez le fichier [api-config.js](api-config.js) et remplacez l'URL locale par votre URL Railway :

```javascript
// Avant (développement local)
const API_BASE_URL = 'http://localhost:3000/api';

// Après (production)
const API_BASE_URL = 'https://votre-projet.up.railway.app/api';
```

**Remplacez `votre-projet.up.railway.app` par votre vraie URL Railway !**

### 1.2 Pousser les changements sur GitHub

```bash
cd "c:\Users\Darius\Desktop\catalogue Menuserie"
git add api-config.js
git commit -m "Configuration API pour production"
git push origin main
```

## Étape 2 : Créer un Compte Netlify

1. Allez sur [netlify.com](https://www.netlify.com)
2. Cliquez sur **"Sign up"**
3. Connectez-vous avec votre compte GitHub
4. Autorisez Netlify à accéder à vos repositories

## Étape 3 : Déployer le Site

### Méthode 1 : Déploiement depuis GitHub (Recommandé)

1. Sur le dashboard Netlify, cliquez sur **"Add new site"** → **"Import an existing project"**
2. Choisissez **"Deploy with GitHub"**
3. Sélectionnez votre repository **"catalogue Menuserie"**
4. Configurez le déploiement :

| Paramètre | Valeur |
|-----------|--------|
| **Branch to deploy** | `main` |
| **Base directory** | (laisser vide - racine du projet) |
| **Build command** | (laisser vide - pas de build nécessaire) |
| **Publish directory** | `.` (ou laisser vide) |

5. Cliquez sur **"Deploy site"**

### Méthode 2 : Déploiement par Drag & Drop (Simple mais moins pratique)

1. Sur le dashboard Netlify, faites glisser le dossier de votre projet directement dans la zone de dépôt
2. Netlify va déployer automatiquement

**Note :** Cette méthode ne permet pas les mises à jour automatiques depuis GitHub.

## Étape 4 : Configurer le Site

### 4.1 Changer le nom du site

Par défaut, Netlify génère un nom aléatoire (ex: `random-name-123.netlify.app`). Pour le personnaliser :

1. Dans votre site Netlify, allez dans **"Site settings"**
2. Cliquez sur **"Change site name"**
3. Entrez un nom descriptif (ex: `dkbois` ou `menuiserie-dkbois`)
4. Votre site sera accessible à : `https://dkbois.netlify.app`

### 4.2 Configurer les redirections (Important pour les SPA)

Créez un fichier `_redirects` à la racine du projet pour gérer les URLs :

**Fichier : `_redirects`**
```
# Rediriger toutes les routes vers index.html (pour éviter les 404)
/*    /index.html   200
```

**OU** créez un fichier `netlify.toml` :

**Fichier : `netlify.toml`**
```toml
[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
```

**Pourquoi ?** Si quelqu'un accède directement à `https://dkbois.netlify.app/portfolio.html`, Netlify doit savoir comment gérer cette route.

### 4.3 Commit et push

```bash
git add _redirects
# OU
git add netlify.toml

git commit -m "Ajout configuration Netlify"
git push origin main
```

Netlify va automatiquement redéployer votre site.

## Étape 5 : Mettre à Jour les Variables d'Environnement du Backend

Maintenant que vous avez l'URL de votre frontend Netlify, vous devez la configurer dans Railway :

1. Allez sur [railway.app](https://railway.app)
2. Ouvrez votre projet backend
3. Cliquez sur votre service Django
4. Allez dans **"Variables"**
5. Mettez à jour les variables suivantes :

| Variable | Nouvelle Valeur |
|----------|-----------------|
| `CORS_ALLOWED_ORIGINS` | `https://dkbois.netlify.app` (votre URL Netlify) |
| `CSRF_TRUSTED_ORIGINS` | `https://votre-backend.up.railway.app,https://dkbois.netlify.app` |

**Important :** Séparez les URLs par des virgules, sans espaces.

6. Sauvegardez et attendez que Railway redéploie automatiquement

## Étape 6 : Tester le Site

1. Ouvrez votre site : `https://dkbois.netlify.app` (ou votre nom choisi)
2. Vérifiez que :
   - ✅ La page d'accueil charge correctement
   - ✅ Les images s'affichent
   - ✅ La navigation fonctionne
   - ✅ Les données de l'API s'affichent (services, projets, témoignages)
   - ✅ Le changement de langue fonctionne
   - ✅ Le formulaire de contact fonctionne

### Vérifier la Console du Navigateur

Ouvrez la console (F12) et vérifiez qu'il n'y a pas d'erreurs :
- ❌ Pas d'erreurs CORS
- ❌ Pas d'erreurs 404 pour les fichiers
- ❌ Pas d'erreurs API

## Étape 7 : Configurer un Domaine Personnalisé (Optionnel)

Si vous avez acheté un nom de domaine (ex: `dkbois.cm`), vous pouvez le lier à Netlify :

1. Dans Netlify, allez dans **"Domain settings"**
2. Cliquez sur **"Add custom domain"**
3. Entrez votre domaine (ex: `dkbois.cm`)
4. Netlify va vous donner des instructions DNS
5. Allez chez votre registrar de domaine et ajoutez les DNS records
6. Attendez la propagation DNS (quelques heures)
7. Netlify va automatiquement configurer le SSL (HTTPS gratuit avec Let's Encrypt)

## Mises à Jour Automatiques

Avec le déploiement GitHub, chaque fois que vous faites `git push`, Netlify redéploie automatiquement :

```bash
# Faire des modifications
git add .
git commit -m "Mise à jour du design"
git push origin main

# Netlify redéploie automatiquement en 1-2 minutes
```

## Limites du Plan Gratuit Netlify

- ✅ **Bande passante illimitée** (presque)
- ✅ **100 GB/mois** de bande passante
- ✅ **Sites illimités**
- ✅ **SSL gratuit** (HTTPS automatique)
- ✅ **Déploiements automatiques** depuis GitHub
- ✅ **300 minutes de build par mois** (largement suffisant)

Pour DKBOIS, le plan gratuit est **parfait** car il n'y a pas de build process.

## Troubleshooting

### Problème : Erreurs CORS dans la console

**Symptôme :**
```
Access to fetch at 'https://backend.railway.app/api/projects/' from origin 'https://dkbois.netlify.app'
has been blocked by CORS policy
```

**Solution :**
1. Vérifiez que `CORS_ALLOWED_ORIGINS` dans Railway contient votre URL Netlify
2. Pas d'espaces dans la variable
3. Incluez `https://` dans l'URL
4. Redémarrez le service Railway après modification

### Problème : Page blanche ou erreur 404

**Solution :**
1. Vérifiez que vous avez créé le fichier `_redirects` ou `netlify.toml`
2. Vérifiez que tous vos liens HTML sont relatifs (pas d'URL absolues locales)
3. Ouvrez la console (F12) pour voir les erreurs exactes

### Problème : Les données de l'API ne s'affichent pas

**Solution :**
1. Vérifiez que `api-config.js` contient la bonne URL Railway
2. Testez l'API directement : `https://votre-backend.up.railway.app/api/projects/?lang=fr`
3. Vérifiez les erreurs CORS (voir ci-dessus)
4. Vérifiez que le backend Railway est bien déployé et actif

### Problème : Images manquantes

**Solution :**
1. Vérifiez que les chemins d'images sont relatifs (ex: `./images/logo.png` et non `/images/logo.png`)
2. Vérifiez que le dossier `images/` est bien commité dans Git
3. Testez en local d'abord avec un serveur HTTP (`npx http-server`)

### Problème : Formulaire de contact ne fonctionne pas

**Solution :**
1. Ouvrez la console (F12) et vérifiez les erreurs
2. Assurez-vous que `contact.js` utilise bien `API.contact.submit()`
3. Testez l'endpoint directement avec curl :
```bash
curl -X POST https://votre-backend.up.railway.app/api/contact/ \
  -H "Content-Type: application/json" \
  -d '{"firstname":"Test","lastname":"User","email":"test@example.com","phone":"123","project_type":"renovation","description":"Test","gdpr_consent":true}'
```

## Vérification du Déploiement Complet

Checklist finale :

- [ ] Backend Railway accessible et API fonctionne
- [ ] Frontend Netlify déployé et accessible
- [ ] `api-config.js` contient la bonne URL Railway
- [ ] Variables `CORS_ALLOWED_ORIGINS` et `CSRF_TRUSTED_ORIGINS` configurées dans Railway
- [ ] Pas d'erreurs CORS dans la console
- [ ] Toutes les pages fonctionnent (accueil, portfolio, services, about, contact)
- [ ] Changement de langue fonctionne
- [ ] Images et fichiers statiques chargent correctement
- [ ] Formulaire de contact envoie bien les données
- [ ] SSL/HTTPS activé (cadenas vert dans le navigateur)

## Commandes Utiles

```bash
# Installer Netlify CLI (optionnel)
npm install -g netlify-cli

# Se connecter à Netlify
netlify login

# Déployer manuellement
netlify deploy --prod

# Ouvrir le site dans le navigateur
netlify open

# Voir les logs de déploiement
netlify deploy --build
```

## Prochaines Étapes

- [ ] Ajouter Google Analytics pour suivre les visiteurs
- [ ] Configurer un domaine personnalisé
- [ ] Ajouter des métadonnées SEO (Open Graph, Twitter Cards)
- [ ] Optimiser les images pour le web
- [ ] Tester les performances avec Lighthouse

---

## Support

- **Documentation Netlify :** https://docs.netlify.com
- **Support Netlify :** https://answers.netlify.com

---

**Félicitations ! Votre site DKBOIS est maintenant en ligne !** 🎉

- **Frontend :** https://dkbois.netlify.app
- **Backend API :** https://votre-projet.up.railway.app/api/
- **Admin Django :** https://votre-projet.up.railway.app/admin/
