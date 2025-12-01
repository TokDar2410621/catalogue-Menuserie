from rest_framework import serializers
from .models import (
    Project, Service, Testimonial, TeamMember,
    TimelineEvent, CompanyValue, FAQ, ContactSubmission
)


class ProjectListSerializer(serializers.ModelSerializer):
    """Serializer for project list view"""

    title = serializers.SerializerMethodField()
    short_desc = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            'id', 'slug', 'title', 'category', 'type', 'material',
            'short_desc', 'tags', 'images', 'featured', 'order'
        ]

    def get_title(self, obj):
        """Return title based on language context"""
        lang = self.context.get('lang', 'fr')
        return obj.title_fr if lang == 'fr' else obj.title_en

    def get_short_desc(self, obj):
        """Return short description based on language context"""
        lang = self.context.get('lang', 'fr')
        return obj.short_desc_fr if lang == 'fr' else obj.short_desc_en


class ProjectDetailSerializer(serializers.ModelSerializer):
    """Serializer for project detail view"""

    title = serializers.SerializerMethodField()
    short_desc = serializers.SerializerMethodField()
    full_desc = serializers.SerializerMethodField()
    challenge = serializers.SerializerMethodField()
    specs = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            'id', 'slug', 'title', 'category', 'type', 'material',
            'short_desc', 'full_desc', 'challenge', 'specs',
            'tags', 'images', 'featured', 'created_at', 'updated_at'
        ]

    def get_title(self, obj):
        lang = self.context.get('lang', 'fr')
        return obj.title_fr if lang == 'fr' else obj.title_en

    def get_short_desc(self, obj):
        lang = self.context.get('lang', 'fr')
        return obj.short_desc_fr if lang == 'fr' else obj.short_desc_en

    def get_full_desc(self, obj):
        lang = self.context.get('lang', 'fr')
        return obj.full_desc_fr if lang == 'fr' else obj.full_desc_en

    def get_challenge(self, obj):
        lang = self.context.get('lang', 'fr')
        return obj.challenge_fr if lang == 'fr' else obj.challenge_en

    def get_specs(self, obj):
        """Return specifications object based on language"""
        lang = self.context.get('lang', 'fr')
        return {
            'duration': obj.duration_fr if lang == 'fr' else obj.duration_en,
            'location': obj.location,
            'finish': obj.finish_fr if lang == 'fr' else obj.finish_en,
        }


class ServiceSerializer(serializers.ModelSerializer):
    """Serializer for services"""

    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    timeframe = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = [
            'id', 'service_id', 'slug', 'icon', 'title', 'description',
            'sub_services', 'process_steps', 'timeframe', 'images',
            'order', 'is_active'
        ]

    def get_title(self, obj):
        lang = self.context.get('lang', 'fr')
        return obj.title_fr if lang == 'fr' else obj.title_en

    def get_description(self, obj):
        lang = self.context.get('lang', 'fr')
        return obj.description_fr if lang == 'fr' else obj.description_en

    def get_timeframe(self, obj):
        lang = self.context.get('lang', 'fr')
        return obj.timeframe_fr if lang == 'fr' else obj.timeframe_en


class TestimonialSerializer(serializers.ModelSerializer):
    """Serializer for testimonials"""

    class Meta:
        model = Testimonial
        fields = ['id', 'name', 'role', 'text', 'stars', 'image', 'order']


class TeamMemberSerializer(serializers.ModelSerializer):
    """Serializer for team members"""

    role = serializers.SerializerMethodField()
    quote = serializers.SerializerMethodField()

    class Meta:
        model = TeamMember
        fields = ['id', 'name', 'role', 'experience_years', 'quote', 'image', 'order']

    def get_role(self, obj):
        lang = self.context.get('lang', 'fr')
        return obj.role_fr if lang == 'fr' else obj.role_en

    def get_quote(self, obj):
        lang = self.context.get('lang', 'fr')
        return obj.quote_fr if lang == 'fr' else obj.quote_en


class TimelineEventSerializer(serializers.ModelSerializer):
    """Serializer for timeline events"""

    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = TimelineEvent
        fields = ['id', 'year', 'title', 'description', 'order']

    def get_title(self, obj):
        lang = self.context.get('lang', 'fr')
        return obj.title_fr if lang == 'fr' else obj.title_en

    def get_description(self, obj):
        lang = self.context.get('lang', 'fr')
        return obj.description_fr if lang == 'fr' else obj.description_en


class CompanyValueSerializer(serializers.ModelSerializer):
    """Serializer for company values"""

    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = CompanyValue
        fields = ['id', 'icon', 'title', 'description', 'order']

    def get_title(self, obj):
        lang = self.context.get('lang', 'fr')
        return obj.title_fr if lang == 'fr' else obj.title_en

    def get_description(self, obj):
        lang = self.context.get('lang', 'fr')
        return obj.description_fr if lang == 'fr' else obj.description_en


class FAQSerializer(serializers.ModelSerializer):
    """Serializer for FAQs"""

    question = serializers.SerializerMethodField()
    answer = serializers.SerializerMethodField()

    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer', 'order']

    def get_question(self, obj):
        lang = self.context.get('lang', 'fr')
        return obj.question_fr if lang == 'fr' else obj.question_en

    def get_answer(self, obj):
        lang = self.context.get('lang', 'fr')
        return obj.answer_fr if lang == 'fr' else obj.answer_en


class ContactSubmissionSerializer(serializers.ModelSerializer):
    """Serializer for contact form submissions"""

    class Meta:
        model = ContactSubmission
        fields = [
            'id', 'firstname', 'lastname', 'email', 'phone',
            'project_type', 'budget', 'description', 'files',
            'gdpr_consent', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']

    def validate_gdpr_consent(self, value):
        """Ensure GDPR consent is given"""
        if not value:
            raise serializers.ValidationError("GDPR consent is required.")
        return value
