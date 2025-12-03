# CRUD API Guide - Projects and Services

Complete guide for using the full CRUD (Create, Read, Update, Delete) endpoints for Projects and Services.

## Base URL

```
http://localhost:3000/api
```

## Authentication & Permissions

**Current State (Development):**
- All endpoints are publicly accessible (no authentication required)
- `permission_classes = [AllowAny]`

**Production TODO:**
- Add authentication (JWT, Session, or Token-based)
- Update permission classes:
  - `GET` endpoints: Public access (AllowAny)
  - `POST/PUT/PATCH/DELETE` endpoints: Require authentication (IsAuthenticated or IsAdminUser)
- Update both `ProjectViewSet` and `ServiceViewSet` in `views.py`

## Content Type

All POST/PUT/PATCH requests must use JSON:
```
Content-Type: application/json
```

---

## PROJECTS API

### 1. List Projects (GET)

**Endpoint:** `GET /api/projects/`

**Query Parameters:**
- `lang` - Language code (`fr` or `en`, default: `fr`)
- `category` - Filter by category (`kitchen`, `living`, `exterior`)
- `type` - Filter by type (`creation`, `restoration`, `fitting`)
- `material` - Filter by material (`oak`, `walnut`, `maple`)
- `featured` - Filter featured projects (`true` or `false`)
- `search` - Search in titles and tags
- `ordering` - Order by field (`order`, `created_at`, `-created_at`)

**Example:**
```bash
# List all projects in French
curl http://localhost:3000/api/projects/?lang=fr

# List featured kitchen projects
curl http://localhost:3000/api/projects/?category=kitchen&featured=true

# Search projects
curl http://localhost:3000/api/projects/?search=moderne
```

**Response:** 200 OK
```json
[
  {
    "id": 1,
    "slug": "cuisine-moderne",
    "title": "Cuisine Moderne",
    "category": "kitchen",
    "type": "creation",
    "material": "oak",
    "short_desc": "Une cuisine moderne...",
    "tags": ["Cuisine", "Moderne"],
    "images": ["image/cuisine.jpg"],
    "featured": true,
    "order": 1
  }
]
```

---

### 2. Get Project Detail (GET)

**Endpoint:** `GET /api/projects/{slug}/`

**Example:**
```bash
curl http://localhost:3000/api/projects/cuisine-moderne/?lang=fr
```

**Response:** 200 OK
```json
{
  "id": 1,
  "slug": "cuisine-moderne",
  "title": "Cuisine Moderne",
  "category": "kitchen",
  "type": "creation",
  "material": "oak",
  "short_desc": "Une cuisine moderne...",
  "full_desc": "Description complète de la cuisine...",
  "challenge": "Le défi principal était...",
  "specs": {
    "duration": "2 semaines",
    "location": "Yaoundé",
    "finish": "Vernis mat"
  },
  "tags": ["Cuisine", "Moderne"],
  "images": ["image/cuisine.jpg"],
  "featured": true,
  "created_at": "2025-01-15T10:30:00Z",
  "updated_at": "2025-01-15T10:30:00Z"
}
```

---

### 3. Create Project (POST)

**Endpoint:** `POST /api/projects/`

**Required Fields:**
- `title_fr`, `title_en` - Project titles
- `category` - One of: `kitchen`, `living`, `exterior`
- `type` - One of: `creation`, `restoration`, `fitting`
- `material` - One of: `oak`, `walnut`, `maple`
- `short_desc_fr`, `short_desc_en` - Short descriptions
- `full_desc_fr`, `full_desc_en` - Full descriptions

**Optional Fields:**
- `slug` - Auto-generated if not provided
- `challenge_fr`, `challenge_en` - Challenge descriptions
- `duration_fr`, `duration_en` - Project duration
- `location` - Project location
- `finish_fr`, `finish_en` - Finish type
- `tags` - Array of tags (default: `[]`)
- `images` - Array of image URLs (default: `[]`)
- `featured` - Boolean (default: `false`)
- `order` - Display order (default: `0`)

**Example:**
```bash
curl -X POST http://localhost:3000/api/projects/ \
  -H "Content-Type: application/json" \
  -d '{
    "title_fr": "Cuisine Moderne",
    "title_en": "Modern Kitchen",
    "category": "kitchen",
    "type": "creation",
    "material": "oak",
    "short_desc_fr": "Une cuisine moderne et fonctionnelle",
    "short_desc_en": "A modern and functional kitchen",
    "full_desc_fr": "Description complète de la cuisine moderne avec tous les détails.",
    "full_desc_en": "Full description of the modern kitchen with all details.",
    "challenge_fr": "Optimiser l'\''espace dans une petite cuisine",
    "challenge_en": "Optimize space in a small kitchen",
    "duration_fr": "2 semaines",
    "duration_en": "2 weeks",
    "location": "Yaoundé",
    "finish_fr": "Vernis mat",
    "finish_en": "Matte varnish",
    "tags": ["Cuisine", "Moderne", "Chêne"],
    "images": ["image/cuisine-moderne.jpg", "image/cuisine-moderne-2.jpg"],
    "featured": true,
    "order": 1
  }'
```

**Response:** 201 Created
```json
{
  "message": "Project created successfully",
  "data": {
    "slug": "modern-kitchen",
    "title_fr": "Cuisine Moderne",
    "title_en": "Modern Kitchen",
    "category": "kitchen",
    "type": "creation",
    "material": "oak",
    // ... all fields
  }
}
```

**Error Response:** 400 Bad Request
```json
{
  "title_fr": ["This field is required."],
  "category": ["\"invalid\" is not a valid choice."]
}
```

---

### 4. Update Project (PUT)

**Endpoint:** `PUT /api/projects/{slug}/`

**Note:** PUT requires all fields (full update). Use PATCH for partial updates.

**Example:**
```bash
curl -X PUT http://localhost:3000/api/projects/cuisine-moderne/ \
  -H "Content-Type: application/json" \
  -d '{
    "slug": "cuisine-moderne",
    "title_fr": "Cuisine Moderne Mise à Jour",
    "title_en": "Updated Modern Kitchen",
    "category": "kitchen",
    "type": "creation",
    "material": "walnut",
    "short_desc_fr": "Description mise à jour",
    "short_desc_en": "Updated description",
    "full_desc_fr": "Description complète mise à jour",
    "full_desc_en": "Updated full description",
    "tags": ["Cuisine", "Moderne", "Noyer"],
    "images": ["image/cuisine-updated.jpg"],
    "featured": false,
    "order": 2
  }'
```

**Response:** 200 OK
```json
{
  "message": "Project updated successfully",
  "data": {
    // Updated project data
  }
}
```

---

### 5. Partial Update Project (PATCH)

**Endpoint:** `PATCH /api/projects/{slug}/`

**Note:** Only include fields you want to update.

**Example:**
```bash
curl -X PATCH http://localhost:3000/api/projects/cuisine-moderne/ \
  -H "Content-Type: application/json" \
  -d '{
    "featured": true,
    "order": 1
  }'
```

**Response:** 200 OK
```json
{
  "message": "Project updated successfully",
  "data": {
    // Updated project data with changes applied
  }
}
```

---

### 6. Delete Project (DELETE)

**Endpoint:** `DELETE /api/projects/{slug}/`

**Example:**
```bash
curl -X DELETE http://localhost:3000/api/projects/cuisine-moderne/
```

**Response:** 204 No Content
```json
{
  "message": "Project deleted successfully"
}
```

**Error Response:** 404 Not Found
```json
{
  "detail": "Not found."
}
```

---

### 7. Get Featured Projects (GET)

**Endpoint:** `GET /api/projects/featured/`

**Example:**
```bash
curl http://localhost:3000/api/projects/featured/?lang=fr
```

**Response:** 200 OK - Array of featured projects

---

## SERVICES API

### 1. List Services (GET)

**Endpoint:** `GET /api/services/`

**Query Parameters:**
- `lang` - Language code (`fr` or `en`, default: `fr`)
- `show_all` - Show inactive services (`true` or `false`, default: `false`)

**Example:**
```bash
# List active services in French
curl http://localhost:3000/api/services/?lang=fr

# List all services including inactive (for admin)
curl http://localhost:3000/api/services/?show_all=true
```

**Response:** 200 OK
```json
[
  {
    "id": 1,
    "service_id": "interior",
    "slug": "menuiserie-interieure",
    "icon": "hammer",
    "title": "Menuiserie Intérieure",
    "description": "Création de portes, fenêtres...",
    "sub_services": {
      "fr": ["Portes", "Fenêtres"],
      "en": ["Doors", "Windows"]
    },
    "process_steps": [...],
    "timeframe": "2-4 semaines",
    "images": ["image/menuiserie.jpg"],
    "order": 1,
    "is_active": true
  }
]
```

---

### 2. Get Service Detail (GET)

**Endpoint:** `GET /api/services/{slug}/`

**Example:**
```bash
curl http://localhost:3000/api/services/menuiserie-interieure/?lang=fr
```

**Response:** 200 OK
```json
{
  "id": 1,
  "service_id": "interior",
  "slug": "menuiserie-interieure",
  "icon": "hammer",
  "title": "Menuiserie Intérieure",
  "description": "Description complète du service...",
  "sub_services": {
    "fr": ["Portes sur mesure", "Fenêtres"],
    "en": ["Custom doors", "Windows"]
  },
  "process_steps": {
    "fr": [
      {"step": 1, "title": "Consultation", "description": "..."},
      {"step": 2, "title": "Conception", "description": "..."}
    ],
    "en": [...]
  },
  "timeframe": "2-4 semaines",
  "images": ["image/menuiserie-1.jpg", "image/menuiserie-2.jpg"],
  "order": 1,
  "is_active": true
}
```

---

### 3. Create Service (POST)

**Endpoint:** `POST /api/services/`

**Required Fields:**
- `service_id` - Unique identifier (e.g., "interior", "cabinetry")
- `icon` - Lucide icon name
- `title_fr`, `title_en` - Service titles
- `description_fr`, `description_en` - Service descriptions

**Optional Fields:**
- `slug` - Auto-generated from service_id if not provided
- `sub_services` - Object with `fr` and `en` arrays (default: `[]`)
- `process_steps` - Object with `fr` and `en` arrays (default: `[]`)
- `timeframe_fr`, `timeframe_en` - Estimated timeframe
- `images` - Array of image URLs (default: `[]`)
- `order` - Display order (default: `0`)
- `is_active` - Boolean (default: `true`)

**Example:**
```bash
curl -X POST http://localhost:3000/api/services/ \
  -H "Content-Type: application/json" \
  -d '{
    "service_id": "custom-furniture",
    "icon": "armchair",
    "title_fr": "Mobilier Sur Mesure",
    "title_en": "Custom Furniture",
    "description_fr": "Création de mobilier personnalisé selon vos besoins",
    "description_en": "Creation of custom furniture according to your needs",
    "sub_services": {
      "fr": ["Tables", "Chaises", "Étagères"],
      "en": ["Tables", "Chairs", "Shelves"]
    },
    "process_steps": {
      "fr": [
        {
          "step": 1,
          "title": "Consultation",
          "description": "Rencontre pour discuter de vos besoins"
        },
        {
          "step": 2,
          "title": "Conception",
          "description": "Création des plans et maquettes"
        },
        {
          "step": 3,
          "title": "Fabrication",
          "description": "Réalisation du mobilier en atelier"
        },
        {
          "step": 4,
          "title": "Installation",
          "description": "Livraison et installation chez vous"
        }
      ],
      "en": [
        {
          "step": 1,
          "title": "Consultation",
          "description": "Meeting to discuss your needs"
        },
        {
          "step": 2,
          "title": "Design",
          "description": "Creation of plans and mockups"
        },
        {
          "step": 3,
          "title": "Manufacturing",
          "description": "Furniture creation in workshop"
        },
        {
          "step": 4,
          "title": "Installation",
          "description": "Delivery and installation at your place"
        }
      ]
    },
    "timeframe_fr": "3-6 semaines",
    "timeframe_en": "3-6 weeks",
    "images": ["image/mobilier.jpg"],
    "order": 4,
    "is_active": true
  }'
```

**Response:** 201 Created
```json
{
  "message": "Service created successfully",
  "data": {
    "service_id": "custom-furniture",
    "slug": "custom-furniture",
    "icon": "armchair",
    "title_fr": "Mobilier Sur Mesure",
    // ... all fields
  }
}
```

---

### 4. Update Service (PUT)

**Endpoint:** `PUT /api/services/{slug}/`

**Example:**
```bash
curl -X PUT http://localhost:3000/api/services/mobilier-sur-mesure/ \
  -H "Content-Type: application/json" \
  -d '{
    "service_id": "custom-furniture",
    "slug": "mobilier-sur-mesure",
    "icon": "armchair",
    "title_fr": "Mobilier Sur Mesure Premium",
    "title_en": "Premium Custom Furniture",
    "description_fr": "Description mise à jour",
    "description_en": "Updated description",
    "sub_services": {
      "fr": ["Tables", "Chaises", "Étagères", "Bureaux"],
      "en": ["Tables", "Chairs", "Shelves", "Desks"]
    },
    "process_steps": {...},
    "timeframe_fr": "4-8 semaines",
    "timeframe_en": "4-8 weeks",
    "images": ["image/mobilier-premium.jpg"],
    "order": 3,
    "is_active": true
  }'
```

**Response:** 200 OK
```json
{
  "message": "Service updated successfully",
  "data": {
    // Updated service data
  }
}
```

---

### 5. Partial Update Service (PATCH)

**Endpoint:** `PATCH /api/services/{slug}/`

**Example:**
```bash
curl -X PATCH http://localhost:3000/api/services/mobilier-sur-mesure/ \
  -H "Content-Type: application/json" \
  -d '{
    "is_active": false,
    "order": 10
  }'
```

**Response:** 200 OK
```json
{
  "message": "Service updated successfully",
  "data": {
    // Updated service data
  }
}
```

---

### 6. Delete Service (DELETE)

**Endpoint:** `DELETE /api/services/{slug}/`

**Example:**
```bash
curl -X DELETE http://localhost:3000/api/services/mobilier-sur-mesure/
```

**Response:** 204 No Content
```json
{
  "message": "Service deleted successfully"
}
```

---

## Error Responses

### Validation Errors (400 Bad Request)
```json
{
  "field_name": ["Error message"],
  "another_field": ["Another error message"]
}
```

### Not Found (404)
```json
{
  "detail": "Not found."
}
```

### Unique Constraint Violation (400)
```json
{
  "slug": ["A project with this slug already exists."],
  "service_id": ["A service with this service_id already exists."]
}
```

---

## Data Format Notes

### Project Categories
- `kitchen` - Kitchen projects
- `living` - Living room/furniture projects
- `exterior` - Exterior/outdoor projects

### Project Types
- `creation` - New creation from scratch
- `restoration` - Restoration of existing items
- `fitting` - Installation/fitting work

### Project Materials
- `oak` - Oak wood (Chêne)
- `walnut` - Walnut wood (Noyer)
- `maple` - Maple wood (Érable)

### Service Icons
Use any valid [Lucide icon name](https://lucide.dev/icons/):
- `hammer` - For construction/joinery
- `armchair` - For furniture
- `door-open` - For doors
- `window` - For windows
- `wrench` - For repairs/restoration

### JSON Fields Format

**Tags** (array of strings):
```json
"tags": ["Cuisine", "Moderne", "Chêne"]
```

**Images** (array of URLs):
```json
"images": ["image/projet-1.jpg", "image/projet-2.jpg"]
```

**Sub-services** (bilingual object):
```json
"sub_services": {
  "fr": ["Service 1", "Service 2"],
  "en": ["Service 1", "Service 2"]
}
```

**Process steps** (bilingual array of objects):
```json
"process_steps": {
  "fr": [
    {"step": 1, "title": "Étape 1", "description": "Description"},
    {"step": 2, "title": "Étape 2", "description": "Description"}
  ],
  "en": [
    {"step": 1, "title": "Step 1", "description": "Description"},
    {"step": 2, "title": "Step 2", "description": "Description"}
  ]
}
```

---

## Testing

### Using Python Test Script
```bash
cd backend
python test_crud_api.py
```

### Using curl
See examples above for each endpoint.

### Using JavaScript (fetch)
```javascript
// Create project
const response = await fetch('http://localhost:3000/api/projects/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    title_fr: "Nouveau Projet",
    title_en: "New Project",
    category: "kitchen",
    type: "creation",
    material: "oak",
    short_desc_fr: "Description courte",
    short_desc_en: "Short description",
    full_desc_fr: "Description complète",
    full_desc_en: "Full description"
  })
});

const data = await response.json();
console.log(data);
```

---

## Next Steps for Production

1. **Add Authentication:**
   ```python
   from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

   class ProjectViewSet(viewsets.ModelViewSet):
       permission_classes = [IsAuthenticatedOrReadOnly]
       # Or for admin-only write access:
       # permission_classes = [IsAdminUser]
   ```

2. **Add JWT or Token Authentication:**
   - Install: `pip install djangorestframework-simplejwt`
   - Configure in settings.py
   - Add authentication endpoints

3. **Add Rate Limiting:**
   - Install: `pip install django-ratelimit`
   - Apply to create/update/delete endpoints

4. **Add File Upload Support:**
   - Configure `MEDIA_ROOT` and `MEDIA_URL`
   - Add `ImageField` to models
   - Create upload endpoint for images

5. **Add Audit Logging:**
   - Track who created/modified records
   - Add `created_by` and `modified_by` fields

6. **Add Soft Delete:**
   - Add `deleted_at` field
   - Filter out deleted records by default
   - Allow admin to restore deleted items
