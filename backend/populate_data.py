"""
Data population script for DKbois backend.
This script populates the database with the initial data from data.js

Usage:
    python populate_data.py
"""

import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dkbois_backend.settings')
django.setup()

from portfolio.models import (
    Project, Service, Testimonial, TeamMember,
    TimelineEvent, CompanyValue, FAQ
)


def populate_projects():
    """Populate portfolio projects"""
    print("Populating projects...")

    portfolioImage = 'https://r2.flowith.net/files/jpeg/32GEY-realistic_featured_achievements_placeholders_index_3@1024x1024.jpeg'
    interiorImage = 'https://r2.flowith.net/files/jpeg/FE8CF-hero_section_woodworking_placeholder_index_2@1024x1024.jpeg'
    cabinetImage = 'https://r2.flowith.net/files/jpeg/WS4KO-icone_services_menuiserie_ebenisterie_restauration_agencement_index_1@1024x1024.jpeg'
    restoreImage = portfolioImage

    projects_data = [
        {
            'slug': 'cuisine-haussmannienne',
            'title_fr': 'Cuisine Haussmannienne',
            'title_en': 'Haussmann Kitchen',
            'category': 'kitchen',
            'type': 'fitting',
            'material': 'oak',
            'short_desc_fr': "Alliance du charme ancien et de la modernité.",
            'short_desc_en': "Blending old charm with modernity.",
            'full_desc_fr': "Rénovation complète d'une cuisine dans un appartement haussmannien. L'objectif était de conserver l'âme du lieu tout en intégrant des équipements modernes invisibles.",
            'full_desc_en': "Complete renovation of a kitchen in a Haussmann apartment. The goal was to preserve the soul of the place while integrating invisible modern equipment.",
            'challenge_fr': "Intégration de l'électroménager dans des moulures existantes sans dénaturer le style.",
            'challenge_en': "Integrating appliances into existing moldings without distorting the style.",
            'duration_fr': "3 mois",
            'duration_en': "3 months",
            'location': "Paris 7ème",
            'finish_fr': "Huile naturelle mate",
            'finish_en': "Matte natural oil",
            'tags': ["Cuisine", "Chêne", "Haussmann"],
            'images': [portfolioImage, interiorImage, cabinetImage],
            'featured': True,
            'order': 1
        },
        {
            'slug': 'bibliotheque-noyer',
            'title_fr': 'Bibliothèque Noyer',
            'title_en': 'Walnut Library',
            'category': 'living',
            'type': 'creation',
            'material': 'walnut',
            'short_desc_fr': "Bibliothèque sur mesure toute hauteur.",
            'short_desc_en': "Full-height custom library.",
            'full_desc_fr': "Conception et pose d'une bibliothèque monumentale en noyer américain massif. Intégration d'un éclairage LED subtil pour mettre en valeur les ouvrages d'art.",
            'full_desc_en': "Design and installation of a monumental solid American walnut library. Integration of subtle LED lighting to highlight art books.",
            'challenge_fr': "Ajustement précis sur des murs non droits d'une bâtisse du XVIIe siècle.",
            'challenge_en': "Precise adjustment on uneven walls of a 17th-century building.",
            'duration_fr': "6 semaines",
            'duration_en': "6 weeks",
            'location': "Lyon",
            'finish_fr': "Vernis satiné",
            'finish_en': "Satin varnish",
            'tags': ["Salon", "Noyer", "Luxe"],
            'images': [interiorImage, portfolioImage, cabinetImage],
            'featured': True,
            'order': 2
        },
        {
            'slug': 'restauration-commode-xviiie',
            'title_fr': 'Restauration Commode XVIIIe',
            'title_en': '18th C. Commode Restoration',
            'category': 'living',
            'type': 'restoration',
            'material': 'walnut',
            'short_desc_fr': "Sauvegarde du patrimoine familial.",
            'short_desc_en': "Saving family heritage.",
            'full_desc_fr': "Restauration complète d'une commode Louis XV. Reprise des placages soulevés, nettoyage des bronzes et vernis au tampon traditionnel.",
            'full_desc_en': "Complete restoration of a Louis XV commode. Repairing lifted veneers, cleaning bronzes, and traditional French polish.",
            'challenge_fr': "Conservation de la patine d'origine tout en consolidant la structure.",
            'challenge_en': "Preserving the original patina while consolidating the structure.",
            'duration_fr': "4 semaines",
            'duration_en': "4 weeks",
            'location': "Atelier",
            'finish_fr': "Vernis au tampon",
            'finish_en': "French polish",
            'tags': ["Restauration", "Noyer", "Ancien"],
            'images': [restoreImage, cabinetImage, portfolioImage],
            'featured': False,
            'order': 3
        },
    ]

    for data in projects_data:
        project, created = Project.objects.get_or_create(
            slug=data['slug'],
            defaults=data
        )
        if created:
            print(f"  Created: {project.title_fr}")
        else:
            print(f"  Already exists: {project.title_fr}")


def populate_services():
    """Populate services"""
    print("\nPopulating services...")

    interiorImage = 'https://r2.flowith.net/files/jpeg/FE8CF-hero_section_woodworking_placeholder_index_2@1024x1024.jpeg'
    cabinetImage = 'https://r2.flowith.net/files/jpeg/WS4KO-icone_services_menuiserie_ebenisterie_restauration_agencement_index_1@1024x1024.jpeg'
    restoreImage = 'https://r2.flowith.net/files/jpeg/32GEY-realistic_featured_achievements_placeholders_index_3@1024x1024.jpeg'

    services_data = [
        {
            'service_id': 'interior',
            'slug': 'menuiserie-interieure',
            'icon': 'door-open',
            'title_fr': 'Menuiserie Intérieure',
            'title_en': 'Interior Joinery',
            'description_fr': "Nous façonnons votre espace de vie avec des menuiseries sur mesure qui allient fonctionnalité et esthétique. Que ce soit pour des portes massives, des escaliers architecturaux ou des parquets traditionnels, nous sélectionnons les meilleures essences pour garantir durabilité et élégance.",
            'description_en': "We shape your living space with custom joinery that combines functionality and aesthetics. Whether for solid doors, architectural staircases, or traditional flooring, we select the finest woods to ensure durability and elegance.",
            'sub_services': [
                {'fr': 'Portes et fenêtres', 'en': 'Custom doors and windows'},
                {'fr': 'Escaliers et rampes', 'en': 'Stairs and railings'},
                {'fr': 'Parquets et lambris', 'en': 'Parquet and paneling'},
                {'fr': 'Placards et dressings', 'en': 'Cupboards and walk-in closets'}
            ],
            'process_steps': [
                {'step': 1, 'title': {'fr': 'Relevé & Conception', 'en': 'Survey & Design'}},
                {'step': 2, 'title': {'fr': 'Fabrication en Atelier', 'en': 'Workshop Fabrication'}},
                {'step': 3, 'title': {'fr': 'Pose & Finitions', 'en': 'Installation & Finishing'}}
            ],
            'timeframe_fr': '6 à 10 semaines',
            'timeframe_en': '6 to 10 weeks',
            'images': [interiorImage, cabinetImage, restoreImage],
            'order': 1
        },
        {
            'service_id': 'cabinetry',
            'slug': 'ebenisterie-sur-mesure',
            'icon': 'gem',
            'title_fr': 'Ébénisterie sur Mesure',
            'title_en': 'Custom Cabinetmaking',
            'description_fr': "L'ébénisterie est le cœur de notre passion. Nous concevons des meubles uniques, bibliothèques complexes et pièces de mobilier qui deviennent les éléments centraux de votre décoration. Chaque création est une œuvre d'art fonctionnelle.",
            'description_en': "Cabinetmaking is the heart of our passion. We design unique furniture, complex libraries, and pieces that become the central elements of your decor. Each creation is a functional work of art.",
            'sub_services': [
                {'fr': 'Meubles de salon', 'en': 'Living room furniture'},
                {'fr': 'Mobilier de cuisine', 'en': 'Kitchen furniture'},
                {'fr': 'Bibliothèques et bureaux', 'en': 'Libraries and offices'},
                {'fr': 'Créations artistiques', 'en': 'Artistic creations'}
            ],
            'process_steps': [
                {'step': 1, 'title': {'fr': 'Design & Choix des Essences', 'en': 'Design & Wood Selection'}},
                {'step': 2, 'title': {'fr': 'Façonnage & Assemblage', 'en': 'Crafting & Assembly'}},
                {'step': 3, 'title': {'fr': 'Vernissage & Finition', 'en': 'Varnishing & Finishing'}}
            ],
            'timeframe_fr': '8 à 12 semaines',
            'timeframe_en': '8 to 12 weeks',
            'images': [cabinetImage, interiorImage, restoreImage],
            'order': 2
        },
        {
            'service_id': 'restoration',
            'slug': 'restauration-patrimoniale',
            'icon': 'hammer',
            'title_fr': 'Restauration Patrimoniale',
            'title_en': 'Heritage Restoration',
            'description_fr': "Respecter l'histoire et le travail des anciens. Nous redonnons vie aux meubles d'époque et boiseries historiques en utilisant des techniques traditionnelles (colle d'os, vernis au tampon) pour préserver l'authenticité de votre patrimoine.",
            'description_en': "Respecting history and the work of the ancients. We bring period furniture and historic woodwork back to life using traditional techniques (hide glue, French polish) to preserve the authenticity of your heritage.",
            'sub_services': [
                {'fr': 'Meubles anciens', 'en': 'Antique furniture'},
                {'fr': 'Boiseries historiques', 'en': 'Historic woodwork'},
                {'fr': 'Expertise et conseil', 'en': 'Expertise and advice'},
                {'fr': 'Techniques traditionnelles', 'en': 'Traditional techniques'}
            ],
            'process_steps': [
                {'step': 1, 'title': {'fr': 'Diagnostic & Traitement', 'en': 'Diagnosis & Treatment'}},
                {'step': 2, 'title': {'fr': 'Consolidation Structurelle', 'en': 'Structural Consolidation'}},
                {'step': 3, 'title': {'fr': 'Restauration & Patine', 'en': 'Restoration & Patina'}}
            ],
            'timeframe_fr': 'Sur devis',
            'timeframe_en': 'On quote',
            'images': [restoreImage, cabinetImage, interiorImage],
            'order': 3
        },
        {
            'service_id': 'commercial',
            'slug': 'agencement-commercial',
            'icon': 'layout-dashboard',
            'title_fr': 'Agencement Commercial',
            'title_en': 'Commercial Fitting',
            'description_fr': "Nous accompagnons les professionnels dans l'aménagement de leurs espaces. Boutiques, hôtels, ou bureaux : nous créons des environnements qui reflètent votre image de marque avec des matériaux nobles et durables.",
            'description_en': "We assist professionals in fitting out their spaces. Shops, hotels, or offices: we create environments that reflect your brand image using noble and sustainable materials.",
            'sub_services': [
                {'fr': 'Boutiques et showrooms', 'en': 'Shops and showrooms'},
                {'fr': 'Restaurants et hôtels', 'en': 'Restaurants and hotels'},
                {'fr': 'Bureaux professionnels', 'en': 'Professional offices'},
                {'fr': 'Stands d\'exposition', 'en': 'Exhibition stands'}
            ],
            'process_steps': [
                {'step': 1, 'title': {'fr': 'Étude & Plans', 'en': 'Study & Plans'}},
                {'step': 2, 'title': {'fr': 'Préfabrication en Atelier', 'en': 'Workshop Prefabrication'}},
                {'step': 3, 'title': {'fr': 'Installation sur Site', 'en': 'On-site Installation'}}
            ],
            'timeframe_fr': '4 à 8 semaines',
            'timeframe_en': '4 to 8 weeks',
            'images': [interiorImage, restoreImage, cabinetImage],
            'order': 4
        }
    ]

    for data in services_data:
        service, created = Service.objects.get_or_create(
            service_id=data['service_id'],
            defaults=data
        )
        if created:
            print(f"  Created: {service.title_fr}")
        else:
            print(f"  Already exists: {service.title_fr}")


def populate_testimonials():
    """Populate testimonials"""
    print("\nPopulating testimonials...")

    portraitImage = 'https://r2.flowith.net/files/jpeg/WW58V-professional_artisan_portraits_index_4@1024x1024.jpeg'

    testimonials_data = [
        {
            'name': 'Jean Dupont',
            'role': "Architecte d'intérieur",
            'text': "Une précision incroyable et un respect absolu des délais. DKbois est mon partenaire privilégié pour mes chantiers haut de gamme.",
            'stars': 5,
            'image': portraitImage,
            'order': 1
        },
        {
            'name': 'Sophie Martin',
            'role': 'Particulier',
            'text': "Ils ont transformé notre salon avec une bibliothèque sur mesure qui dépasse toutes nos attentes. Finitions parfaites.",
            'stars': 5,
            'image': portraitImage,
            'order': 2
        },
        {
            'name': 'Marc Lefevre',
            'role': 'Restaurateur',
            'text': "L'agencement complet de notre restaurant a été réalisé avec brio. Le bois apporte une chaleur que nos clients adorent.",
            'stars': 5,
            'image': portraitImage,
            'order': 3
        }
    ]

    for data in testimonials_data:
        testimonial, created = Testimonial.objects.get_or_create(
            name=data['name'],
            defaults=data
        )
        if created:
            print(f"  Created: {testimonial.name}")
        else:
            print(f"  Already exists: {testimonial.name}")


def populate_team():
    """Populate team members"""
    print("\nPopulating team members...")

    portraitImage = 'https://r2.flowith.net/files/jpeg/WW58V-professional_artisan_portraits_index_4@1024x1024.jpeg'

    team_data = [
        {
            'name': 'Marc Dubois',
            'role_fr': 'Maître Ébéniste',
            'role_en': 'Master Cabinetmaker',
            'experience_years': 25,
            'quote_fr': 'Le bois ne ment jamais.',
            'quote_en': 'Wood never lies.',
            'image': portraitImage,
            'order': 1
        },
        {
            'name': 'Sarah Chen',
            'role_fr': 'Designer Bois',
            'role_en': 'Wood Designer',
            'experience_years': 8,
            'quote_fr': 'Allier fonction et émotion.',
            'quote_en': 'Combining function and emotion.',
            'image': portraitImage,
            'order': 2
        },
        {
            'name': 'Thomas Vallet',
            'role_fr': "Chef d'Atelier",
            'role_en': 'Workshop Manager',
            'experience_years': 15,
            'quote_fr': 'La précision est reine.',
            'quote_en': 'Precision is king.',
            'image': portraitImage,
            'order': 3
        },
        {
            'name': 'Lucas Petit',
            'role_fr': 'Compagnon Menuisier',
            'role_en': 'Journeyman Carpenter',
            'experience_years': 5,
            'quote_fr': 'Apprendre chaque jour.',
            'quote_en': 'Learning every day.',
            'image': portraitImage,
            'order': 4
        }
    ]

    for data in team_data:
        member, created = TeamMember.objects.get_or_create(
            name=data['name'],
            defaults=data
        )
        if created:
            print(f"  Created: {member.name}")
        else:
            print(f"  Already exists: {member.name}")


def populate_timeline():
    """Populate timeline events"""
    print("\nPopulating timeline...")

    timeline_data = [
        {
            'year': '1990',
            'title_fr': 'La Fondation',
            'title_en': 'Foundation',
            'description_fr': "Création de l'atelier par Pierre Dubois, artisan passionné, dans un petit garage de banlieue parisienne.",
            'description_en': "Establishment of the workshop by Pierre Dubois, a passionate craftsman, in a small garage in the Parisian suburbs.",
            'order': 1
        },
        {
            'year': '2005',
            'title_fr': "L'Expansion",
            'title_en': 'Expansion',
            'description_fr': 'Déménagement dans nos locaux actuels de 800m² et acquisition de nos premières machines à commande numérique.',
            'description_en': 'Move to our current 800m² premises and acquisition of our first CNC machines.',
            'order': 2
        },
        {
            'year': '2012',
            'title_fr': 'Reconnaissance',
            'title_en': 'Recognition',
            'description_fr': "Obtention du label 'Artisan d'Art' récompensant la qualité exceptionnelle de nos restaurations de mobilier.",
            'description_en': "Obtained the 'Artisan d'Art' label rewarding the exceptional quality of our furniture restorations.",
            'order': 3
        },
        {
            'year': '2024',
            'title_fr': 'Innovation Durable',
            'title_en': 'Sustainable Innovation',
            'description_fr': 'Transition vers une production 100% éco-responsable avec recyclage complet des déchets bois.',
            'description_en': 'Transition to 100% eco-responsible production with complete wood waste recycling.',
            'order': 4
        }
    ]

    for data in timeline_data:
        event, created = TimelineEvent.objects.get_or_create(
            year=data['year'],
            title_fr=data['title_fr'],
            defaults=data
        )
        if created:
            print(f"  Created: {event.year} - {event.title_fr}")
        else:
            print(f"  Already exists: {event.year} - {event.title_fr}")


def populate_values():
    """Populate company values"""
    print("\nPopulating company values...")

    values_data = [
        {
            'icon': 'hammer',
            'title_fr': 'Savoir-Faire',
            'title_en': 'Craftsmanship',
            'description_fr': 'Maîtrise des techniques ancestrales et modernes pour un résultat impeccable.',
            'description_en': 'Mastery of ancestral and modern techniques for an impeccable result.',
            'order': 1
        },
        {
            'icon': 'leaf',
            'title_fr': 'Durabilité',
            'title_en': 'Sustainability',
            'description_fr': 'Sélection de bois issus de forêts gérées durablement et finitions écologiques.',
            'description_en': 'Selection of wood from sustainably managed forests and ecological finishes.',
            'order': 2
        },
        {
            'icon': 'scan-face',
            'title_fr': 'Service Personnalisé',
            'title_en': 'Personalized Service',
            'description_fr': 'Une écoute attentive de vos besoins pour un projet qui vous ressemble vraiment.',
            'description_en': 'Attentive listening to your needs for a project that truly reflects you.',
            'order': 3
        },
        {
            'icon': 'lightbulb',
            'title_fr': 'Innovation',
            'title_en': 'Innovation',
            'description_fr': "Allier la technologie de pointe à la main de l'homme pour repousser les limites.",
            'description_en': 'Combining cutting-edge technology with human touch to push the boundaries.',
            'order': 4
        }
    ]

    for data in values_data:
        value, created = CompanyValue.objects.get_or_create(
            title_fr=data['title_fr'],
            defaults=data
        )
        if created:
            print(f"  Created: {value.title_fr}")
        else:
            print(f"  Already exists: {value.title_fr}")


def populate_faqs():
    """Populate FAQs"""
    print("\nPopulating FAQs...")

    faqs_data = [
        {
            'question_fr': 'Quels sont vos délais de réalisation ?',
            'question_en': 'What are your lead times?',
            'answer_fr': 'Nos délais varient selon la complexité du projet. Comptez généralement 6 à 8 semaines pour la fabrication d\'un meuble sur mesure et 8 à 12 semaines pour un agencement complet.',
            'answer_en': 'Our lead times vary depending on project complexity. Generally allow 6 to 8 weeks for custom furniture and 8 to 12 weeks for a complete fit-out.',
            'order': 1
        },
        {
            'question_fr': 'Comment se déroule le processus de devis ?',
            'question_en': 'How does the quote process work?',
            'answer_fr': 'Après un premier contact via notre formulaire, nous organisons un rendez-vous pour discuter de votre projet. Nous vous envoyons ensuite un devis détaillé et gratuit sous 7 jours.',
            'answer_en': 'After initial contact via our form, we arrange a meeting to discuss your project. We then send a detailed and free quote within 7 days.',
            'order': 2
        },
        {
            'question_fr': 'Travaillez-vous uniquement avec du bois local ?',
            'question_en': 'Do you only work with local wood?',
            'answer_fr': 'Nous privilégions les essences de bois françaises et européennes issues de forêts gérées durablement (PEFC, FSC). Nous pouvons également travailler avec des bois exotiques sur demande spécifique.',
            'answer_en': 'We prioritize French and European wood species from sustainably managed forests (PEFC, FSC). We can also work with exotic woods upon specific request.',
            'order': 3
        }
    ]

    for data in faqs_data:
        faq, created = FAQ.objects.get_or_create(
            question_fr=data['question_fr'],
            defaults=data
        )
        if created:
            print(f"  Created: {faq.question_fr}")
        else:
            print(f"  Already exists: {faq.question_fr}")


def main():
    """Main function to populate all data"""
    print("=" * 60)
    print("DKbois Database Population Script")
    print("=" * 60)

    populate_projects()
    populate_services()
    populate_testimonials()
    populate_team()
    populate_timeline()
    populate_values()
    populate_faqs()

    print("\n" + "=" * 60)
    print("Database population complete!")
    print("=" * 60)
    print("\nYou can now:")
    print("1. Create a superuser: python manage.py createsuperuser")
    print("2. Run the development server: python manage.py runserver")
    print("3. Access the admin at: http://127.0.0.1:8000/admin/")
    print("4. Access the API at: http://127.0.0.1:8000/api/")


if __name__ == '__main__':
    main()
