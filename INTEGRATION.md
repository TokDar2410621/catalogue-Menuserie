# Intégration Frontend-Backend DKbois

## ✅ Ce qui a été fait

### 1. Configuration API ([api-config.js](api-config.js))
- Fichier centralisé pour toutes les interactions avec l'API
- URL de base configurable : `http://localhost:3000/api`
- Fonctions utilitaires pour chaque ressource (projets, services, témoignages, etc.)
- Gestion d'erreurs intégrée

### 2. Page d'accueil ([main.js](main.js)) ✅ TERMINÉ
- ✅ Services chargés depuis `/api/services/`
- ✅ Portfolio (projets vedettes) depuis `/api/projects/featured/`
- ✅ Témoignages depuis `/api/testimonials/`
- ✅ Support du changement de langue dynamique
- ✅ Gestion d'erreurs avec messages utilisateur

## 🔄 En cours

###  3. Page Portfolio ([portfolio.js](portfolio.js))
- Chargement de tous les projets avec filtres
- Filtrage par catégorie, type, matériau
- Pagination si nécessaire

### 4. Page Projet détaillé ([project.js](project.js))
- Chargement d'un projet spécifique via slug
- Affichage des détails complets

### 5. Page Services ([services.js](services.js))
- Chargement des services détaillés
- Processus et étapes

### 6. Page À Propos ([about.js](about.js))
- Équipe depuis `/api/team/`
- Timeline depuis `/api/timeline/`
- Valeurs depuis `/api/values/`

### 7. Page Contact ([contact.js](contact.js))
- Soumission du formulaire vers `/api/contact/`
- Chargement des FAQs depuis `/api/faqs/`
- Validation et messages de confirmation

## 📝 Notes importantes

### API Endpoints utilisés
```
GET  /api/projects/              - Liste des projets (avec filtres)
GET  /api/projects/featured/     - Projets vedettes
GET  /api/projects/{slug}/       - Détail d'un projet
GET  /api/services/              - Liste des services
GET  /api/services/{slug}/       - Détail d'un service
GET  /api/testimonials/          - Témoignages
GET  /api/team/                  - Membres de l'équipe
GET  /api/timeline/              - Événements timeline
GET  /api/values/                - Valeurs de l'entreprise
GET  /api/faqs/                  - Questions fréquentes
POST /api/contact/               - Soumission formulaire contact
```

### Paramètres de langue
Tous les endpoints supportent le paramètre `?lang=fr` ou `?lang=en`

### CORS
Le backend est configuré pour accepter les requêtes depuis :
- `http://localhost:3000`
- `http://localhost:8000`
- `http://127.0.0.1:3000`
- `http://127.0.0.1:8000`

## 🎯 Prochaines étapes

1. Terminer l'intégration de tous les fichiers JS
2. Tester chaque page individuellement
3. Vérifier le changement de langue sur toutes les pages
4. Tester la soumission du formulaire de contact
5. Vérifier les filtres du portfolio

## 🚀 Pour tester

1. Assurez-vous que le serveur Django tourne sur le port 3000 :
   ```bash
   cd backend
   py -3.13 manage.py runserver 3000
   ```

2. Ouvrez le frontend avec un serveur local (VS Code Live Server, etc.)

3. Vérifiez la console du navigateur pour les éventuelles erreurs

4. Testez le changement de langue (bouton EN/FR)

## ⚠️ Important

- Les données sont maintenant **dynamiques** et proviennent de la base de données
- Pour modifier le contenu, utilisez l'interface admin Django
- Les modifications sont instantanées (pas besoin de rebuild)
