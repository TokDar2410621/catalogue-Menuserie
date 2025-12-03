from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.core.files.storage import default_storage
from django.conf import settings
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
    TestimonialSerializer, TeamMemberSerializer, TimelineEventSerializer,
    CompanyValueSerializer, FAQSerializer, ContactSubmissionSerializer
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


class TestimonialViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for testimonials.
    Returns active testimonials only.
    """
    queryset = Testimonial.objects.filter(is_active=True)
    serializer_class = TestimonialSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['lang'] = self.request.query_params.get('lang', 'fr')
        return context


class TeamMemberViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for team members.
    Returns active team members only.
    """
    queryset = TeamMember.objects.filter(is_active=True)
    serializer_class = TeamMemberSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['lang'] = self.request.query_params.get('lang', 'fr')
        return context


class TimelineEventViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for timeline events.
    Shows company history.
    """
    queryset = TimelineEvent.objects.all()
    serializer_class = TimelineEventSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['lang'] = self.request.query_params.get('lang', 'fr')
        return context


class CompanyValueViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for company values.
    """
    queryset = CompanyValue.objects.all()
    serializer_class = CompanyValueSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['lang'] = self.request.query_params.get('lang', 'fr')
        return context


class FAQViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for FAQs.
    Returns active FAQs only.
    """
    queryset = FAQ.objects.filter(is_active=True)
    serializer_class = FAQSerializer

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

        # Return relative URL (without /media/ prefix as frontend expects)
        file_url = saved_path.replace('\\', '/')

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
