from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register viewsets
router = DefaultRouter()
router.register(r'projects', views.ProjectViewSet, basename='project')
router.register(r'services', views.ServiceViewSet, basename='service')
router.register(r'testimonials', views.TestimonialViewSet, basename='testimonial')
router.register(r'team', views.TeamMemberViewSet, basename='team')
router.register(r'timeline', views.TimelineEventViewSet, basename='timeline')
router.register(r'values', views.CompanyValueViewSet, basename='value')
router.register(r'faqs', views.FAQViewSet, basename='faq')
router.register(r'contact', views.ContactSubmissionViewSet, basename='contact')

# URL patterns
urlpatterns = [
    # API endpoints
    path('api/', include(router.urls)),

    # Authentication
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Admin dashboard
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
]
