# DKbois Backend - Django REST API

Complete Django backend with REST API for the DKbois woodworking portfolio website.

## Features

- Full REST API with bilingual content support (French/English)
- Django Admin interface for content management
- Custom admin dashboard with statistics
- CORS enabled for frontend integration
- SQLite database (easily upgradeable to PostgreSQL)
- Comprehensive data models for:
  - Portfolio projects with filtering
  - Services
  - Testimonials
  - Team members
  - Company timeline
  - Company values
  - FAQs
  - Contact form submissions

## Technology Stack

- Django 5.1.7
- Django REST Framework 3.15.2
- django-cors-headers 4.7.0
- django-filter 25.1
- Pillow 10.4.0
- Python 3.13+

## Project Structure

```
backend/
├── dkbois_backend/          # Django project settings
│   ├── settings.py          # Main settings (CORS, REST framework, etc.)
│   ├── urls.py              # Main URL configuration
│   └── wsgi.py
├── portfolio/               # Main app
│   ├── models.py            # Database models
│   ├── serializers.py       # DRF serializers
│   ├── views.py             # API views and viewsets
│   ├── admin.py             # Django admin configuration
│   ├── urls.py              # App URL configuration
│   ├── templates/
│   │   └── portfolio/
│   │       └── admin_dashboard.html  # Custom dashboard
│   └── migrations/
├── manage.py
├── populate_data.py         # Data population script
├── requirements.txt
└── README.md
```

## Installation & Setup

### 1. Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2. Run Migrations

```bash
python manage.py migrate
```

### 3. Populate Initial Data

```bash
python populate_data.py
```

This script will populate the database with:
- 3 portfolio projects
- 4 services
- 3 testimonials
- 4 team members
- 4 timeline events
- 4 company values
- 3 FAQs

### 4. Create Superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

### 5. Run Development Server

```bash
python manage.py runserver
```

The server will start at `http://127.0.0.1:8000/`

## API Endpoints

All API endpoints support the `?lang=fr` or `?lang=en` query parameter for language selection (defaults to French).

### Projects
- `GET /api/projects/` - List all projects
  - Query params: `?category=kitchen`, `?type=creation`, `?material=oak`, `?featured=true`
- `GET /api/projects/{slug}/` - Get project details
- `GET /api/projects/featured/` - Get only featured projects

### Services
- `GET /api/services/` - List all services
- `GET /api/services/{slug}/` - Get service details

### Testimonials
- `GET /api/testimonials/` - List all testimonials

### Team
- `GET /api/team/` - List all team members

### Timeline
- `GET /api/timeline/` - List timeline events

### Company Values
- `GET /api/values/` - List company values

### FAQs
- `GET /api/faqs/` - List all FAQs

### Contact Submissions
- `POST /api/contact/` - Submit contact form
- `GET /api/contact/` - List submissions (admin only)

#### Contact Form POST Example

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

## Admin Interfaces

### Django Admin
Access the full Django admin interface at:
```
http://127.0.0.1:8000/admin/
```

Features:
- Full CRUD operations on all models
- Inline editing
- Filters and search
- Bilingual field editing
- List editable fields for quick updates

### Custom Admin Dashboard
Access the custom dashboard at:
```
http://127.0.0.1:8000/dashboard/
```

Features:
- Statistics overview
- Quick links to manage all content types
- Requires staff/superuser authentication

## Language Support

The API supports bilingual content (French/English). Add `?lang=en` to any API request to get English content:

```
GET /api/projects/?lang=en
GET /api/services/interior/?lang=fr
```

Default language is French (`fr`).

## Filtering & Search

### Projects
Filter by category, type, material, or featured status:
```
GET /api/projects/?category=kitchen&type=creation
GET /api/projects/?material=oak&featured=true
```

Search in titles:
```
GET /api/projects/?search=bibliotheque
```

Order by:
```
GET /api/projects/?ordering=order
GET /api/projects/?ordering=-created_at
```

## CORS Configuration

CORS is configured to allow requests from:
- http://localhost:3000
- http://localhost:5500
- http://localhost:8080
- http://127.0.0.1:3000
- http://127.0.0.1:5500
- http://127.0.0.1:8080

**Note:** `CORS_ALLOW_ALL_ORIGINS = True` is enabled in development. **Disable this in production** and specify exact origins.

## Database Schema

### Project Model
- Bilingual titles and descriptions
- Category (kitchen, living, exterior)
- Type (creation, restoration, fitting)
- Material (oak, walnut, maple)
- Specifications (duration, location, finish)
- Tags and images (JSON fields)
- Featured flag for homepage display

### Service Model
- Unique service ID
- Bilingual title and description
- Icon (Lucide icon name)
- Sub-services and process steps (JSON)
- Timeframe
- Multiple images

### Testimonial Model
- Client name and role
- Testimonial text
- Star rating (1-5)
- Display order

### TeamMember Model
- Name
- Bilingual role
- Experience years
- Bilingual quote
- Profile image

### TimelineEvent Model
- Year
- Bilingual title and description
- Display order

### CompanyValue Model
- Icon
- Bilingual title and description
- Display order

### FAQ Model
- Bilingual question and answer
- Active/inactive status
- Display order

### ContactSubmission Model
- Contact information (firstname, lastname, email, phone)
- Project details (type, budget, description)
- File uploads (JSON)
- GDPR consent
- Admin tracking (is_read, is_replied, notes)

## Frontend Integration

### Example: Fetch Projects with JavaScript

```javascript
// Fetch all projects (French)
fetch('http://127.0.0.1:8000/api/projects/?lang=fr')
  .then(res => res.json())
  .then(data => {
    console.log(data.results); // Array of projects
  });

// Fetch featured projects (English)
fetch('http://127.0.0.1:8000/api/projects/featured/?lang=en')
  .then(res => res.json())
  .then(data => {
    console.log(data); // Array of featured projects
  });

// Submit contact form
fetch('http://127.0.0.1:8000/api/contact/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    firstname: 'Jean',
    lastname: 'Dupont',
    email: 'jean@example.com',
    project_type: 'cabinetry',
    description: 'Project description',
    gdpr_consent: true
  })
})
.then(res => res.json())
.then(data => console.log('Success:', data));
```

## Production Deployment

### Security Checklist

1. **Disable Debug Mode**
   ```python
   # settings.py
   DEBUG = False
   ```

2. **Update Secret Key**
   ```python
   # settings.py
   SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
   ```

3. **Configure Allowed Hosts**
   ```python
   # settings.py
   ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
   ```

4. **Restrict CORS**
   ```python
   # settings.py
   CORS_ALLOW_ALL_ORIGINS = False
   CORS_ALLOWED_ORIGINS = [
       'https://yourdomain.com',
   ]
   ```

5. **Use PostgreSQL**
   ```python
   # settings.py
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'dkbois_db',
           'USER': 'your_db_user',
           'PASSWORD': 'your_db_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

6. **Collect Static Files**
   ```bash
   python manage.py collectstatic
   ```

7. **Use environment variables** for sensitive data (use python-decouple)

### Recommended Hosting
- **Backend**: Heroku, Railway, DigitalOcean, AWS
- **Database**: PostgreSQL (managed service)
- **Static files**: AWS S3, Cloudinary

## Troubleshooting

### Port already in use
```bash
# Use a different port
python manage.py runserver 8001
```

### Database locked (SQLite)
```bash
# Restart the server
# Or switch to PostgreSQL for production
```

### CORS errors
- Check `CORS_ALLOWED_ORIGINS` in settings.py
- Ensure `corsheaders` is in INSTALLED_APPS
- Ensure `CorsMiddleware` is in MIDDLEWARE

## Testing API Endpoints

Use the included API test script:

```bash
python test_api.py
```

Or use curl:

```bash
# Test projects endpoint
curl http://127.0.0.1:8000/api/projects/?lang=fr

# Test services endpoint
curl http://127.0.0.1:8000/api/services/

# Test contact submission
curl -X POST http://127.0.0.1:8000/api/contact/ \
  -H "Content-Type: application/json" \
  -d '{"firstname":"Test","lastname":"User","email":"test@example.com","project_type":"interior","description":"Test project","gdpr_consent":true}'
```

## Support & Documentation

- Django Documentation: https://docs.djangoproject.com/
- Django REST Framework: https://www.django-rest-framework.org/
- django-cors-headers: https://github.com/adamchainz/django-cors-headers

## License

This project is proprietary to DKbois.
