from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.core.files.storage import default_storage
from django.conf import settings
from django.utils import timezone
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
import os
from pathlib import Path

from .models import (
    Project, Service, Testimonial, TeamMember,
    TimelineEvent, CompanyValue, FAQ, ContactSubmission
)
from .serializers import (
    ProjectListSerializer, ProjectDetailSerializer, ProjectWriteSerializer,
    ServiceSerializer, ServiceWriteSerializer,
    TestimonialSerializer, TeamMemberSerializer, TeamMemberWriteSerializer,
    TimelineEventSerializer, TimelineEventWriteSerializer,
    CompanyValueSerializer, CompanyValueWriteSerializer,
    FAQSerializer, FAQWriteSerializer, ContactSubmissionSerializer
)


class ProjectViewSet(viewsets.ModelViewSet):
    """
    ViewSet for projects with full CRUD operations.
    Supports filtering by category, type, and material.

    NOTE: Currently allows all operations for development.
    TODO: Add authentication and permissions for production:
          - GET endpoints: Public access
          - POST/PUT/PATCH/DELETE: Require authentication (IsAuthenticated or IsAdminUser)
    """
    queryset = Project.objects.all()
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'type', 'material', 'featured']
    search_fields = ['title_fr', 'title_en', 'tags']
    ordering_fields = ['order', 'created_at']

    # Allow all operations for development - CHANGE THIS FOR PRODUCTION
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        """Return appropriate serializer based on action"""
        if self.action in ['create', 'update', 'partial_update']:
            return ProjectWriteSerializer
        elif self.action == 'retrieve':
            # Use write serializer for admin editing (returns all language fields)
            if self.request.query_params.get('edit') == 'true':
                return ProjectWriteSerializer
            return ProjectDetailSerializer
        return ProjectListSerializer

    def get_serializer_context(self):
        """Add language to serializer context"""
        context = super().get_serializer_context()
        # Get language from query params, default to French
        context['lang'] = self.request.query_params.get('lang', 'fr')
        return context

    def create(self, request, *args, **kwargs):
        """Create a new project"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {'message': 'Project created successfully', 'data': serializer.data},
            status=status.HTTP_201_CREATED,
            headers=headers
        )

    def update(self, request, *args, **kwargs):
        """Update a project (full update)"""
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            'message': 'Project updated successfully',
            'data': serializer.data
        })

    def destroy(self, request, *args, **kwargs):
        """Delete a project"""
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {'message': 'Project deleted successfully'},
            status=status.HTTP_204_NO_CONTENT
        )

    @action(detail=False, methods=['get'])
    def featured(self, request):
        """Return only featured projects for homepage"""
        featured_projects = self.queryset.filter(featured=True)
        serializer = self.get_serializer(featured_projects, many=True)
        return Response(serializer.data)


class ServiceViewSet(viewsets.ModelViewSet):
    """
    ViewSet for services with full CRUD operations.

    NOTE: Currently allows all operations for development.
    TODO: Add authentication and permissions for production:
          - GET endpoints: Public access
          - POST/PUT/PATCH/DELETE: Require authentication (IsAuthenticated or IsAdminUser)
    """
    queryset = Service.objects.all()  # Show all services for admin, filter on frontend if needed
    lookup_field = 'slug'

    # Allow all operations for development - CHANGE THIS FOR PRODUCTION
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        """Return appropriate serializer based on action"""
        if self.action in ['create', 'update', 'partial_update']:
            return ServiceWriteSerializer
        # Use write serializer for admin editing (returns all language fields)
        if self.action == 'retrieve' and self.request.query_params.get('edit') == 'true':
            return ServiceWriteSerializer
        return ServiceSerializer

    def get_serializer_context(self):
        """Add language to serializer context"""
        context = super().get_serializer_context()
        context['lang'] = self.request.query_params.get('lang', 'fr')
        return context

    def get_queryset(self):
        """Filter active services for public list view, show all for admin operations"""
        queryset = super().get_queryset()
        # Only filter for list view, not for create/update/delete
        if self.action == 'list':
            # Check if request wants all services (for admin interface)
            show_all = self.request.query_params.get('show_all', 'false').lower() == 'true'
            if not show_all:
                queryset = queryset.filter(is_active=True)
        return queryset

    def create(self, request, *args, **kwargs):
        """Create a new service"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {'message': 'Service created successfully', 'data': serializer.data},
            status=status.HTTP_201_CREATED,
            headers=headers
        )

    def update(self, request, *args, **kwargs):
        """Update a service (full update)"""
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            'message': 'Service updated successfully',
            'data': serializer.data
        })

    def destroy(self, request, *args, **kwargs):
        """Delete a service"""
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {'message': 'Service deleted successfully'},
            status=status.HTTP_204_NO_CONTENT
        )


class TestimonialViewSet(viewsets.ModelViewSet):
    """
    ViewSet for testimonials with full CRUD operations.
    Returns active testimonials only (new testimonials default to is_active=True).

    NOTE: Currently allows all operations for development.
    TODO: Gate POST/PUT/PATCH/DELETE behind IsAdminUser for production.
    """
    queryset = Testimonial.objects.filter(is_active=True)
    serializer_class = TestimonialSerializer
    permission_classes = [AllowAny]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['lang'] = self.request.query_params.get('lang', 'fr')
        return context


class TeamMemberViewSet(viewsets.ModelViewSet):
    """
    ViewSet for team members with full CRUD operations.
    """
    queryset = TeamMember.objects.all()  # Show all for admin
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        """Return appropriate serializer based on action"""
        if self.action in ['create', 'update', 'partial_update']:
            return TeamMemberWriteSerializer
        # Use write serializer for admin editing (returns all language fields)
        if self.action == 'retrieve' and self.request.query_params.get('edit') == 'true':
            return TeamMemberWriteSerializer
        return TeamMemberSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['lang'] = self.request.query_params.get('lang', 'fr')
        return context


class TimelineEventViewSet(viewsets.ModelViewSet):
    """
    ViewSet for timeline events with full CRUD operations.
    """
    queryset = TimelineEvent.objects.all()
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        """Return appropriate serializer based on action"""
        if self.action in ['create', 'update', 'partial_update']:
            return TimelineEventWriteSerializer
        # Use write serializer for admin editing (returns all language fields)
        if self.action == 'retrieve' and self.request.query_params.get('edit') == 'true':
            return TimelineEventWriteSerializer
        return TimelineEventSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['lang'] = self.request.query_params.get('lang', 'fr')
        return context


class CompanyValueViewSet(viewsets.ModelViewSet):
    """
    ViewSet for company values with full CRUD operations.
    """
    queryset = CompanyValue.objects.all()
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        """Return appropriate serializer based on action"""
        if self.action in ['create', 'update', 'partial_update']:
            return CompanyValueWriteSerializer
        # Use write serializer for admin editing (returns all language fields)
        if self.action == 'retrieve' and self.request.query_params.get('edit') == 'true':
            return CompanyValueWriteSerializer
        return CompanyValueSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['lang'] = self.request.query_params.get('lang', 'fr')
        return context


class FAQViewSet(viewsets.ModelViewSet):
    """
    ViewSet for FAQs with full CRUD operations.
    """
    queryset = FAQ.objects.all()  # Show all for admin
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        """Return appropriate serializer based on action"""
        if self.action in ['create', 'update', 'partial_update']:
            return FAQWriteSerializer
        # Use write serializer for admin editing (returns all language fields)
        if self.action == 'retrieve' and self.request.query_params.get('edit') == 'true':
            return FAQWriteSerializer
        return FAQSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['lang'] = self.request.query_params.get('lang', 'fr')
        return context


class ContactSubmissionViewSet(viewsets.ModelViewSet):
    """
    ViewSet for contact form submissions.
    POST allowed for everyone, other methods require admin access.
    """
    queryset = ContactSubmission.objects.all()
    serializer_class = ContactSubmissionSerializer

    def get_permissions(self):
        """Allow POST for everyone, other methods for admin only"""
        if self.action == 'create':
            return [AllowAny()]
        return [IsAdminUser()]

    def create(self, request, *args, **kwargs):
        """Create a new contact submission"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {'message': 'Contact submission received successfully', 'data': serializer.data},
            status=status.HTTP_201_CREATED,
            headers=headers
        )


# Custom Admin Dashboard Views
def is_staff_user(user):
    """Check if user is staff"""
    return user.is_staff


@login_required
@user_passes_test(is_staff_user)
def admin_dashboard(request):
    """Admin dashboard home page"""
    context = {
        'projects_count': Project.objects.count(),
        'services_count': Service.objects.count(),
        'testimonials_count': Testimonial.objects.count(),
        'contact_submissions_count': ContactSubmission.objects.count(),
        'unread_contacts': ContactSubmission.objects.filter(is_read=False).count(),
    }
    return render(request, 'portfolio/admin_dashboard.html', context)


def login_view(request):
    """Custom login view"""
    if request.user.is_authenticated:
        return redirect('admin_dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            next_url = request.POST.get('next') or request.GET.get('next') or 'admin_dashboard'
            return redirect(next_url)
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')

    return render(request, 'portfolio/login.html')


def logout_view(request):
    """Custom logout view"""
    auth_logout(request)
    messages.success(request, 'Vous avez été déconnecté avec succès.')
    return redirect('login')


@api_view(['POST'])
def upload_image(request):
    """
    Upload an image file and return its URL.
    Accepts multipart/form-data with a 'file' field.
    """
    if 'file' not in request.FILES:
        return Response(
            {'error': 'No file provided'},
            status=status.HTTP_400_BAD_REQUEST
        )

    uploaded_file = request.FILES['file']

    # Validate file extension
    allowed_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.webp']
    file_ext = os.path.splitext(uploaded_file.name)[1].lower()

    if file_ext not in allowed_extensions:
        return Response(
            {'error': f'Invalid file type. Allowed: {", ".join(allowed_extensions)}'},
            status=status.HTTP_400_BAD_REQUEST
        )

    # Validate file size (max 5MB)
    max_size = 5 * 1024 * 1024  # 5MB in bytes
    if uploaded_file.size > max_size:
        return Response(
            {'error': 'File too large. Maximum size is 5MB'},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        # Create upload directory if it doesn't exist
        upload_dir = 'uploads'
        full_upload_path = os.path.join(settings.MEDIA_ROOT, upload_dir)
        os.makedirs(full_upload_path, exist_ok=True)

        # Generate unique filename
        import uuid
        from datetime import datetime
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        unique_filename = f"{timestamp}_{uuid.uuid4().hex[:8]}{file_ext}"

        # Save file
        file_path = os.path.join(upload_dir, unique_filename)
        saved_path = default_storage.save(file_path, uploaded_file)

        # Build absolute URL so frontend works regardless of storage backend
        # (Cloudinary in prod returns https://res.cloudinary.com/...,
        # local FileSystemStorage returns /media/uploads/...).
        storage_url = default_storage.url(saved_path)
        if storage_url.startswith('http://') or storage_url.startswith('https://'):
            file_url = storage_url
        else:
            file_url = request.build_absolute_uri(storage_url)

        return Response({
            'url': file_url,
            'filename': unique_filename,
            'size': uploaded_file.size
        }, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response(
            {'error': f'Failed to upload file: {str(e)}'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


# Static frontend pages: (path, changefreq, priority).
# path '' is the homepage. These mirror the real .html files at the site root.
SITEMAP_STATIC_PAGES = [
    ('', 'weekly', '1.0'),
    ('about.html', 'monthly', '0.8'),
    ('services.html', 'monthly', '0.9'),
    ('portfolio.html', 'weekly', '0.9'),
    ('contact.html', 'monthly', '0.8'),
    ('mathurin-defehe.html', 'monthly', '0.7'),
]


def sitemap_view(request):
    """
    Dynamic XML sitemap generated from the database.

    Lists the static frontend pages plus one URL per project detail page
    (project.html?id=<slug>), so newly published projects appear in the
    sitemap automatically with a content-driven <lastmod>.

    Served at /sitemap.xml on this backend. The frontend domain proxies
    /sitemap.xml to this endpoint (see vercel.json) so crawlers fetch it
    from https://fdkbois.com/sitemap.xml — same host as the listed URLs.

    FRONTEND_URL must be the canonical host. Vercel canonicalises to the
    apex (www.fdkbois.com 307-redirects to fdkbois.com), so the default and
    every <loc>/hreflang use the apex to avoid listing redirecting URLs.
    """
    frontend = os.environ.get('FRONTEND_URL', 'https://fdkbois.com').rstrip('/')

    # Only list projects with a usable slug; a blank slug would yield
    # project.html?id= which the frontend renders as a "project not found"
    # soft-404 (project.js). Blank slugs are possible via the admin write path.
    projects = list(Project.objects.exclude(slug='').exclude(slug__isnull=True))
    services = list(Service.objects.filter(is_active=True))

    now = timezone.now()
    project_lastmods = [p.updated_at for p in projects if p.updated_at]
    service_lastmods = [s.updated_at for s in services if s.updated_at]
    projects_lastmod = max(project_lastmods) if project_lastmods else now
    services_lastmod = max(service_lastmods) if service_lastmods else now
    site_lastmod = max(projects_lastmod, services_lastmod)

    # Per-page lastmod: portfolio tracks projects, services tracks services,
    # everything else tracks the most recent content change site-wide.
    page_lastmods = {
        'portfolio.html': projects_lastmod,
        'services.html': services_lastmod,
    }

    def build_entry(path, lastmod, changefreq, priority):
        base = f"{frontend}/{path}"
        sep = '&' if '?' in path else '?'
        return {
            'loc': base,
            'loc_fr': f"{base}{sep}lang=fr",
            'loc_en': f"{base}{sep}lang=en",
            'lastmod': lastmod.strftime('%Y-%m-%d'),
            'changefreq': changefreq,
            'priority': priority,
        }

    urls = [
        build_entry(path, page_lastmods.get(path, site_lastmod), changefreq, priority)
        for path, changefreq, priority in SITEMAP_STATIC_PAGES
    ]

    for project in projects:
        urls.append(build_entry(
            f"project.html?id={project.slug}",
            project.updated_at or now,
            'monthly',
            '0.7',
        ))

    return render(
        request,
        'portfolio/sitemap.xml',
        {'urls': urls},
        content_type='application/xml',
    )
