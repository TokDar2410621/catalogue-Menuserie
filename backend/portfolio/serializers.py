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


class ProjectWriteSerializer(serializers.ModelSerializer):
    """Serializer for creating and updating projects"""

    class Meta:
        model = Project
        fields = [
            'slug', 'title_fr', 'title_en', 'category', 'type', 'material',
            'short_desc_fr', 'short_desc_en', 'full_desc_fr', 'full_desc_en',
            'challenge_fr', 'challenge_en', 'duration_fr', 'duration_en',
            'location', 'finish_fr', 'finish_en', 'tags', 'images',
            'featured', 'order'
        ]
        read_only_fields = []
        # Allow partial updates - all fields optional except title_fr
        extra_kwargs = {
            'title_en': {'required': False, 'allow_blank': True},
            'category': {'required': False, 'allow_blank': True},
            'type': {'required': False, 'allow_blank': True},
            'material': {'required': False, 'allow_blank': True},
            'short_desc_fr': {'required': False, 'allow_blank': True},
            'short_desc_en': {'required': False, 'allow_blank': True},
            'full_desc_fr': {'required': False, 'allow_blank': True},
            'full_desc_en': {'required': False, 'allow_blank': True},
            'slug': {'required': False, 'allow_blank': True},
        }

    def validate_slug(self, value):
        """Validate slug uniqueness on update"""
        # Skip validation for empty slug
        if not value:
            return value

        instance = self.instance
        if instance and Project.objects.exclude(pk=instance.pk).filter(slug=value).exists():
            raise serializers.ValidationError("A project with this slug already exists.")
        elif not instance and Project.objects.filter(slug=value).exists():
            raise serializers.ValidationError("A project with this slug already exists.")
        return value

    def create(self, validated_data):
        """Create a new project - slug auto-generated if not provided"""
        if not validated_data.get('slug'):
            # Slug will be auto-generated in model save()
            validated_data['slug'] = ''
        return super().create(validated_data)


class ServiceWriteSerializer(serializers.ModelSerializer):
    """Serializer for creating and updating services"""

    class Meta:
        model = Service
        fields = [
            'service_id', 'slug', 'icon', 'title_fr', 'title_en',
            'description_fr', 'description_en', 'sub_services',
            'process_steps', 'timeframe_fr', 'timeframe_en',
            'images', 'order', 'is_active'
        ]
        read_only_fields = []
        # Allow partial updates - all fields optional except title_fr
        extra_kwargs = {
            'service_id': {'required': False, 'allow_blank': True},
            'slug': {'required': False, 'allow_blank': True},
            'icon': {'required': False, 'allow_blank': True},
            'title_en': {'required': False, 'allow_blank': True},
            'description_fr': {'required': False, 'allow_blank': True},
            'description_en': {'required': False, 'allow_blank': True},
            'timeframe_fr': {'required': False, 'allow_blank': True},
            'timeframe_en': {'required': False, 'allow_blank': True},
        }

    def validate_slug(self, value):
        """Validate slug uniqueness on update"""
        # Skip validation for empty slug
        if not value:
            return value

        instance = self.instance
        if instance and Service.objects.exclude(pk=instance.pk).filter(slug=value).exists():
            raise serializers.ValidationError("A service with this slug already exists.")
        elif not instance and Service.objects.filter(slug=value).exists():
            raise serializers.ValidationError("A service with this slug already exists.")
        return value

    def validate_service_id(self, value):
        """Validate service_id uniqueness on update"""
        # Skip validation for empty service_id
        if not value:
            return value

        instance = self.instance
        if instance and Service.objects.exclude(pk=instance.pk).filter(service_id=value).exists():
            raise serializers.ValidationError("A service with this service_id already exists.")
        elif not instance and Service.objects.filter(service_id=value).exists():
            raise serializers.ValidationError("A service with this service_id already exists.")
        return value

    def create(self, validated_data):
        """Create a new service - slug auto-generated if not provided"""
        if not validated_data.get('slug'):
            # Slug will be auto-generated in model save()
            validated_data['slug'] = ''
        return super().create(validated_data)


class ContactSubmissionSerializer(serializers.ModelSerializer):
    """Serializer for contact form submissions"""

    class Meta:
        model = ContactSubmission
        fields = [
            'id', 'firstname', 'lastname', 'email', 'phone',
            'project_type', 'description', 'files',
            'gdpr_consent', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']

    def validate_gdpr_consent(self, value):
        """Ensure GDPR consent is given"""
        if not value:
            raise serializers.ValidationError("GDPR consent is required.")
        return value


class TeamMemberWriteSerializer(serializers.ModelSerializer):
    """Serializer for creating and updating team members"""

    # Add 'exp' as an alias for 'experience_years' for frontend compatibility
    exp = serializers.IntegerField(source='experience_years', required=False)

    class Meta:
        model = TeamMember
        fields = [
            'name', 'role_fr', 'role_en', 'exp',
            'quote_fr', 'quote_en', 'bio_fr', 'bio_en',
            'image', 'order', 'is_active'
        ]
        extra_kwargs = {
            'role_en': {'required': False, 'allow_blank': True},
            'quote_en': {'required': False, 'allow_blank': True},
            'bio_fr': {'required': False, 'allow_blank': True},
            'bio_en': {'required': False, 'allow_blank': True},
        }


class TimelineEventWriteSerializer(serializers.ModelSerializer):
    """Serializer for creating and updating timeline events"""

    # Add 'desc' as an alias for 'description' for frontend compatibility
    desc_fr = serializers.CharField(source='description_fr', required=False, allow_blank=True)
    desc_en = serializers.CharField(source='description_en', required=False, allow_blank=True)

    class Meta:
        model = TimelineEvent
        fields = [
            'year', 'title_fr', 'title_en',
            'desc_fr', 'desc_en', 'order'
        ]
        extra_kwargs = {
            'title_en': {'required': False, 'allow_blank': True},
        }


class CompanyValueWriteSerializer(serializers.ModelSerializer):
    """Serializer for creating and updating company values"""

    # Add 'desc' as an alias for 'description' for frontend compatibility
    desc_fr = serializers.CharField(source='description_fr', required=False, allow_blank=True)
    desc_en = serializers.CharField(source='description_en', required=False, allow_blank=True)

    class Meta:
        model = CompanyValue
        fields = [
            'icon', 'title_fr', 'title_en',
            'desc_fr', 'desc_en', 'order'
        ]
        extra_kwargs = {
            'title_en': {'required': False, 'allow_blank': True},
        }


class FAQWriteSerializer(serializers.ModelSerializer):
    """Serializer for creating and updating FAQs"""

    class Meta:
        model = FAQ
        fields = [
            'question_fr', 'question_en', 'answer_fr', 'answer_en',
            'category', 'order', 'is_active'
        ]
        extra_kwargs = {
            'question_en': {'required': False, 'allow_blank': True},
            'answer_en': {'required': False, 'allow_blank': True},
            'category': {'required': False, 'allow_blank': True},
        }
