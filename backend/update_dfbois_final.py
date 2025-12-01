import os
import sys
import django

# Setup Django
sys.path.append(r'C:\Users\Darius\Desktop\catalogue Menuserie\backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dkbois_backend.settings')
django.setup()

from portfolio.models import Service, TeamMember, TimelineEvent, CompanyValue, FAQ

print("Mise a jour des donnees DF Bois...")

# Services
print("Mise a jour des services...")
Service.objects.update_or_create(
    service_id='menuiserie',
    defaults={
        'slug': 'menuiserie',
        'icon': 'door-open',
        'title_fr': 'Menuiserie',
        'title_en': 'Carpentry',
        'description_fr': 'Fabrication et installation de portes, fenetres, escaliers et tous travaux de menuiserie sur mesure.',
        'description_en': 'Manufacturing and installation of doors, windows, stairs and all custom carpentry work.',
        'order': 1,
        'is_active': True
    }
)

Service.objects.update_or_create(
    service_id='construction',
    defaults={
        'slug': 'construction',
        'icon': 'hammer',
        'title_fr': 'Construction',
        'title_en': 'Construction',
        'description_fr': 'Construction de batiments residentiels et commerciaux avec 25 ans d\'experience.',
        'description_en': 'Construction of residential and commercial buildings with 25 years of experience.',
        'order': 2,
        'is_active': True
    }
)

Service.objects.update_or_create(
    service_id='renovation',
    defaults={
        'slug': 'renovation',
        'icon': 'wrench',
        'title_fr': 'Renovation',
        'title_en': 'Renovation',
        'description_fr': 'Renovation complete de maisons, bureaux et espaces commerciaux.',
        'description_en': 'Complete renovation of houses, offices and commercial spaces.',
        'order': 3,
        'is_active': True
    }
)

Service.objects.update_or_create(
    service_id='fabrication-meubles',
    defaults={
        'slug': 'fabrication-meubles',
        'icon': 'gem',
        'title_fr': 'Fabrication de Meubles',
        'title_en': 'Furniture Manufacturing',
        'description_fr': 'Creation de meubles sur mesure repondant aux besoins precis de nos clients.',
        'description_en': 'Creation of custom furniture meeting the precise needs of our clients.',
        'order': 4,
        'is_active': True
    }
)

# Supprimer les anciens services qui ne sont plus utilises
Service.objects.exclude(service_id__in=['menuiserie', 'construction', 'renovation', 'fabrication-meubles']).delete()

# Team Member
print("Mise a jour de l'equipe...")
TeamMember.objects.all().delete()
TeamMember.objects.create(
    name='Defehe Kamdem FOBHA Mathurin',
    role_fr='Fondateur et Promoteur',
    role_en='Founder and Promoter',
    experience_years=20,
    quote_fr='La satisfaction totale de la clientele est la cle d\'un bon retour d\'experience et du succes de l\'entreprise.',
    quote_en='Total customer satisfaction is the key to good feedback and business success.',
    order=1,
    is_active=True
)

# Timeline
print("Mise a jour de la timeline...")
TimelineEvent.objects.all().delete()
TimelineEvent.objects.create(
    year='1999',
    title_fr='Les Debuts',
    title_en='The Beginning',
    description_fr='Defehe Kamdem FOBHA Mathurin commence sa formation en menuiserie et ebenisterie.',
    description_en='Defehe Kamdem FOBHA Mathurin begins his training in carpentry and cabinetry.',
    order=1
)

TimelineEvent.objects.create(
    year='2004',
    title_fr='Fondation de DF Bois',
    title_en='DF Bois Foundation',
    description_fr='Creation officielle de DF Bois, specialisee dans la menuiserie, la construction, la renovation et la fabrication de meubles.',
    description_en='Official creation of DF Bois, specialized in carpentry, construction, renovation and furniture manufacturing.',
    order=2
)

TimelineEvent.objects.create(
    year='2014',
    title_fr='Expansion des Services',
    title_en='Service Expansion',
    description_fr='Elargissement de l\'offre avec des projets de construction et renovation de plus grande envergure.',
    description_en='Expansion of services with larger construction and renovation projects.',
    order=3
)

TimelineEvent.objects.create(
    year='2024',
    title_fr='Vision d\'Avenir',
    title_en='Vision for the Future',
    description_fr='DF Bois poursuit sa croissance avec pour objectif de creer des emplois et contribuer au developpement de la communaute camerounaise.',
    description_en='DF Bois continues its growth with the goal of creating jobs and contributing to the development of the Cameroonian community.',
    order=4
)

# Company Values
print("Mise a jour des valeurs...")
CompanyValue.objects.all().delete()
CompanyValue.objects.create(
    icon='check-circle',
    title_fr='Qualite et Perfection',
    title_en='Quality and Perfection',
    description_fr='Un point d\'honneur a atteindre la perfection dans chaque realisation avec une finition impeccable.',
    description_en='A point of honor to achieve perfection in each project with impeccable finishing.',
    order=1
)

CompanyValue.objects.create(
    icon='heart',
    title_fr='Satisfaction Client',
    title_en='Customer Satisfaction',
    description_fr='La satisfaction totale de la clientele est notre priorite absolue.',
    description_en='Total customer satisfaction is our absolute priority.',
    order=2
)

CompanyValue.objects.create(
    icon='users',
    title_fr='Engagement Communautaire',
    title_en='Community Engagement',
    description_fr='Creer des emplois et contribuer au bien-etre de la communaute camerounaise.',
    description_en='Create jobs and contribute to the well-being of the Cameroonian community.',
    order=3
)

CompanyValue.objects.create(
    icon='award',
    title_fr='Savoir-faire Traditionnel',
    title_en='Traditional Expertise',
    description_fr='25 ans d\'experience combinant savoir-faire traditionnel et exigence de qualite.',
    description_en='25 years of experience combining traditional expertise and quality requirements.',
    order=4
)

# FAQs
print("Mise a jour des FAQs...")
FAQ.objects.all().delete()
FAQ.objects.create(
    question_fr='Ou est situe DF Bois ?',
    question_en='Where is DF Bois located?',
    answer_fr='DF Bois est base au Cameroun et intervient sur tout le territoire national.',
    answer_en='DF Bois is based in Cameroon and operates throughout the national territory.',
    order=1,
    is_active=True
)

FAQ.objects.create(
    question_fr='Quels types de projets realisez-vous ?',
    question_en='What types of projects do you carry out?',
    answer_fr='Nous realisons des projets de menuiserie, construction, renovation et fabrication de meubles sur mesure pour particuliers et professionnels.',
    answer_en='We carry out carpentry, construction, renovation and custom furniture manufacturing projects for individuals and professionals.',
    order=2,
    is_active=True
)

FAQ.objects.create(
    question_fr='Quels sont vos tarifs ?',
    question_en='What are your rates?',
    answer_fr='Nos tarifs varient selon la complexite du projet. Contactez-nous pour un devis gratuit et personnalise en FCFA.',
    answer_en='Our rates vary depending on the complexity of the project. Contact us for a free and personalized quote in FCFA.',
    order=3,
    is_active=True
)

print("\n=== MISE A JOUR TERMINEE ===")
print(f"Services: {Service.objects.count()}")
print(f"Equipe: {TeamMember.objects.count()}")
print(f"Timeline: {TimelineEvent.objects.count()}")
print(f"Valeurs: {CompanyValue.objects.count()}")
print(f"FAQs: {FAQ.objects.count()}")
