from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .models import (
    Project, Service, Testimonial, TeamMember,
    TimelineEvent, CompanyValue, FAQ, ContactSubmission
)
from .serializers import (
    ProjectListSerializer, ProjectDetailSerializer, ServiceSerializer,
    TestimonialSerializer, TeamMemberSerializer, TimelineEventSerializer,
    CompanyValueSerializer, FAQSerializer, ContactSubmissionSerializer
)


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for projects with filtering by category, type, and material.
    Provides list and detail views.
    """
    queryset = Project.objects.all()
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'type', 'material', 'featured']
    search_fields = ['title_fr', 'title_en', 'tags']
    ordering_fields = ['order', 'created_at']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProjectDetailSerializer
        return ProjectListSerializer

    def get_serializer_context(self):
        """Add language to serializer context"""
        context = super().get_serializer_context()
        # Get language from query params, default to French
        context['lang'] = self.request.query_params.get('lang', 'fr')
        return context

    @action(detail=False, methods=['get'])
    def featured(self, request):
        """Return only featured projects for homepage"""
        featured_projects = self.queryset.filter(featured=True)
        serializer = self.get_serializer(featured_projects, many=True)
        return Response(serializer.data)


class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for services.
    Read-only access to service information.
    """
    queryset = Service.objects.filter(is_active=True)
    serializer_class = ServiceSerializer
    lookup_field = 'slug'

    def get_serializer_context(self):
        """Add language to serializer context"""
        context = super().get_serializer_context()
        context['lang'] = self.request.query_params.get('lang', 'fr')
        return context


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
