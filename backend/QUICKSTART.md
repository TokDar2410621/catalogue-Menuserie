# DKbois Backend - Quick Start Guide

## Installation (5 minutes)

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

### 4. Create Admin User
```bash
python manage.py createsuperuser
```
Enter username, email, and password when prompted.

### 5. Start Server
```bash
python manage.py runserver
```

## Access Points

- **API Base**: http://127.0.0.1:8000/api/
- **Django Admin**: http://127.0.0.1:8000/admin/
- **Custom Dashboard**: http://127.0.0.1:8000/dashboard/

## Quick API Examples

### Get All Projects (French)
```
http://127.0.0.1:8000/api/projects/?lang=fr
```

### Get All Projects (English)
```
http://127.0.0.1:8000/api/projects/?lang=en
```

### Get Featured Projects
```
http://127.0.0.1:8000/api/projects/featured/
```

### Filter Projects by Category
```
http://127.0.0.1:8000/api/projects/?category=kitchen
```

### Get Services
```
http://127.0.0.1:8000/api/services/
```

### Get Testimonials
```
http://127.0.0.1:8000/api/testimonials/
```

### Submit Contact Form
```bash
curl -X POST http://127.0.0.1:8000/api/contact/ \
  -H "Content-Type: application/json" \
  -d '{
    "firstname": "Jean",
    "lastname": "Dupont",
    "email": "jean@example.com",
    "project_type": "cabinetry",
    "description": "Je souhaite un devis",
    "gdpr_consent": true
  }'
```

## All Available Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/projects/` | GET | List all projects |
| `/api/projects/{slug}/` | GET | Get project detail |
| `/api/projects/featured/` | GET | Get featured projects |
| `/api/services/` | GET | List all services |
| `/api/services/{slug}/` | GET | Get service detail |
| `/api/testimonials/` | GET | List testimonials |
| `/api/team/` | GET | List team members |
| `/api/timeline/` | GET | List timeline events |
| `/api/values/` | GET | List company values |
| `/api/faqs/` | GET | List FAQs |
| `/api/contact/` | POST | Submit contact form |
| `/api/contact/` | GET | List submissions (admin only) |

## Language Support

Add `?lang=fr` or `?lang=en` to any endpoint:
- French (default): `?lang=fr`
- English: `?lang=en`

Example:
```
http://127.0.0.1:8000/api/projects/?lang=en
```

## Filtering Projects

```
# By category
/api/projects/?category=kitchen
/api/projects/?category=living
/api/projects/?category=exterior

# By type
/api/projects/?type=creation
/api/projects/?type=restoration
/api/projects/?type=fitting

# By material
/api/projects/?material=oak
/api/projects/?material=walnut

# Combined filters
/api/projects/?category=kitchen&type=fitting&material=oak
```

## Testing

Run the test script:
```bash
python test_api.py
```

Or use curl:
```bash
curl http://127.0.0.1:8000/api/projects/
```

## Troubleshooting

### "No module named 'django'"
```bash
pip install -r requirements.txt
```

### "Table doesn't exist"
```bash
python manage.py migrate
```

### "No data showing"
```bash
python populate_data.py
```

### Server won't start
- Check if port 8000 is already in use
- Use a different port: `python manage.py runserver 8001`

## Next Steps

1. Read the full [README.md](README.md) for detailed documentation
2. Customize the admin interface in `portfolio/admin.py`
3. Add more data through Django admin
4. Integrate with your frontend

## File Structure

```
backend/
├── portfolio/           # Main app
│   ├── models.py       # Database models
│   ├── serializers.py  # API serializers
│   ├── views.py        # API views
│   ├── admin.py        # Admin configuration
│   └── urls.py         # URL routing
├── dkbois_backend/     # Project settings
│   └── settings.py     # Configuration
├── manage.py           # Django management
├── populate_data.py    # Data population script
├── test_api.py         # API testing script
└── db.sqlite3          # Database
```

## Support

For issues or questions, refer to:
- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- Full [README.md](README.md) in this directory
