"""
Script pour mettre à jour le contenu DKbois dans la base de données
Contenu adapté de l'entreprise DF Bois camerounaise
"""
import os
import sys
import django

# Configuration Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SECRET_KEY', 'django-insecure-dev-key-for-local-only')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dkbois_backend.settings')
django.setup()

from portfolio.models import Service, TeamMember, TimelineEvent, CompanyValue

def update_company_description():
    """Met à jour la description de l'entreprise dans les services"""
    print("\n[DESCRIPTION] Mise a jour de la description de l'entreprise...")

    # Vérifier si un service "À propos" existe, sinon le créer
    about_service, created = Service.objects.get_or_create(
        service_id='about-company',
        defaults={
            'slug': 'a-propos-dkbois',
            'title_fr': 'À propos de DKbois',
            'title_en': 'About DKbois',
            'icon': 'info',
            'is_active': True
        }
    )

    about_service.description_fr = """DKbois est une entreprise spécialisée dans la menuiserie, la construction, la rénovation et la fabrication de meubles. Forte de 25 ans d'expérience, notre société s'appuie sur un savoir-faire traditionnel allié à une grande exigence dans la qualité de la finition.

Chez DKbois, le respect des délais de livraison est une priorité, tout comme la satisfaction de nos clients. Nous mettons un point d'honneur à réaliser chaque projet avec soin, rigueur et professionnalisme, pour offrir des solutions sur mesure qui correspondent parfaitement aux attentes.

Qu'il s'agisse de rénovations, de créations personnalisées ou de constructions neuves, DKbois s'engage à accompagner ses clients à chaque étape, en garantissant un travail durable et esthétique."""

    about_service.description_en = """DKbois is a company specialized in joinery, construction, renovation and furniture manufacturing. With 25 years of experience, our company relies on traditional know-how combined with high standards in finishing quality.

At DKbois, respecting delivery deadlines is a priority, as is customer satisfaction. We take pride in completing each project with care, rigor and professionalism, to offer tailor-made solutions that perfectly match expectations.

Whether it's renovations, personalized creations or new constructions, DKbois is committed to supporting its clients at every stage, guaranteeing durable and aesthetic work."""

    about_service.save()
    print(f"  [OK] Description de l'entreprise mise a jour")

def create_founder_profile():
    """Crée ou met à jour le profil du fondateur"""
    print("\n[FONDATEUR] Creation/mise a jour du profil du fondateur...")

    # Créer ou mettre à jour le profil du fondateur
    founder, created = TeamMember.objects.get_or_create(
        name='Defehe Kamdem FOBHA Mathurin',
        defaults={
            'experience_years': 20,
            'image': 'image/founder-placeholder.jpg'
        }
    )

    founder.role_fr = 'Fondateur et Promoteur'
    founder.role_en = 'Founder and Promoter'
    founder.quote_fr = 'La passion du bois et la satisfaction du client sont au cœur de chaque réalisation'
    founder.quote_en = 'Passion for wood and customer satisfaction are at the heart of every project'
    founder.bio_fr = """Defehe Kamdem FOBHA Mathurin est le fondateur et promoteur de DKbois. Formé dans le domaine de la menuiserie et de l'ébénisterie, il a suivi des études secondaires techniques spécialisées qui lui ont permis d'acquérir un solide savoir-faire. Fort de 20 ans d'expérience, il met un point d'honneur à atteindre la perfection dans chaque réalisation.

Animé par une véritable passion pour le bois, Mathurin s'engage à fabriquer des articles sur mesure qui répondent aux besoins précis de ses clients, avec une finition impeccable et un travail durable. Sa motivation première est la satisfaction totale de la clientèle, qu'il considère comme la clé d'un bon retour d'expérience et du succès de l'entreprise."""

    founder.bio_en = """Defehe Kamdem FOBHA Mathurin is the founder and promoter of DKbois. Trained in the field of joinery and cabinetmaking, he completed specialized technical secondary studies that allowed him to acquire solid expertise. With 20 years of experience, he makes it a point of honor to achieve perfection in every project.

Driven by a true passion for wood, Mathurin is committed to manufacturing custom-made items that meet the precise needs of his clients, with impeccable finishing and durable work. His primary motivation is total customer satisfaction, which he considers the key to good feedback and the company's success."""

    founder.save()

    action = "cree" if created else "mis a jour"
    print(f"  [OK] Profil du fondateur {action}: {founder.name}")

def update_company_values():
    """Met à jour les valeurs de l'entreprise"""
    print("\n[VALEURS] Mise a jour des valeurs de l'entreprise...")

    values_data = [
        {
            'icon': 'award',
            'title_fr': 'Excellence & Qualité',
            'title_en': 'Excellence & Quality',
            'description_fr': 'Un savoir-faire traditionnel de 25 ans allié à une exigence sans compromis dans la qualité de finition de chaque projet.',
            'description_en': '25 years of traditional expertise combined with uncompromising quality standards in every project finish.',
            'order': 1
        },
        {
            'icon': 'clock',
            'title_fr': 'Respect des Délais',
            'title_en': 'Deadline Compliance',
            'description_fr': 'Le respect des délais de livraison est notre priorité absolue pour assurer votre satisfaction.',
            'description_en': 'Meeting delivery deadlines is our top priority to ensure your satisfaction.',
            'order': 2
        },
        {
            'icon': 'users',
            'title_fr': 'Satisfaction Client',
            'title_en': 'Customer Satisfaction',
            'description_fr': 'Chaque projet est réalisé avec soin, rigueur et professionnalisme pour répondre parfaitement à vos attentes.',
            'description_en': 'Each project is completed with care, rigor and professionalism to perfectly meet your expectations.',
            'order': 3
        },
        {
            'icon': 'leaf',
            'title_fr': 'Durabilité',
            'title_en': 'Sustainability',
            'description_fr': 'Un travail durable et esthétique qui résiste à l\'épreuve du temps.',
            'description_en': 'Durable and aesthetic work that stands the test of time.',
            'order': 4
        }
    ]

    for value_data in values_data:
        value, created = CompanyValue.objects.update_or_create(
            title_fr=value_data['title_fr'],
            defaults=value_data
        )
        action = "creee" if created else "mise a jour"
        print(f"  [OK] Valeur {action}: {value.title_fr}")

def update_timeline():
    """Met à jour la chronologie de l'entreprise"""
    print("\n[CHRONOLOGIE] Mise a jour de la chronologie...")

    timeline_data = [
        {
            'year': 1999,
            'title_fr': 'Les Débuts',
            'title_en': 'The Beginning',
            'description_fr': 'Defehe Kamdem FOBHA Mathurin commence son parcours dans la menuiserie après sa formation technique spécialisée.',
            'description_en': 'Defehe Kamdem FOBHA Mathurin begins his journey in joinery after his specialized technical training.',
            'order': 1
        },
        {
            'year': 2005,
            'title_fr': 'Fondation de DKbois',
            'title_en': 'Foundation of DKbois',
            'description_fr': 'Création de DKbois, entreprise spécialisée dans la menuiserie, la construction et la fabrication de meubles sur mesure.',
            'description_en': 'Creation of DKbois, a company specialized in joinery, construction and custom furniture manufacturing.',
            'order': 2
        },
        {
            'year': 2015,
            'title_fr': 'Expansion des Services',
            'title_en': 'Service Expansion',
            'description_fr': 'Élargissement de l\'offre pour inclure la rénovation et les créations personnalisées de grande envergure.',
            'description_en': 'Expansion of services to include renovation and large-scale custom creations.',
            'order': 3
        },
        {
            'year': 2024,
            'title_fr': 'Excellence Reconnue',
            'title_en': 'Recognized Excellence',
            'description_fr': '25 ans d\'expertise au service de la satisfaction client et de l\'excellence dans le travail du bois.',
            'description_en': '25 years of expertise serving customer satisfaction and excellence in woodworking.',
            'order': 4
        }
    ]

    for timeline_item in timeline_data:
        event, created = TimelineEvent.objects.update_or_create(
            year=timeline_item['year'],
            defaults=timeline_item
        )
        action = "cree" if created else "mis a jour"
        print(f"  [OK] Evenement {action}: {event.year} - {event.title_fr}")

def main():
    print("=" * 70)
    print("MISE A JOUR DU CONTENU DKBOIS")
    print("Adaptation du contenu de l'entreprise DF Bois camerounaise")
    print("=" * 70)

    try:
        update_company_description()
        create_founder_profile()
        update_company_values()
        update_timeline()

        print("\n" + "=" * 70)
        print("MISE A JOUR TERMINEE AVEC SUCCES!")
        print("=" * 70)
        print("\nContenu mis a jour:")
        print("  - Description de l'entreprise")
        print("  - Profil du fondateur: Defehe Kamdem FOBHA Mathurin")
        print("  - Valeurs de l'entreprise (4 valeurs)")
        print("  - Chronologie (4 evenements)")
        print("\nAccedez a l'admin Django pour voir les changements:")
        print("  http://localhost:3000/admin/")

    except Exception as e:
        print(f"\nErreur: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
