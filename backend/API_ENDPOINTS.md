# DKbois API Endpoints Reference

Complete reference for all available API endpoints.

## Base URL

```
http://127.0.0.1:8000/api/
```

## Language Parameter

All endpoints support the `lang` query parameter:
- `?lang=fr` - French (default)
- `?lang=en` - English

Example: `/api/projects/?lang=en`

---

## Projects

### List All Projects
**GET** `/api/projects/`

**Query Parameters:**
- `lang` - Language (fr/en)
- `category` - Filter by category (kitchen/living/exterior)
- `type` - Filter by type (creation/restoration/fitting)
- `material` - Filter by material (oak/walnut/maple)
- `featured` - Filter by featured status (true/false)
- `search` - Search in titles
- `ordering` - Order by field (order/-created_at)
- `page` - Page number (pagination)

**Response:**
```json
{
  "count": 3,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "slug": "cuisine-haussmannienne",
      "title": "Cuisine Haussmannienne",
      "category": "kitchen",
      "type": "fitting",
      "material": "oak",
      "short_desc": "Alliance du charme ancien et de la modernité.",
      "tags": ["Cuisine", "Chêne", "Haussmann"],
      "images": ["url1", "url2"],
      "featured": true,
      "order": 1
    }
  ]
}
```

### Get Project Detail
**GET** `/api/projects/{slug}/`

**Example:** `/api/projects/cuisine-haussmannienne/?lang=fr`

**Response:**
```json
{
  "id": 1,
  "slug": "cuisine-haussmannienne",
  "title": "Cuisine Haussmannienne",
  "category": "kitchen",
  "type": "fitting",
  "material": "oak",
  "short_desc": "Alliance du charme ancien et de la modernité.",
  "full_desc": "Rénovation complète d'une cuisine...",
  "challenge": "Intégration de l'électroménager...",
  "specs": {
    "duration": "3 mois",
    "location": "Paris 7ème",
    "finish": "Huile naturelle mate"
  },
  "tags": ["Cuisine", "Chêne", "Haussmann"],
  "images": ["url1", "url2", "url3"],
  "featured": true,
  "created_at": "2025-01-01T12:00:00Z",
  "updated_at": "2025-01-01T12:00:00Z"
}
```

### Get Featured Projects
**GET** `/api/projects/featured/`

Returns only projects with `featured=true`

---

## Services

### List All Services
**GET** `/api/services/`

**Response:**
```json
[
  {
    "id": 1,
    "service_id": "interior",
    "slug": "menuiserie-interieure",
    "icon": "door-open",
    "title": "Menuiserie Intérieure",
    "description": "Nous façonnons votre espace de vie...",
    "sub_services": [
      {"fr": "Portes et fenêtres", "en": "Custom doors and windows"}
    ],
    "process_steps": [
      {"step": 1, "title": {"fr": "Relevé & Conception", "en": "Survey & Design"}}
    ],
    "timeframe": "6 à 10 semaines",
    "images": ["url1", "url2"],
    "order": 1,
    "is_active": true
  }
]
```

### Get Service Detail
**GET** `/api/services/{slug}/`

**Example:** `/api/services/menuiserie-interieure/?lang=en`

---

## Testimonials

### List All Testimonials
**GET** `/api/testimonials/`

**Response:**
```json
[
  {
    "id": 1,
    "name": "Jean Dupont",
    "role": "Architecte d'intérieur",
    "text": "Une précision incroyable...",
    "stars": 5,
    "image": "https://...",
    "order": 1
  }
]
```

---

## Team Members

### List All Team Members
**GET** `/api/team/`

**Response:**
```json
[
  {
    "id": 1,
    "name": "Marc Dubois",
    "role": "Maître Ébéniste",
    "experience_years": 25,
    "quote": "Le bois ne ment jamais.",
    "image": "https://...",
    "order": 1
  }
]
```

---

## Timeline

### List Timeline Events
**GET** `/api/timeline/`

**Response:**
```json
[
  {
    "id": 1,
    "year": "1990",
    "title": "La Fondation",
    "description": "Création de l'atelier par Pierre Dubois...",
    "order": 1
  }
]
```

---

## Company Values

### List Company Values
**GET** `/api/values/`

**Response:**
```json
[
  {
    "id": 1,
    "icon": "hammer",
    "title": "Savoir-Faire",
    "description": "Maîtrise des techniques ancestrales...",
    "order": 1
  }
]
```

---

## FAQs

### List FAQs
**GET** `/api/faqs/`

**Response:**
```json
[
  {
    "id": 1,
    "question": "Quels sont vos délais de réalisation ?",
    "answer": "Nos délais varient selon la complexité...",
    "order": 1
  }
]
```

---

## Contact Submissions

### Submit Contact Form
**POST** `/api/contact/`

**Headers:**
```
Content-Type: application/json
```

**Request Body:**
```json
{
  "firstname": "Jean",
  "lastname": "Dupont",
  "email": "jean.dupont@example.com",
  "phone": "0123456789",
  "project_type": "cabinetry",
  "budget": "5000-15000",
  "description": "Je souhaite une bibliothèque sur mesure",
  "gdpr_consent": true
}
```

**Field Options:**
- `project_type`: interior | cabinetry | restoration | fitting | other
- `budget`: < 5000 | 5000-15000 | > 15000

**Response:**
```json
{
  "message": "Contact submission received successfully",
  "data": {
    "id": 1,
    "firstname": "Jean",
    "lastname": "Dupont",
    "email": "jean.dupont@example.com",
    "phone": "0123456789",
    "project_type": "cabinetry",
    "budget": "5000-15000",
    "description": "Je souhaite une bibliothèque sur mesure",
    "files": [],
    "gdpr_consent": true,
    "created_at": "2025-01-01T12:00:00Z"
  }
}
```

### List Contact Submissions (Admin Only)
**GET** `/api/contact/`

Requires authentication with staff/admin user.

---

## Error Responses

### 400 Bad Request
```json
{
  "field_name": ["Error message"]
}
```

### 404 Not Found
```json
{
  "detail": "Not found."
}
```

### 500 Server Error
```json
{
  "detail": "Internal server error"
}
```

---

## Pagination

All list endpoints are paginated with 20 items per page.

**Response structure:**
```json
{
  "count": 50,
  "next": "http://127.0.0.1:8000/api/projects/?page=2",
  "previous": null,
  "results": [...]
}
```

**Navigate pages:**
- `/api/projects/?page=2`
- `/api/projects/?page=3`

---

## Examples with cURL

### Get all projects in English
```bash
curl "http://127.0.0.1:8000/api/projects/?lang=en"
```

### Filter projects by kitchen category
```bash
curl "http://127.0.0.1:8000/api/projects/?category=kitchen&lang=fr"
```

### Get a specific project
```bash
curl "http://127.0.0.1:8000/api/projects/cuisine-haussmannienne/?lang=fr"
```

### Submit contact form
```bash
curl -X POST http://127.0.0.1:8000/api/contact/ \
  -H "Content-Type: application/json" \
  -d '{
    "firstname": "Jean",
    "lastname": "Dupont",
    "email": "jean@example.com",
    "phone": "0123456789",
    "project_type": "cabinetry",
    "budget": "5000-15000",
    "description": "Je souhaite un devis pour une bibliothèque",
    "gdpr_consent": true
  }'
```

---

## CORS Configuration

The API accepts requests from:
- http://localhost:3000
- http://localhost:5500
- http://localhost:8080
- http://127.0.0.1:3000
- http://127.0.0.1:5500
- http://127.0.0.1:8080

And currently allows all origins in development mode.

---

## Rate Limiting

Currently no rate limiting is implemented. Consider adding it for production.

---

## Authentication

- Most endpoints are **public** (read-only)
- **Contact submission** is public (POST only)
- **Admin operations** require authentication
- Use Django admin credentials to access protected endpoints

---

## Content-Type

All responses are in `application/json` format.

All POST requests must include:
```
Content-Type: application/json
```
