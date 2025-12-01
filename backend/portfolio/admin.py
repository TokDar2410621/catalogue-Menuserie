from django.contrib import admin
from .models import (
    Project, Service, Testimonial, TeamMember,
    TimelineEvent, CompanyValue, FAQ, ContactSubmission
)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title_fr', 'category', 'type', 'material', 'featured', 'order', 'created_at']
    list_filter = ['category', 'type', 'material', 'featured']
    search_fields = ['title_fr', 'title_en', 'short_desc_fr', 'short_desc_en']
    prepopulated_fields = {'slug': ('title_en',)}
    list_editable = ['featured', 'order']
    ordering = ['order', '-created_at']

    fieldsets = (
        ('Basic Information', {
            'fields': ('slug', 'title_fr', 'title_en', 'category', 'type', 'material')
        }),
        ('Descriptions', {
            'fields': ('short_desc_fr', 'short_desc_en', 'full_desc_fr', 'full_desc_en', 'challenge_fr', 'challenge_en')
        }),
        ('Specifications', {
            'fields': ('duration_fr', 'duration_en', 'location', 'finish_fr', 'finish_en')
        }),
        ('Media & Tags', {
            'fields': ('tags', 'images')
        }),
        ('Display Settings', {
            'fields': ('featured', 'order')
        }),
    )


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title_fr', 'service_id', 'icon', 'is_active', 'order']
    list_filter = ['is_active']
    search_fields = ['title_fr', 'title_en', 'service_id']
    prepopulated_fields = {'slug': ('service_id',)}
    list_editable = ['is_active', 'order']
    ordering = ['order']

    fieldsets = (
        ('Basic Information', {
            'fields': ('service_id', 'slug', 'icon', 'title_fr', 'title_en')
        }),
        ('Description', {
            'fields': ('description_fr', 'description_en')
        }),
        ('Details', {
            'fields': ('sub_services', 'process_steps', 'timeframe_fr', 'timeframe_en', 'images')
        }),
        ('Display Settings', {
            'fields': ('is_active', 'order')
        }),
    )


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'stars', 'is_active', 'order', 'created_at']
    list_filter = ['is_active', 'stars']
    search_fields = ['name', 'role', 'text']
    list_editable = ['is_active', 'order']
    ordering = ['order', '-created_at']


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'role_fr', 'experience_years', 'is_active', 'order']
    list_filter = ['is_active']
    search_fields = ['name', 'role_fr', 'role_en']
    list_editable = ['is_active', 'order']
    ordering = ['order', 'name']

    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'role_fr', 'role_en', 'experience_years', 'image')
        }),
        ('Quote', {
            'fields': ('quote_fr', 'quote_en')
        }),
        ('Display Settings', {
            'fields': ('is_active', 'order')
        }),
    )


@admin.register(TimelineEvent)
class TimelineEventAdmin(admin.ModelAdmin):
    list_display = ['year', 'title_fr', 'order']
    search_fields = ['year', 'title_fr', 'title_en']
    list_editable = ['order']
    ordering = ['year', 'order']

    fieldsets = (
        ('Event Information', {
            'fields': ('year', 'title_fr', 'title_en', 'description_fr', 'description_en')
        }),
        ('Display Settings', {
            'fields': ('order',)
        }),
    )


@admin.register(CompanyValue)
class CompanyValueAdmin(admin.ModelAdmin):
    list_display = ['title_fr', 'icon', 'order']
    search_fields = ['title_fr', 'title_en']
    list_editable = ['order']
    ordering = ['order']

    fieldsets = (
        ('Value Information', {
            'fields': ('icon', 'title_fr', 'title_en', 'description_fr', 'description_en')
        }),
        ('Display Settings', {
            'fields': ('order',)
        }),
    )


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['question_fr', 'is_active', 'order']
    list_filter = ['is_active']
    search_fields = ['question_fr', 'question_en', 'answer_fr', 'answer_en']
    list_editable = ['is_active', 'order']
    ordering = ['order']

    fieldsets = (
        ('Question & Answer', {
            'fields': ('question_fr', 'question_en', 'answer_fr', 'answer_en')
        }),
        ('Display Settings', {
            'fields': ('is_active', 'order')
        }),
    )


@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'project_type', 'budget', 'is_read', 'is_replied', 'created_at']
    list_filter = ['is_read', 'is_replied', 'project_type', 'budget', 'created_at']
    search_fields = ['firstname', 'lastname', 'email', 'description']
    list_editable = ['is_read', 'is_replied']
    readonly_fields = ['firstname', 'lastname', 'email', 'phone', 'project_type', 'budget', 'description', 'files', 'gdpr_consent', 'created_at']
    ordering = ['-created_at']

    fieldsets = (
        ('Contact Information', {
            'fields': ('firstname', 'lastname', 'email', 'phone', 'created_at')
        }),
        ('Project Details', {
            'fields': ('project_type', 'budget', 'description', 'files')
        }),
        ('Admin', {
            'fields': ('is_read', 'is_replied', 'notes', 'gdpr_consent')
        }),
    )

    def full_name(self, obj):
        return f"{obj.firstname} {obj.lastname}"
    full_name.short_description = 'Name'

    def has_add_permission(self, request):
        # Don't allow manual addition of contact submissions
        return False
