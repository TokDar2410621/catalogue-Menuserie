"""
Script pour mettre à jour les données de DF Bois avec les informations du Cameroun
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dkbois_backend.settings')
django.setup()

from portfolio.models import Service, TeamMember, TimelineEvent, CompanyValue, FAQ, Project, Testimonial

print("🔄 Mise à jour des données pour DF Bois (Cameroun)...")

# 1. SERVICES
print("\n📦 Création des services...")
services_data = [
    {
        'slug': 'menuiserie',
        'icon': 'door-open',
        'title_fr': 'Menuiserie',
        'title_en': 'Carpentry',
        'description_fr': 'Fabrication et installation de portes, fenêtres, escaliers et tous travaux de menuiserie sur mesure.',
        'description_en': 'Manufacturing and installation of doors, windows, stairs and all custom carpentry work.',
        'order': 1,
        'is_active': True
    },
    {
        'slug': 'construction',
        'icon': 'hammer',
        'title_fr': 'Construction',
        'title_en': 'Construction',
        'description_fr': 'Construction de bâtiments résidentiels et commerciaux avec 25 ans d\'expérience.',
        'description_en': 'Construction of residential and commercial buildings with 25 years of experience.',
        'order': 2,
        'is_active': True
    },
    {
        'slug': 'renovation',
        'icon': 'wrench',
        'title_fr': 'Rénovation',
        'title_en': 'Renovation',
        'description_fr': 'Rénovation complète de maisons, bureaux et espaces commerciaux.',
        'description_en': 'Complete renovation of houses, offices and commercial spaces.',
        'order': 3,
        'is_active': True
    },
    {
        'slug': 'fabrication-meubles',
        'icon': 'gem',
        'title_fr': 'Fabrication de Meubles',
        'title_en': 'Furniture Manufacturing',
        'description_fr': 'Création de meubles sur mesure répondant aux besoins précis de nos clients.',
        'description_en': 'Creation of custom furniture meeting the precise needs of our clients.',
        'order': 4,
        'is_active': True
    }
]

for service_data in services_data:
    service, created = Service.objects.get_or_create(slug=service_data['slug'], defaults=service_data)
    if created:
        print(f"  ✅ Service créé: {service.title_fr}")

# 2. FONDATEUR / PROMOTEUR
print("\n👤 Création du profil du promoteur...")
mathurin = TeamMember.objects.create(
    name='Defehe Kamdem FOBHA Mathurin',
    role_fr='Fondateur et Promoteur',
    role_en='Founder and Promoter',
    years_experience=20,
    quote_fr='La satisfaction totale de la clientèle est la clé d\'un bon retour d\'expérience et du succès de l\'entreprise.',
    quote_en='Total customer satisfaction is the key to good feedback and business success.',
    bio_fr='Defehe Kamdem FOBHA Mathurin est le fondateur et promoteur de DF Bois. Formé dans le domaine de la menuiserie et de l\'ébénisterie, il a suivi des études secondaires techniques spécialisées qui lui ont permis d\'acquérir un solide savoir-faire. Fort de 20 ans d\'expérience, il met un point d\'honneur à atteindre la perfection dans chaque réalisation.\n\nAnimé par une véritable passion pour le bois, Mathurin s\'engage à fabriquer des articles sur mesure qui répondent aux besoins précis de ses clients, avec une finition impeccable et un travail durable. Sa motivation première est la satisfaction totale de la clientèle, qu\'il considère comme la clé d\'un bon retour d\'expérience et du succès de l\'entreprise.\n\nIl nourrit également une vision claire pour DF Bois : faire grandir l\'entreprise, créer des emplois et contribuer au bien-être de la communauté. Pour lui, le plaisir de servir et la qualité du travail sont au cœur de chaque projet entrepris.',
    bio_en='Defehe Kamdem FOBHA Mathurin is the founder and promoter of DF Bois. Trained in carpentry and cabinetry, he completed specialized technical secondary studies that allowed him to acquire solid expertise. With 20 years of experience, he makes it a point of honor to achieve perfection in each project.\n\nDriven by a true passion for wood, Mathurin is committed to manufacturing custom items that meet the precise needs of his clients, with impeccable finishing and durable work. His primary motivation is total customer satisfaction, which he considers the key to good feedback and business success.\n\nHe also nurtures a clear vision for DF Bois: to grow the company, create jobs, and contribute to the community\'s well-being. For him, the pleasure of serving and work quality are at the heart of every project undertaken.',
    order=1,
    is_active=True
)
print(f"  ✅ Promoteur créé: {mathurin.name}")

# 3. TIMELINE (Histoire de l'entreprise)
print("\n📅 Création de la timeline...")
timeline_data = [
    {
        'year': '1999',
        'title_fr': 'Les Débuts',
        'title_en': 'The Beginning',
        'description_fr': 'Defehe Kamdem FOBHA Mathurin commence sa formation en menuiserie et ébénisterie.',
        'description_en': 'Defehe Kamdem FOBHA Mathurin begins his training in carpentry and cabinetry.',
        'order': 1
    },
    {
        'year': '2004',
        'title_fr': 'Fondation de DF Bois',
        'title_en': 'DF Bois Foundation',
        'description_fr': 'Création officielle de DF Bois, spécialisée dans la menuiserie, la construction, la rénovation et la fabrication de meubles.',
        'description_en': 'Official creation of DF Bois, specialized in carpentry, construction, renovation and furniture manufacturing.',
        'order': 2
    },
    {
        'year': '2014',
        'title_fr': 'Expansion des Services',
        'title_en': 'Service Expansion',
        'description_fr': 'Élargissement de l\'offre avec des projets de construction et rénovation de plus grande envergure.',
        'description_en': 'Expansion of services with larger construction and renovation projects.',
        'order': 3
    },
    {
        'year': '2024',
        'title_fr': 'Vision d\'Avenir',
        'title_en': 'Vision for the Future',
        'description_fr': 'DF Bois poursuit sa croissance avec pour objectif de créer des emplois et contribuer au développement de la communauté camerounaise.',
        'description_en': 'DF Bois continues its growth with the goal of creating jobs and contributing to the development of the Cameroonian community.',
        'order': 4
    }
]

for event_data in timeline_data:
    event = TimelineEvent.objects.create(**event_data)
    print(f"  ✅ Événement créé: {event.year} - {event.title_fr}")

# 4. VALEURS DE L'ENTREPRISE
print("\n💎 Création des valeurs...")
values_data = [
    {
        'icon': 'check-circle',
        'title_fr': 'Qualité et Perfection',
        'title_en': 'Quality and Perfection',
        'description_fr': 'Un point d\'honneur à atteindre la perfection dans chaque réalisation avec une finition impeccable.',
        'description_en': 'A point of honor to achieve perfection in each project with impeccable finishing.',
        'order': 1
    },
    {
        'icon': 'heart',
        'title_fr': 'Satisfaction Client',
        'title_en': 'Customer Satisfaction',
        'description_fr': 'La satisfaction totale de la clientèle est notre priorité absolue.',
        'description_en': 'Total customer satisfaction is our absolute priority.',
        'order': 2
    },
    {
        'icon': 'users',
        'title_fr': 'Engagement Communautaire',
        'title_en': 'Community Engagement',
        'description_fr': 'Créer des emplois et contribuer au bien-être de la communauté camerounaise.',
        'description_en': 'Create jobs and contribute to the well-being of the Cameroonian community.',
        'order': 3
    },
    {
        'icon': 'award',
        'title_fr': 'Savoir-faire Traditionnel',
        'title_en': 'Traditional Expertise',
        'description_fr': '25 ans d\'expérience combinant savoir-faire traditionnel et exigence de qualité.',
        'description_en': '25 years of experience combining traditional expertise and quality requirements.',
        'order': 4
    }
]

for value_data in values_data:
    value = CompanyValue.objects.create(**value_data)
    print(f"  ✅ Valeur créée: {value.title_fr}")

# 5. FAQs
print("\n❓ Création des FAQs...")
faqs_data = [
    {
        'question_fr': 'Où est situé DF Bois ?',
        'question_en': 'Where is DF Bois located?',
        'answer_fr': 'DF Bois est basé au Cameroun et intervient sur tout le territoire national.',
        'answer_en': 'DF Bois is based in Cameroon and operates throughout the national territory.',
        'order': 1,
        'is_active': True
    },
    {
        'question_fr': 'Quels types de projets réalisez-vous ?',
        'question_en': 'What types of projects do you carry out?',
        'answer_fr': 'Nous réalisons des projets de menuiserie, construction, rénovation et fabrication de meubles sur mesure pour particuliers et professionnels.',
        'answer_en': 'We carry out carpentry, construction, renovation and custom furniture manufacturing projects for individuals and professionals.',
        'order': 2,
        'is_active': True
    },
    {
        'question_fr': 'Quels sont vos tarifs ?',
        'question_en': 'What are your rates?',
        'answer_fr': 'Nos tarifs varient selon la complexité du projet. Contactez-nous pour un devis gratuit et personnalisé en FCFA.',
        'answer_en': 'Our rates vary depending on the complexity of the project. Contact us for a free and personalized quote in FCFA.',
        'order': 3,
        'is_active': True
    },
    {
        'question_fr': 'Offrez-vous des garanties sur vos travaux ?',
        'question_en': 'Do you offer guarantees on your work?',
        'answer_fr': 'Oui, tous nos travaux sont garantis. La durée de garantie dépend du type de projet réalisé.',
        'answer_en': 'Yes, all our work is guaranteed. The warranty period depends on the type of project carried out.',
        'order': 4,
        'is_active': True
    }
]

for faq_data in faqs_data:
    faq = FAQ.objects.create(**faq_data)
    print(f"  ✅ FAQ créée: {faq.question_fr}")

print("\n✅ Mise à jour terminée!")
print(f"   - {Service.objects.count()} services")
print(f"   - {TeamMember.objects.count()} membre d'équipe")
print(f"   - {TimelineEvent.objects.count()} événements timeline")
print(f"   - {CompanyValue.objects.count()} valeurs")
print(f"   - {FAQ.objects.count()} FAQs")
