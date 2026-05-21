# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**DKbois** — bilingual (FR/EN) portfolio site for a woodworking / cabinetry business.

Two halves:
- **Frontend** ([repo root](.)): static HTML + ES6 module JS, no build step. Tailwind/GSAP/Lucide via CDN. Deployed to Vercel (`catalogue-menuserie.vercel.app`).
- **Backend** ([backend/](backend/)): Django 5.1 + DRF, SQLite locally / PostgreSQL on Railway, Cloudinary for media uploads. Deployed to Railway (`carefree-heart-production-ec3a.up.railway.app`).

The two are connected via [api-config.js](api-config.js), which **auto-detects environment** (localhost → `http://localhost:3000/api`, otherwise → Railway URL). When adding new pages, do NOT hardcode the API base — import from [api-config.js](api-config.js).

## Running Locally

### Backend
```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
py -3.13 manage.py runserver 3000   # Windows w/ multiple Pythons; else: python manage.py runserver 3000
```

Port **must be 3000** — the frontend auto-detection in [api-config.js](api-config.js) assumes it.

Optional one-time data setup:
- `python populate_data.py` — sample bilingual content
- `python populate_real_data.py` — real DKbois content
- `python create_admin.py` — creates/resets superuser `admin` / `admin123` (also runs automatically on Railway via [backend/start.sh](backend/start.sh))

### Frontend
Any static server from the repo root (VS Code Live Server, `npx http-server -p 8080`). ES6 modules require HTTP, not `file://`.

### Access points (local)
- Frontend: whatever port your static server uses
- API: `http://localhost:3000/api/`
- Django admin: `http://localhost:3000/admin/`
- Custom Django dashboard: `http://localhost:3000/dashboard/` (login-required, separate from the static [admin.html](admin.html))

### Testing endpoints
- `python test_api.py` — basic GET smoke tests
- `python test_crud_api.py` — full CRUD coverage
- `python test_cloudinary.py` — verifies Cloudinary credentials in `.env`

## Architecture

### Frontend pages and pairing
Each page is `<name>.html` + `<name>.js`. JS uses ES6 modules and is imported with `type="module"`.

API-integrated pages (import [api-config.js](api-config.js)):
- [index.html](index.html) + [main.js](main.js) — services, featured projects, testimonials
- [admin.html](admin.html) + [admin.js](admin.js) — **standalone single-page admin app** that talks to the DRF endpoints (separate from Django's `/admin/`). Auth state is kept in `localStorage` under `adminToken`.

The remaining pages ([about](about.html), [services](services.html), [portfolio](portfolio.html), [project](project.html), [contact](contact.html), [mathurin-defehe](mathurin-defehe.html)) currently read from [data.js](data.js) — migration to the API is ongoing. Check the file's imports before assuming which source it uses.

Shared chrome lives in [navbar-component.js](navbar-component.js) and [footer-component.js](footer-component.js) (re-exported via [components.js](components.js)).

### Bilingual system
- **UI strings**: hardcoded in [data.js](data.js) under `translations.fr` / `translations.en`, applied via `data-i18n="key.path"` attributes. Every page implements `setupLanguage()` / `switchLanguage()`.
- **Content** (DB-backed): each model has `_fr` / `_en` field pairs. List/detail endpoints accept `?lang=fr|en` and serializers collapse to single-language output via context. Default `fr`.
- **Admin editing exception**: detail endpoints accept `?edit=true` which switches to the `*WriteSerializer`, returning ALL language fields. [admin.js](admin.js) relies on this. See `get_serializer_class` in [backend/portfolio/views.py](backend/portfolio/views.py).

Language is propagated via the `?lang=` URL parameter — keep this when generating links.

### Backend layout
Single app `portfolio` inside project `dkbois_backend`.

- [backend/portfolio/models.py](backend/portfolio/models.py) — 8 models: `Project`, `Service`, `Testimonial`, `TeamMember`, `TimelineEvent`, `CompanyValue`, `FAQ`, `ContactSubmission`. Bilingual fields are stored as `_fr`/`_en` columns; `tags`/`images`/`sub_services`/`process_steps` are `JSONField` lists.
- [backend/portfolio/views.py](backend/portfolio/views.py) — DRF `ModelViewSet` per model. All currently use `permission_classes = [AllowAny]` (intentional, with `TODO` comments). `ContactSubmission` is the only one that gates non-POST behind `IsAdminUser`. Plus standalone views: `upload_image` (POST `/api/upload/`), `login_view`, `logout_view`, `admin_dashboard`.
- [backend/portfolio/serializers.py](backend/portfolio/serializers.py) — paired `*Serializer` (read, single-lang via `context['lang']`) and `*WriteSerializer` (full bilingual fields).
- [backend/portfolio/urls.py](backend/portfolio/urls.py) — DRF router registers all viewsets under `/api/`.

### Endpoints
All resources except `testimonials` (read-only) and `contact` (POST-public, others admin) expose full CRUD:

```
GET|POST    /api/{projects|services|testimonials|team|timeline|values|faqs}/
GET|PUT|PATCH|DELETE  /api/projects/{slug}/        (lookup_field=slug)
GET|PUT|PATCH|DELETE  /api/services/{slug}/        (lookup_field=slug)
GET|PUT|PATCH|DELETE  /api/{team|timeline|values|faqs}/{id}/
GET         /api/projects/featured/                (custom action)
POST        /api/contact/                          (public; list/detail require admin)
POST        /api/upload/                           (multipart file upload, 5MB max, jpg/png/gif/webp)
```

Query params: `?lang=fr|en`, `?edit=true` (detail endpoints, see bilingual section above), and on `/api/services/` `?show_all=true` to include inactive services. Project list supports filters: `category`, `type`, `material`, `featured`, plus `search` on titles/tags.

### Media storage
- **Local dev**: Django default storage → `backend/media/`.
- **Production**: Cloudinary via `cloudinary_storage.storage.MediaCloudinaryStorage` (set in [settings.py](backend/dkbois_backend/settings.py) `STORAGES["default"]`). Static files always served by WhiteNoise.
- Cloudinary credentials come from `.env` (see [backend/.env.example](backend/.env.example) and [backend/CLOUDINARY_SETUP.md](backend/CLOUDINARY_SETUP.md)).

When working with image fields locally vs production, the URLs returned by `/api/upload/` differ — Cloudinary returns absolute URLs, the local file storage returns a relative path like `uploads/<filename>`.

### Configuration via environment
Driven entirely by env vars (with sensible local defaults baked into [backend/dkbois_backend/settings.py](backend/dkbois_backend/settings.py)):
- `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`
- `DATABASE_URL` — if present, switches to PostgreSQL via `dj_database_url`; else SQLite
- `CORS_ALLOWED_ORIGINS`, `CSRF_TRUSTED_ORIGINS` — comma-separated. Trailing slashes are stripped automatically by the list comprehensions in settings.py — there was a real bug from this (commit `fc3ab77`)
- `CLOUDINARY_CLOUD_NAME` / `CLOUDINARY_API_KEY` / `CLOUDINARY_API_SECRET`
- `CORS_ALLOW_ALL_ORIGINS = DEBUG`, so when `DEBUG=False` the explicit allowlist is enforced.

### Deployment specifics
- **Backend (Railway)**: [backend/Procfile](backend/Procfile) → [backend/start.sh](backend/start.sh) runs `migrate`, `collectstatic`, `create_admin.py`, then `gunicorn`. The `create_admin.py` script **deletes and recreates** the `admin` superuser on every boot with password `admin123` — do not store other data under that user.
- **Frontend (Vercel/Netlify)**: zero-build static deploy. [_redirects](_redirects) handles SPA-style fallbacks on Netlify.

## Styling system

Tailwind via CDN, with a per-page inline `tailwind.config` `<script>`. Custom palette repeated across HTML files:
- `oak` #8B4513, `walnut` #3E2723 (main text), `maple` #F5DEB3, `offwhite` #FAF9F6, `forest` #2F5233, `gold` #D4AF37
- `font-serif` = Playfair Display (headings), `font-sans` = Lato (body)

[styles.css](styles.css) holds keyframes, hover effects, navbar underline animation, custom scrollbar. GSAP + ScrollTrigger drive reveal animations (`.animate-up`, `.reveal-section`).

Images use a custom `IntersectionObserver` lazy loader: set `class="lazy"` and `data-src="…"`, the `lazyLoadImages()` helper swaps `data-src` → `src` when in view.

## Patterns to follow when changing things

- **Adding a model field**: edit [models.py](backend/portfolio/models.py) → `makemigrations` → `migrate` → add to BOTH the read serializer AND the `*WriteSerializer` in [serializers.py](backend/portfolio/serializers.py). The admin UI ([admin.js](admin.js)) consumes the write serializer via `?edit=true` and will silently drop unknown fields.
- **New bilingual UI string**: add to both `fr` and `en` blocks in [data.js](data.js) `translations`, then use `data-i18n="path.to.key"` in HTML. The string is applied on `setupLanguage()` and re-applied on `switchLanguage()`.
- **New API consumer in JS**: import `{ API }` from `./api-config.js` — don't write new `fetch` calls or hardcode the base URL. Add a new resource block to [api-config.js](api-config.js) if you're hitting a new endpoint.
- **CORS / CSRF issues in production**: check that the env-var list in Railway has no trailing slashes (the settings code strips them but the symptom is confusing — see commit `fc3ab77`).
- **Resetting prod admin password**: re-run [backend/create_admin.py](backend/create_admin.py) on Railway, or let the next deploy do it (start.sh runs it on every boot).

## Reference docs in repo

- [INTEGRATION.md](INTEGRATION.md) — frontend↔API migration tracker (status notes may lag behind code; verify against imports)
- [DEPLOIEMENT_RESUME.md](DEPLOIEMENT_RESUME.md), [NETLIFY_DEPLOYMENT.md](NETLIFY_DEPLOYMENT.md), [backend/DEPLOYMENT.md](backend/DEPLOYMENT.md) — deployment walkthroughs (FR)
- [backend/README.md](backend/README.md), [backend/QUICKSTART.md](backend/QUICKSTART.md), [backend/API_ENDPOINTS.md](backend/API_ENDPOINTS.md)
- [backend/CRUD_API_GUIDE.md](backend/CRUD_API_GUIDE.md), [backend/CRUD_IMPLEMENTATION_SUMMARY.md](backend/CRUD_IMPLEMENTATION_SUMMARY.md) — CRUD endpoint reference
- [backend/CLOUDINARY_SETUP.md](backend/CLOUDINARY_SETUP.md)
