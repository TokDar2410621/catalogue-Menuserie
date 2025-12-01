# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**DKbois** - A bilingual (French/English) portfolio website for a woodworking and cabinetry business.

**Architecture:** Full-stack application with:
- **Frontend:** Static HTML/CSS/JS with ES6 modules (no build process)
- **Backend:** Django REST API with SQLite database
- **Integration:** Hybrid approach - homepage uses API, other pages transitioning from static data

## Running the Site

### Backend (Django REST API)

**Windows (Python 3.13):**
```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python populate_data.py  # Optional: populate sample data
python manage.py createsuperuser  # Create admin account
py -3.13 manage.py runserver 3000  # Run on port 3000
```

**Other Systems:**
```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python populate_data.py
python manage.py createsuperuser
python manage.py runserver 3000
```

**Access Points:**
- API: http://localhost:3000/api/
- Django Admin: http://localhost:3000/admin/
- Custom Dashboard: http://localhost:3000/dashboard/

**Common Commands:**
- `python manage.py makemigrations` - Create new migrations after model changes
- `python manage.py migrate` - Apply migrations
- `python manage.py shell` - Open Django shell
- `python test_api.py` - Test API endpoints
- `python update_data_simple.py` - Update/sync data (run from backend directory)

### Frontend (Static Website)

- **Local Development:** Use any local server (e.g., VS Code Live Server extension, `npx http-server`)
- **No build step required:** All dependencies loaded via CDN
- **ES6 modules:** Requires local server (can't use file:// protocol)

## Architecture

### Hybrid Data Architecture (In Transition)

**Current State:** The project is transitioning from static data to API-driven content:

**Static Data ([data.js](data.js)):**
- `translations` - UI strings still used by all pages for interface text
- Legacy data structures for pages not yet migrated

**API Data ([api-config.js](api-config.js)):**
- Centralized API client with functions for all endpoints
- Base URL: `http://localhost:3000/api`
- All endpoints support `?lang=fr` or `?lang=en` parameter
- Used by [main.js](main.js) (homepage) for dynamic content

**Migration Status:**
- ✅ **Homepage ([main.js](main.js)):** Fully integrated with API (services, featured projects, testimonials)
- 🔄 **Other pages:** Still using [data.js](data.js), migration pending

### Backend API Structure

**Location:** `backend/` directory

**Tech Stack:**
- Django 5.1.7
- Django REST Framework 3.15.2
- django-cors-headers 4.7.0
- django-filter 25.1
- Pillow 10.4.0
- SQLite database (can upgrade to PostgreSQL)

**Key Files:**
- `backend/portfolio/models.py` - Database models
- `backend/portfolio/serializers.py` - DRF serializers
- `backend/portfolio/views.py` - API viewsets and views
- `backend/portfolio/admin.py` - Django admin configuration
- `backend/dkbois_backend/settings.py` - Project settings (CORS, allowed hosts)

**Available Endpoints:**
- `GET /api/projects/` - List projects (supports filters: category, type, material, featured, search)
- `GET /api/projects/featured/` - Featured projects only
- `GET /api/projects/{slug}/` - Project detail
- `GET /api/services/` - List services
- `GET /api/services/{slug}/` - Service detail
- `GET /api/testimonials/` - List testimonials
- `GET /api/team/` - Team members
- `GET /api/timeline/` - Timeline events
- `GET /api/values/` - Company values
- `GET /api/faqs/` - FAQs
- `POST /api/contact/` - Submit contact form
- `GET /api/contact/` - List submissions (admin only)

**CORS Configuration:**
- Development: Allows localhost:3000, localhost:5500, localhost:8080, 127.0.0.1 variants
- **Production:** Must update `CORS_ALLOWED_ORIGINS` in settings.py

### Frontend Page Structure

**Two Implementation Patterns:**

**1. API-Powered Pages** (using [api-config.js](api-config.js)):
- [index.html](index.html) + [main.js](main.js) - Homepage
  - Imports both [data.js](data.js) (for translations) and [api-config.js](api-config.js) (for content)
  - Fetches services, featured projects, testimonials from API
  - Re-renders content on language switch
  - Example: `await API.services.list(currentLang)`

**2. Static Data Pages** (using [data.js](data.js)):
- [about.html](about.html) + [about.js](about.js) - Company history, team, values, timeline
- [services.html](services.html) + [services.js](services.js) - Service descriptions with process steps
- [portfolio.html](portfolio.html) + [portfolio.js](portfolio.js) - Filterable project gallery
- [project.html](project.html) + [project.js](project.js) - Project detail pages (`?id=` URL param)
- [contact.html](contact.html) + [contact.js](contact.js) - Contact form and FAQs

**Common Pattern for All Pages:**
- HTML has `data-i18n` attributes for translatable UI text
- JS implements `setupLanguage()` and `switchLanguage()`
- Language parameter propagated via URL (`?lang=fr` or `?lang=en`)
- Mobile menu, navbar scroll behavior, GSAP animations

### Language System

Language is managed via URL parameters (`?lang=fr` or `?lang=en`):
- Default language is French (`fr`)
- Falls back to browser language if supported
- All translatable elements use `data-i18n="key.path"` attributes
- `setupLanguage()` in each JS file initializes translation on page load
- `switchLanguage()` toggles between languages and updates URL

When adding new translatable content:
1. Add keys to both `fr` and `en` sections in [data.js](data.js) `translations` object
2. Use `data-i18n="your.key.path"` in HTML

### Styling System

Uses **Tailwind CSS** (loaded via CDN) with custom configuration in `<script>` tags within each HTML file:

Custom colors defined:
- `oak` - #8B4513 (primary brown)
- `walnut` - #3E2723 (dark brown, main text)
- `maple` - #F5DEB3 (light wood)
- `offwhite` - #FAF9F6 (backgrounds)
- `forest` - #2F5233 (green accent)
- `gold` - #D4AF37 (premium accent)

Custom fonts:
- `font-serif` - Playfair Display (headings)
- `font-sans` - Lato (body text)

[styles.css](styles.css) contains:
- Animation keyframes
- Custom hover effects for cards and portfolio items
- Navigation underline animations
- Custom scrollbar styling
- Parallax helpers

### Animations

Uses **GSAP** with ScrollTrigger plugin:
- Hero section parallax backgrounds
- Fade-in animations for sections on scroll
- Staggered card animations
- Element reveals on viewport entry

Common animation classes:
- `.animate-up` - Initial hero animations with delays
- `.reveal-section` - Sections that animate on scroll
- Service/portfolio cards have stagger animations

### Image Handling

All images use lazy loading via IntersectionObserver:
- Images have `data-src` attribute and `lazy` class
- `lazyLoadImages()` function swaps `data-src` to `src` when in viewport
- Placeholder background color while loading
- 200px rootMargin for early loading

## Common Development Tasks

### Backend Development

#### Adding a New Portfolio Project via Django Admin
1. Start backend: `cd backend && py -3.13 manage.py runserver 3000`
2. Access admin: http://localhost:3000/admin/
3. Navigate to Projects → Add Project
4. Fill in bilingual fields (title_fr, title_en, description_fr, etc.)
5. Set category, type, material, featured status
6. Add images, tags (JSON format)
7. Slug auto-generated from title

#### Modifying Database Models
1. Edit `backend/portfolio/models.py`
2. Create migration: `python manage.py makemigrations`
3. Review migration file in `backend/portfolio/migrations/`
4. Apply migration: `python manage.py migrate`
5. Update serializers in `backend/portfolio/serializers.py` if needed
6. Test with `python test_api.py`

#### Adding a New API Endpoint
1. Add method to viewset in `backend/portfolio/views.py`
2. Add route in `backend/portfolio/urls.py` if needed
3. Add function to [api-config.js](api-config.js) for frontend access
4. Test endpoint with curl or `python test_api.py`

#### Syncing Data Between data.js and Database
Use the update script to sync static data to database:
```bash
cd backend
python update_data_simple.py
```

### Frontend Development

#### Migrating a Page from Static to API
1. Import [api-config.js](api-config.js) in page JS file
2. Replace data.js imports with API calls (see [main.js](main.js) as example)
3. Update render functions to use API data structure
4. Handle async loading and errors
5. Ensure language switching triggers re-fetch

Example:
```javascript
import { API } from './api-config.js';

const renderServices = async () => {
    const response = await API.services.list(currentLang);
    const services = response.results || response;
    // render services...
};
```

#### Adding a New Service (Static - Legacy)

1. Add to `servicesData` in [data.js](data.js)
2. Add translations to `translations.fr.services` and `translations.en.services`
3. For detailed service page, add to `detailedServicesData`

*Note: Prefer adding via Django Admin once page is migrated to API*

#### Modifying UI Translations

Edit [data.js](data.js) `translations` object. All pages use this for UI strings.

#### Adding Pages

1. Copy structure from existing page HTML (header, footer, navigation)
2. Create corresponding `.js` file with language setup
3. Decide: static data or API-powered (import [data.js](data.js) or [api-config.js](api-config.js))
4. Update navigation links in all HTML files

## External Dependencies (CDN)

- **Tailwind CSS:** https://cdn.tailwindcss.com
- **GSAP:** https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/
- **Lucide Icons:** https://unpkg.com/lucide@latest
- **Google Fonts:** Playfair Display, Lato

All dependencies are loaded in `<head>` of each HTML file.

## Navigation and Mobile Menu

Each page includes:
- Fixed header with logo, nav links, language toggle, CTA button
- Mobile menu overlay (slides in from right)
- Navbar shrinks on scroll (`h-24` → `h-20`)
- Active page indicated with `.active` class and gold underline

Mobile menu is controlled by:
- `#mobile-menu-btn` - Opens menu
- `#close-menu-btn` - Closes menu
- `.mobile-link` clicks - Auto-close menu

## Forms

[contact.html](contact.html) has a contact form with:
- Form fields: firstname, lastname, email, phone, project_type, budget, description, file upload
- Form validation (HTML5 `required` attributes)
- GDPR checkbox
- **API Integration Available:** `POST /api/contact/` endpoint ready
- Submissions viewable in Django Admin at http://localhost:3000/admin/portfolio/contactsubmission/

To integrate contact form with API:
```javascript
import { API } from './api-config.js';

const handleSubmit = async (formData) => {
    try {
        const response = await API.contact.submit(formData);
        // Show success message
    } catch (error) {
        // Show error message
    }
};
```

## Integration Status & Documentation

See [INTEGRATION.md](INTEGRATION.md) for current API integration progress and next steps.

**Backend Documentation:**
- [backend/README.md](backend/README.md) - Complete API documentation
- [backend/QUICKSTART.md](backend/QUICKSTART.md) - Quick setup guide
- [backend/API_ENDPOINTS.md](backend/API_ENDPOINTS.md) - Endpoint reference (if exists)

## Development Workflow

### Working with Both Frontend and Backend

**Typical Development Setup:**
1. Terminal 1: Run Django backend
   ```bash
   cd backend
   py -3.13 manage.py runserver 3000
   ```

2. Terminal 2: Run frontend dev server
   ```bash
   # From project root, use VS Code Live Server or:
   npx http-server -p 8080
   ```

3. Access:
   - Frontend: http://localhost:8080 (or Live Server port)
   - Backend API: http://localhost:3000/api/
   - Django Admin: http://localhost:3000/admin/

**Content Management:**
- Add/edit content via Django Admin (http://localhost:3000/admin/)
- Changes immediately reflected in API responses
- API-powered pages (like homepage) update automatically
- Static pages require migration to see API changes

**Debugging API Issues:**
- Check browser console for fetch errors
- Verify CORS settings in `backend/dkbois_backend/settings.py`
- Test endpoints directly: `curl http://localhost:3000/api/projects/?lang=fr`
- Use `python test_api.py` for automated endpoint testing

### Data Management Strategy

**For New Content:**
1. Add via Django Admin (preferred for API-integrated pages)
2. Content automatically available via API
3. Update [data.js](data.js) if static pages need it (temporary until migration)

**For UI Text/Translations:**
- Continue using [data.js](data.js) `translations` object
- All pages depend on this for interface text
- Backend models handle content translations (title_fr/en, description_fr/en)

## Browser Support

Modern browsers only (ES6 modules, IntersectionObserver, CSS Grid). No transpilation or polyfills included.

## Deployment Notes

**Frontend:** Can deploy to any static host (Netlify, Vercel, GitHub Pages)

**Backend:**
- Update `DEBUG = False` in settings.py
- Set `SECRET_KEY` via environment variable
- Configure `ALLOWED_HOSTS`
- Restrict `CORS_ALLOWED_ORIGINS` to production domain
- Use PostgreSQL instead of SQLite
- Run `python manage.py collectstatic`
- See [backend/README.md](backend/README.md) for full production checklist
