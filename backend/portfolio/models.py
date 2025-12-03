from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator


class Project(models.Model):
    """Portfolio project with bilingual content"""

    CATEGORY_CHOICES = [
        ('kitchen', 'Kitchen'),
        ('living', 'Living Room'),
        ('exterior', 'Exterior'),
    ]

    TYPE_CHOICES = [
        ('creation', 'Creation'),
        ('restoration', 'Restoration'),
        ('fitting', 'Fitting'),
    ]

    MATERIAL_CHOICES = [
        ('oak', 'Oak'),
        ('walnut', 'Walnut'),
        ('maple', 'Maple'),
    ]

    # Basic fields
    slug = models.SlugField(unique=True, max_length=200, blank=True)
    title_fr = models.CharField(max_length=200, verbose_name="Title (French)")
    title_en = models.CharField(max_length=200, verbose_name="Title (English)")

    # Classification
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    material = models.CharField(max_length=20, choices=MATERIAL_CHOICES)

    # Descriptions
    short_desc_fr = models.TextField(verbose_name="Short Description (French)")
    short_desc_en = models.TextField(verbose_name="Short Description (English)")
    full_desc_fr = models.TextField(verbose_name="Full Description (French)")
    full_desc_en = models.TextField(verbose_name="Full Description (English)")
    challenge_fr = models.TextField(verbose_name="Challenge (French)", blank=True)
    challenge_en = models.TextField(verbose_name="Challenge (English)", blank=True)

    # Specifications (stored as JSON)
    duration_fr = models.CharField(max_length=100, verbose_name="Duration (French)", blank=True)
    duration_en = models.CharField(max_length=100, verbose_name="Duration (English)", blank=True)
    location = models.CharField(max_length=200, blank=True)
    finish_fr = models.CharField(max_length=100, verbose_name="Finish (French)", blank=True)
    finish_en = models.CharField(max_length=100, verbose_name="Finish (English)", blank=True)

    # Tags and images (stored as JSON)
    tags = models.JSONField(default=list, blank=True, help_text="List of tags")
    images = models.JSONField(default=list, blank=True, help_text="List of image URLs")

    # Metadata
    featured = models.BooleanField(default=False, help_text="Display on homepage")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order = models.IntegerField(default=0, help_text="Display order")

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title_fr

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title_en or self.title_fr)
        super().save(*args, **kwargs)


class Service(models.Model):
    """Service offering with bilingual content"""

    slug = models.SlugField(unique=True, max_length=100, blank=True)
    service_id = models.CharField(max_length=50, unique=True, help_text="Unique identifier (e.g., 'interior')")
    icon = models.CharField(max_length=50, help_text="Lucide icon name")

    # Title and description
    title_fr = models.CharField(max_length=200, verbose_name="Title (French)")
    title_en = models.CharField(max_length=200, verbose_name="Title (English)")
    description_fr = models.TextField(verbose_name="Description (French)")
    description_en = models.TextField(verbose_name="Description (English)")

    # Detailed information
    sub_services = models.JSONField(default=list, blank=True, help_text="List of sub-services (bilingual)")
    process_steps = models.JSONField(default=list, blank=True, help_text="Process steps (bilingual)")
    timeframe_fr = models.CharField(max_length=100, verbose_name="Timeframe (French)", blank=True)
    timeframe_en = models.CharField(max_length=100, verbose_name="Timeframe (English)", blank=True)
    images = models.JSONField(default=list, blank=True, help_text="List of image URLs")

    # Display settings
    order = models.IntegerField(default=0, help_text="Display order")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'service_id']
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return self.title_fr

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.service_id)
        super().save(*args, **kwargs)


class Testimonial(models.Model):
    """Client testimonial"""

    name = models.CharField(max_length=100)
    role = models.CharField(max_length=200)
    text = models.TextField()
    stars = models.IntegerField(
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    image = models.URLField(blank=True, help_text="URL to client photo")

    # Display settings
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0, help_text="Display order")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"

    def __str__(self):
        return f"{self.name} - {self.stars} stars"


class TeamMember(models.Model):
    """Team member profile with bilingual content"""

    name = models.CharField(max_length=100)
    role_fr = models.CharField(max_length=200, verbose_name="Role (French)")
    role_en = models.CharField(max_length=200, verbose_name="Role (English)")
    experience_years = models.IntegerField(default=0, help_text="Years of experience")
    quote_fr = models.TextField(verbose_name="Quote (French)")
    quote_en = models.TextField(verbose_name="Quote (English)")
    image = models.URLField(blank=True, help_text="URL to team member photo")

    # Display settings
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0, help_text="Display order")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"

    def __str__(self):
        return self.name


class TimelineEvent(models.Model):
    """Company history timeline event with bilingual content"""

    year = models.CharField(max_length=10)
    title_fr = models.CharField(max_length=200, verbose_name="Title (French)")
    title_en = models.CharField(max_length=200, verbose_name="Title (English)")
    description_fr = models.TextField(verbose_name="Description (French)")
    description_en = models.TextField(verbose_name="Description (English)")

    # Display settings
    order = models.IntegerField(default=0, help_text="Display order")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['year', 'order']
        verbose_name = "Timeline Event"
        verbose_name_plural = "Timeline Events"

    def __str__(self):
        return f"{self.year} - {self.title_fr}"


class CompanyValue(models.Model):
    """Company core value with bilingual content"""

    icon = models.CharField(max_length=50, help_text="Lucide icon name")
    title_fr = models.CharField(max_length=200, verbose_name="Title (French)")
    title_en = models.CharField(max_length=200, verbose_name="Title (English)")
    description_fr = models.TextField(verbose_name="Description (French)")
    description_en = models.TextField(verbose_name="Description (English)")

    # Display settings
    order = models.IntegerField(default=0, help_text="Display order")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'title_fr']
        verbose_name = "Company Value"
        verbose_name_plural = "Company Values"

    def __str__(self):
        return self.title_fr


class FAQ(models.Model):
    """Frequently Asked Question with bilingual content"""

    question_fr = models.CharField(max_length=300, verbose_name="Question (French)")
    question_en = models.CharField(max_length=300, verbose_name="Question (English)")
    answer_fr = models.TextField(verbose_name="Answer (French)")
    answer_en = models.TextField(verbose_name="Answer (English)")

    # Display settings
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0, help_text="Display order")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'question_fr']
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

    def __str__(self):
        return self.question_fr


class ContactSubmission(models.Model):
    """Contact form submission"""

    PROJECT_TYPE_CHOICES = [
        ('interior', 'Interior Joinery'),
        ('cabinetry', 'Cabinetmaking'),
        ('restoration', 'Restoration'),
        ('fitting', 'Fitting'),
        ('other', 'Other'),
    ]

    # Contact information
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)

    # Project details
    project_type = models.CharField(max_length=20, choices=PROJECT_TYPE_CHOICES)
    description = models.TextField()

    # File uploads (stored as JSON list of URLs or file paths)
    files = models.JSONField(default=list, blank=True, help_text="List of uploaded file URLs")

    # GDPR consent
    gdpr_consent = models.BooleanField(default=False)

    # Status tracking
    is_read = models.BooleanField(default=False)
    is_replied = models.BooleanField(default=False)
    notes = models.TextField(blank=True, help_text="Admin notes")

    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Contact Submission"
        verbose_name_plural = "Contact Submissions"

    def __str__(self):
        return f"{self.firstname} {self.lastname} - {self.project_type} ({self.created_at.strftime('%Y-%m-%d')})"
