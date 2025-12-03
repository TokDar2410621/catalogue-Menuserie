"""
Data population script for DKbois backend - Using REAL local images
This script populates the database with data using actual images from the image folder

Usage:
    python populate_real_data.py
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
    """Populate portfolio projects with real images"""
    print("Populating projects with real images...")

    # Using actual images from the image folder
    projects_data = [
        {
            'slug': 'cuisine-moderne-bois-clair',
            'title_fr': 'Cuisine Moderne Bois Clair',
            'title_en': 'Modern Light Wood Kitchen',
            'category': 'kitchen',
            'type': 'fitting',
            'material': 'oak',
            'short_desc_fr': "Cuisine complète en bois clair avec plan de travail blanc.",
            'short_desc_en': "Complete light wood kitchen with white countertop.",
            'full_desc_fr': "Installation complète d'une cuisine d'angle en bois clair. Portes vitrées pour un style élégant et fonctionnel. Parfaite harmonie entre esthétique moderne et chaleur du bois naturel.",
            'full_desc_en': "Complete installation of a light wood corner kitchen. Glass doors for an elegant and functional style. Perfect harmony between modern aesthetics and the warmth of natural wood.",
            'challenge_fr': "Optimisation de l'espace en angle tout en gardant l'accessibilité.",
            'challenge_en': "Optimizing corner space while maintaining accessibility.",
            'duration_fr': "6 semaines",
            'duration_en': "6 weeks",
            'location': "Yaoundé, Cameroun",
            'finish_fr': "Vernis satiné naturel",
            'finish_en': "Natural satin varnish",
            'tags': ["Cuisine", "Bois clair", "Moderne"],
            'images': [
                'image/cuisine-images/cuisine-angle-bois-clair-portes-vitrees-01.jpg',
                'image/cuisine-images/cuisine-angle-bois-clair-construction-01.jpg',
                'image/cuisine-images/cuisine-complet.jpg'
            ],
            'featured': True,
            'order': 1
        },
        {
            'slug': 'porte-bois-geometrique',
            'title_fr': 'Porte Bois Motifs Géométriques',
            'title_en': 'Geometric Pattern Wood Door',
            'category': 'living',
            'type': 'creation',
            'material': 'walnut',
            'short_desc_fr': "Porte double battant avec motifs géométriques raffinés.",
            'short_desc_en': "Double leaf door with refined geometric patterns.",
            'full_desc_fr': "Création sur mesure de portes intérieures avec motifs géométriques. Travail minutieux pour créer des panneaux symétriques et élégants qui ajoutent du caractère à votre intérieur.",
            'full_desc_en': "Custom creation of interior doors with geometric patterns. Meticulous work to create symmetrical and elegant panels that add character to your interior.",
            'challenge_fr': "Précision millimétrique pour l'alignement parfait des motifs.",
            'challenge_en': "Millimeter precision for perfect pattern alignment.",
            'duration_fr': "4 semaines",
            'duration_en': "4 weeks",
            'location': "Yaoundé, Cameroun",
            'finish_fr': "Huile protectrice",
            'finish_en': "Protective oil",
            'tags': ["Porte", "Design", "Géométrique"],
            'images': [
                'image/porte-images/porte-double-battant-bois-geometrique-02.jpg',
                'image/porte-images/porte-simple-bois-geometrique-02.jpg',
                'image/porte-images/porte-double-bois-clair-panneaux-geometriques-01.jpg'
            ],
            'featured': True,
            'order': 2
        },
        {
            'slug': 'salon-complet-canape-fauteuils',
            'title_fr': 'Ensemble Salon Complet',
            'title_en': 'Complete Living Room Set',
            'category': 'living',
            'type': 'creation',
            'material': 'oak',
            'short_desc_fr': "Canapé et fauteuils assortis en bois massif.",
            'short_desc_en': "Matching sofa and armchairs in solid wood.",
            'full_desc_fr': "Création d'un ensemble de salon complet comprenant canapé 3 places et fauteuils. Structure en bois massif, finition verte élégante. Design confortable et intemporel.",
            'full_desc_en': "Creation of a complete living room set including 3-seater sofa and armchairs. Solid wood structure, elegant green finish. Comfortable and timeless design.",
            'challenge_fr': "Assurer la cohérence du design tout en garantissant le confort optimal.",
            'challenge_en': "Ensuring design consistency while guaranteeing optimal comfort.",
            'duration_fr': "8 semaines",
            'duration_en': "8 weeks",
            'location': "Atelier DKBOIS",
            'finish_fr': "Tissu velours vert / Structure bois naturel",
            'finish_en': "Green velvet fabric / Natural wood structure",
            'tags': ["Salon", "Mobilier", "Confort"],
            'images': [
                'image/salon-images/salon-complet-canape-fauteuils-vert-01.jpg',
                'image/salon-images/salon-complet-canape-fauteuils-vert-02.jpg',
                'image/canape-images/canape-vert-turquoise-velours-atelier-02.jpg'
            ],
            'featured': True,
            'order': 3
        },
        {
            'slug': 'lit-moderne-lamelles-orange',
            'title_fr': 'Lit Moderne à Lamelles',
            'title_en': 'Modern Slatted Bed',
            'category': 'living',
            'type': 'creation',
            'material': 'oak',
            'short_desc_fr': "Lit avec tête de lit à lamelles horizontales et chevet intégré.",
            'short_desc_en': "Bed with horizontal slat headboard and integrated nightstand.",
            'full_desc_fr': "Lit moderne avec tête de lit design à lamelles horizontales. Finition rouge-orange élégante, chevet intégré pour un ensemble harmonieux. Confort et style contemporain.",
            'full_desc_en': "Modern bed with designer horizontal slat headboard. Elegant orange-red finish, integrated nightstand for a harmonious ensemble. Comfort and contemporary style.",
            'challenge_fr': "Intégration parfaite du chevet dans le design global du lit.",
            'challenge_en': "Perfect integration of the nightstand into the overall bed design.",
            'duration_fr': "5 semaines",
            'duration_en': "5 weeks",
            'location': "Yaoundé, Cameroun",
            'finish_fr': "Peinture orange-rouge mate",
            'finish_en': "Matte orange-red paint",
            'tags': ["Chambre", "Lit", "Moderne"],
            'images': [
                'image/lit-images/lit-rouge-orange-lamelles-horizontales-chevet-01.jpg',
                'image/lit-images/lit-rouge-orange-lamelles-horizontales-chevet-02.jpg',
                'image/lit-images/lit-simple-bois-fonce-draps-verts-01.jpg'
            ],
            'featured': True,
            'order': 4
        },
        {
            'slug': 'table-ronde-salle-manger',
            'title_fr': 'Table Ronde Salle à Manger',
            'title_en': 'Round Dining Table',
            'category': 'living',
            'type': 'creation',
            'material': 'walnut',
            'short_desc_fr': "Table ronde en bois foncé avec chaises assorties.",
            'short_desc_en': "Dark wood round table with matching chairs.",
            'full_desc_fr': "Ensemble table ronde et chaises pour salle à manger. Bois foncé noble avec finition laquée. Chaises vertes modernes pour un contraste élégant. Parfait pour 4 à 6 convives.",
            'full_desc_en': "Round table and chairs set for dining room. Noble dark wood with lacquered finish. Modern green chairs for an elegant contrast. Perfect for 4 to 6 guests.",
            'challenge_fr': "Équilibre visuel entre le bois foncé et les chaises colorées.",
            'challenge_en': "Visual balance between dark wood and colored chairs.",
            'duration_fr': "6 semaines",
            'duration_en': "6 weeks",
            'location': "Yaoundé, Cameroun",
            'finish_fr': "Vernis laqué brillant",
            'finish_en': "High-gloss lacquer",
            'tags': ["Table", "Salle à manger", "Moderne"],
            'images': [
                'image/table-images/table-ronde-salle-manger-bois-fonce-chaises-vertes-01.jpg',
                'image/table-images/table-salle-manger-blanche-chaises-bleues.jpg',
                'image/table-images/table-blanche-6-chaises-bleues-exterieur.jpg'
            ],
            'featured': True,
            'order': 5
        },
        {
            'slug': 'commode-rouge-orange-tiroirs',
            'title_fr': 'Commode Rouge-Orange à Tiroirs',
            'title_en': 'Red-Orange Drawer Dresser',
            'category': 'living',
            'type': 'creation',
            'material': 'oak',
            'short_desc_fr': "Commode moderne avec multiples tiroirs et porte centrale.",
            'short_desc_en': "Modern dresser with multiple drawers and central door.",
            'full_desc_fr': "Commode de rangement avec 6 tiroirs latéraux et porte centrale. Finition rouge-orange vibrante. Design fonctionnel pour optimiser l'espace de rangement.",
            'full_desc_en': "Storage dresser with 6 side drawers and central door. Vibrant red-orange finish. Functional design to optimize storage space.",
            'challenge_fr': "Alignement parfait des tiroirs pour une ouverture fluide.",
            'challenge_en': "Perfect drawer alignment for smooth opening.",
            'duration_fr': "4 semaines",
            'duration_en': "4 weeks",
            'location': "Atelier DKBOIS",
            'finish_fr': "Peinture orange-rouge satinée",
            'finish_en': "Satin orange-red paint",
            'tags': ["Commode", "Rangement", "Couleur"],
            'images': [
                'image/commode-images/commode-rouge-orange-tiroirs-porte-centrale-01.jpg',
                'image/atelier-images/artisan-selfie-commode-orange-tiroirs.jpg',
                'image/meuble-rangement-images/meuble-rangement-rouge-orange-atelier-01.jpg'
            ],
            'featured': False,
            'order': 6
        },
    ]

    for data in projects_data:
        project, created = Project.objects.get_or_create(
            slug=data['slug'],
            defaults=data
        )
        if created:
            print(f"  [+] Created: {project.title_fr}")
        else:
            # Update existing project with new data
            for key, value in data.items():
                if key != 'slug':
                    setattr(project, key, value)
            project.save()
            print(f"  [*] Updated: {project.title_fr}")


def populate_services():
    """Populate services with real images"""
    print("\nPopulating services with real images...")

    services_data = [
        {
            'service_id': 'interior',
            'slug': 'menuiserie-interieure',
            'icon': 'door-open',
            'title_fr': 'Menuiserie Intérieure',
            'title_en': 'Interior Joinery',
            'description_fr': "Nous façonnons votre espace de vie avec des menuiseries sur mesure qui allient fonctionnalité et esthétique. Portes, escaliers, parquets - chaque élément est créé avec passion et précision.",
            'description_en': "We shape your living space with custom joinery that combines functionality and aesthetics. Doors, stairs, flooring - each element is created with passion and precision.",
            'sub_services': [
                {'fr': 'Portes sur mesure', 'en': 'Custom doors'},
                {'fr': 'Fenêtres en bois', 'en': 'Wooden windows'},
                {'fr': 'Escaliers', 'en': 'Stairs'},
                {'fr': 'Parquets', 'en': 'Flooring'}
            ],
            'process_steps': [
                {'step': 1, 'title': {'fr': 'Prise de mesures', 'en': 'Measurements'}},
                {'step': 2, 'title': {'fr': 'Fabrication atelier', 'en': 'Workshop fabrication'}},
                {'step': 3, 'title': {'fr': 'Installation', 'en': 'Installation'}}
            ],
            'timeframe_fr': '4 à 6 semaines',
            'timeframe_en': '4 to 6 weeks',
            'images': [
                'image/porte-images/porte-bois-clair-lamelles-horizontales-atelier-01.jpg',
                'image/porte-images/porte-double-bois-clair-panneaux-classiques-01.jpg',
                'image/porte-images/porte-simple-bois-clair-moderne-01.jpg'
            ],
            'order': 1
        },
        {
            'service_id': 'cabinetry',
            'slug': 'ebenisterie-sur-mesure',
            'icon': 'gem',
            'title_fr': 'Ébénisterie sur Mesure',
            'title_en': 'Custom Cabinetmaking',
            'description_fr': "Création de meubles uniques adaptés à vos besoins et votre style. Chaque pièce est une œuvre d'art fonctionnelle, fabriquée avec les meilleurs bois.",
            'description_en': "Creating unique furniture adapted to your needs and style. Each piece is a functional work of art, crafted with the finest woods.",
            'sub_services': [
                {'fr': 'Cuisines équipées', 'en': 'Fitted kitchens'},
                {'fr': 'Salons sur mesure', 'en': 'Custom living rooms'},
                {'fr': 'Chambres complètes', 'en': 'Complete bedrooms'},
                {'fr': 'Tables et chaises', 'en': 'Tables and chairs'}
            ],
            'process_steps': [
                {'step': 1, 'title': {'fr': 'Design & Plan', 'en': 'Design & Planning'}},
                {'step': 2, 'title': {'fr': 'Sélection du bois', 'en': 'Wood selection'}},
                {'step': 3, 'title': {'fr': 'Fabrication & Finition', 'en': 'Crafting & Finishing'}}
            ],
            'timeframe_fr': '6 à 10 semaines',
            'timeframe_en': '6 to 10 weeks',
            'images': [
                'image/cuisine-images/cuisine-angle-bois-clair-portes-vitrees-01.jpg',
                'image/salon-images/salon-complet-canape-fauteuils-vert-01.jpg',
                'image/lit-images/lit-rouge-orange-lamelles-horizontales-chevet-01.jpg'
            ],
            'order': 2
        },
        {
            'service_id': 'restoration',
            'slug': 'restauration-meubles',
            'icon': 'hammer',
            'title_fr': 'Restauration de Meubles',
            'title_en': 'Furniture Restoration',
            'description_fr': "Redonnez vie à vos meubles anciens. Restauration respectueuse du patrimoine avec techniques traditionnelles et modernes.",
            'description_en': "Bring your old furniture back to life. Heritage-respectful restoration with traditional and modern techniques.",
            'sub_services': [
                {'fr': 'Meubles anciens', 'en': 'Antique furniture'},
                {'fr': 'Réparations structurelles', 'en': 'Structural repairs'},
                {'fr': 'Refinition', 'en': 'Refinishing'},
                {'fr': 'Consolidation', 'en': 'Consolidation'}
            ],
            'process_steps': [
                {'step': 1, 'title': {'fr': 'Diagnostic', 'en': 'Diagnosis'}},
                {'step': 2, 'title': {'fr': 'Restauration', 'en': 'Restoration'}},
                {'step': 3, 'title': {'fr': 'Protection finale', 'en': 'Final protection'}}
            ],
            'timeframe_fr': 'Sur devis',
            'timeframe_en': 'On quote',
            'images': [
                'image/armoire-images/armoire-rouge-brun-etageres-tiroirs-02.jpg',
                'image/commode-images/commode-rouge-orange-tiroirs-porte-centrale-01.jpg',
                'image/gueridon-images/gueridon-bois-massif-pied-tourne-01.jpg'
            ],
            'order': 3
        },
        {
            'service_id': 'commercial',
            'slug': 'agencement-commercial',
            'icon': 'layout-dashboard',
            'title_fr': 'Agencement Commercial',
            'title_en': 'Commercial Fitting',
            'description_fr': "Aménagement professionnel pour boutiques, restaurants, bureaux. Création d'espaces fonctionnels et esthétiques qui reflètent votre identité.",
            'description_en': "Professional fitting for shops, restaurants, offices. Creating functional and aesthetic spaces that reflect your identity.",
            'sub_services': [
                {'fr': 'Boutiques', 'en': 'Shops'},
                {'fr': 'Restaurants', 'en': 'Restaurants'},
                {'fr': 'Bureaux', 'en': 'Offices'},
                {'fr': 'Hôtels', 'en': 'Hotels'}
            ],
            'process_steps': [
                {'step': 1, 'title': {'fr': 'Étude de projet', 'en': 'Project study'}},
                {'step': 2, 'title': {'fr': 'Préfabrication', 'en': 'Prefabrication'}},
                {'step': 3, 'title': {'fr': 'Installation rapide', 'en': 'Quick installation'}}
            ],
            'timeframe_fr': '3 à 8 semaines',
            'timeframe_en': '3 to 8 weeks',
            'images': [
                'image/cuisine-images/cuisine-angle-bois-clair-utilisee-vitrine-01.jpg',
                'image/table-images/table-salle-manger-rectangulaire-8-chaises-noires-01.jpg',
                'image/bibliotheque-images/bibliotheque-grise-portes-vertes-basses.jpg'
            ],
            'order': 4
        }
    ]

    for data in services_data:
        service, created = Service.objects.get_or_create(
            service_id=data['service_id'],
            defaults=data
        )
        if created:
            print(f"  [+] Created: {service.title_fr}")
        else:
            for key, value in data.items():
                if key != 'service_id':
                    setattr(service, key, value)
            service.save()
            print(f"  [*] Updated: {service.title_fr}")


def populate_testimonials():
    """Populate testimonials with real images"""
    print("\nPopulating testimonials with real images...")

    portraitImage = 'image/atelier-images/proprietaire-costume-assis-planches-atelier.jpg'

    testimonials_data = [
        {
            'name': 'Jean Dupont',
            'role': "Architecte d'intérieur",
            'text': "Une précision incroyable et un respect absolu des délais. DKBOIS est mon partenaire privilégié pour mes chantiers haut de gamme à Yaoundé.",
            'stars': 5,
            'image': portraitImage,
            'order': 1
        },
        {
            'name': 'Sophie Martin',
            'role': 'Particulier',
            'text': "Ils ont transformé notre salon avec une bibliothèque sur mesure qui dépasse toutes nos attentes. Finitions parfaites et bois de qualité exceptionnelle.",
            'stars': 5,
            'image': portraitImage,
            'order': 2
        },
        {
            'name': 'Marc Lefevre',
            'role': 'Restaurateur',
            'text': "L'agencement complet de notre restaurant a été réalisé avec brio. Le bois apporte une chaleur que nos clients adorent. Service professionnel de A à Z.",
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
            print(f"  + Created: {testimonial.name}")
        else:
            for key, value in data.items():
                if key != 'name':
                    setattr(testimonial, key, value)
            testimonial.save()
            print(f"  * Updated: {testimonial.name}")


def populate_team():
    """Populate team members with real images"""
    print("\nPopulating team members with real images...")

    portraitImage = 'image/atelier-images/proprietaire-costume-assis-planches-atelier.jpg'

    team_data = [
        {
            'name': 'Defehe Kamdem FOBHA Mathurin',
            'role_fr': 'Fondateur et Maître Artisan',
            'role_en': 'Founder and Master Craftsman',
            'experience_years': 20,
            'quote_fr': 'La passion du bois et la satisfaction totale du client sont au cœur de chaque réalisation',
            'quote_en': 'Passion for wood and total customer satisfaction are at the heart of every project',
            'image': portraitImage,
            'order': 1
        }
    ]

    for data in team_data:
        member, created = TeamMember.objects.get_or_create(
            name=data['name'],
            defaults=data
        )
        if created:
            print(f"  + Created: {member.name}")
        else:
            for key, value in data.items():
                if key != 'name':
                    setattr(member, key, value)
            member.save()
            print(f"  * Updated: {member.name}")


def populate_timeline():
    """Populate timeline events"""
    print("\nPopulating timeline...")

    timeline_data = [
        {
            'year': '1999',
            'title_fr': 'Les Débuts',
            'title_en': 'The Beginning',
            'description_fr': "Defehe Kamdem FOBHA Mathurin commence son parcours dans la menuiserie après sa formation technique spécialisée en menuiserie et ébénisterie.",
            'description_en': "Defehe Kamdem FOBHA Mathurin begins his journey in joinery after his specialized technical training in joinery and cabinetmaking.",
            'order': 1
        },
        {
            'year': '2004',
            'title_fr': 'Fondation de DKBOIS',
            'title_en': 'Foundation of DKBOIS',
            'description_fr': 'Création de DKBOIS à Yaoundé, quartier Mendong. L\'entreprise se spécialise dans la menuiserie, l\'ébénisterie et la fabrication de meubles sur mesure.',
            'description_en': 'Creation of DKBOIS in Yaoundé, Mendong neighborhood. The company specializes in joinery, cabinetmaking and custom furniture manufacturing.',
            'order': 2
        },
        {
            'year': '2015',
            'title_fr': 'Expansion & Notoriété',
            'title_en': 'Expansion & Recognition',
            'description_fr': 'Développement de la clientèle à Yaoundé et dans tout le Cameroun. Introduction de la garantie unique "Satisfait ou meuble gratuit".',
            'description_en': 'Client base expansion in Yaoundé and throughout Cameroon. Introduction of the unique guarantee "Satisfied or free furniture".',
            'order': 3
        },
        {
            'year': '2024',
            'title_fr': '20 Ans d\'Excellence',
            'title_en': '20 Years of Excellence',
            'description_fr': 'Plus de 20 ans d\'expertise au service de la satisfaction client. DKBOIS s\'impose comme la référence menuiserie de Yaoundé.',
            'description_en': 'Over 20 years of expertise serving customer satisfaction. DKBOIS establishes itself as the carpentry reference in Yaoundé.',
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
            print(f"  + Created: {event.year} - {event.title_fr}")
        else:
            for key, value in data.items():
                if key not in ['year', 'title_fr']:
                    setattr(event, key, value)
            event.save()
            print(f"  * Updated: {event.year} - {event.title_fr}")


def populate_values():
    """Populate company values"""
    print("\nPopulating company values...")

    values_data = [
        {
            'icon': 'gift',
            'title_fr': 'Satisfait ou Meuble Gratuit',
            'title_en': 'Satisfied or Free Furniture',
            'description_fr': 'Notre garantie unique : si vous n\'êtes pas entièrement satisfait de notre travail, nous vous offrons un meuble de votre choix. C\'est notre engagement envers l\'excellence.',
            'description_en': 'Our unique guarantee: if you are not entirely satisfied with our work, we offer you a piece of furniture of your choice. This is our commitment to excellence.',
            'order': 1
        },
        {
            'icon': 'award',
            'title_fr': 'Excellence & Qualité',
            'title_en': 'Excellence & Quality',
            'description_fr': 'Un savoir-faire traditionnel de 20+ ans allié à une exigence sans compromis dans la qualité de finition de chaque projet.',
            'description_en': '20+ years of traditional expertise combined with uncompromising quality standards in every project finish.',
            'order': 2
        },
        {
            'icon': 'clock',
            'title_fr': 'Respect des Délais',
            'title_en': 'Deadline Compliance',
            'description_fr': 'Le respect des délais de livraison est notre priorité absolue pour assurer votre satisfaction.',
            'description_en': 'Meeting delivery deadlines is our top priority to ensure your satisfaction.',
            'order': 3
        },
        {
            'icon': 'users',
            'title_fr': 'Sur Mesure',
            'title_en': 'Custom Made',
            'description_fr': 'Des solutions uniques adaptées à chaque besoin. Chaque projet est conçu spécifiquement pour vous, à Yaoundé et partout au Cameroun.',
            'description_en': 'Unique solutions adapted to each need. Every project is designed specifically for you, in Yaoundé and throughout Cameroon.',
            'order': 4
        }
    ]

    for data in values_data:
        value, created = CompanyValue.objects.get_or_create(
            title_fr=data['title_fr'],
            defaults=data
        )
        if created:
            print(f"  + Created: {value.title_fr}")
        else:
            for key, value_attr in data.items():
                if key != 'title_fr':
                    setattr(value, key, value_attr)
            value.save()
            print(f"  * Updated: {value.title_fr}")


def populate_faqs():
    """Populate FAQs"""
    print("\nPopulating FAQs...")

    faqs_data = [
        {
            'question_fr': 'Quels sont vos délais de réalisation ?',
            'question_en': 'What are your lead times?',
            'answer_fr': 'Nos délais varient selon la complexité du projet. Comptez généralement 4 à 6 semaines pour un meuble simple et 6 à 10 semaines pour un agencement complet comme une cuisine ou un salon.',
            'answer_en': 'Our lead times vary depending on project complexity. Generally allow 4 to 6 weeks for simple furniture and 6 to 10 weeks for a complete fit-out like a kitchen or living room.',
            'order': 1
        },
        {
            'question_fr': 'Travaillez-vous dans tout le Cameroun ?',
            'question_en': 'Do you work throughout Cameroon?',
            'answer_fr': 'Oui, bien que notre atelier soit basé à Yaoundé (quartier Mendong), nous livrons et installons nos créations dans tout le Cameroun.',
            'answer_en': 'Yes, although our workshop is based in Yaoundé (Mendong neighborhood), we deliver and install our creations throughout Cameroon.',
            'order': 2
        },
        {
            'question_fr': 'Quelle est votre garantie qualité ?',
            'question_en': 'What is your quality guarantee?',
            'answer_fr': 'Nous offrons une garantie unique "Satisfait ou meuble gratuit". Si vous n\'êtes pas entièrement satisfait de notre travail, nous vous offrons un meuble de votre choix. Cette garantie témoigne de notre confiance absolue dans la qualité de notre travail.',
            'answer_en': 'We offer a unique "Satisfied or free furniture" guarantee. If you are not entirely satisfied with our work, we offer you a piece of furniture of your choice. This guarantee testifies to our absolute confidence in the quality of our work.',
            'order': 3
        }
    ]

    for data in faqs_data:
        faq, created = FAQ.objects.get_or_create(
            question_fr=data['question_fr'],
            defaults=data
        )
        if created:
            print(f"  + Created: {faq.question_fr}")
        else:
            for key, value in data.items():
                if key != 'question_fr':
                    setattr(faq, key, value)
            faq.save()
            print(f"  * Updated: {faq.question_fr}")


def clean_database():
    """Clean existing data before repopulation"""
    print("\nCleaning existing data...")

    Project.objects.all().delete()
    Service.objects.all().delete()
    Testimonial.objects.all().delete()
    TeamMember.objects.all().delete()
    TimelineEvent.objects.all().delete()
    CompanyValue.objects.all().delete()
    FAQ.objects.all().delete()

    print("  [*] All existing data cleared")


def main():
    """Main function to populate all data"""
    print("=" * 70)
    print(" DKBOIS Database Population Script - REAL LOCAL IMAGES")
    print("=" * 70)

    # Clean existing data first
    clean_database()

    populate_projects()
    populate_services()
    populate_testimonials()
    populate_team()
    populate_timeline()
    populate_values()
    populate_faqs()

    print("\n" + "=" * 70)
    print(" Database population complete with REAL images!")
    print("=" * 70)
    print("\nAll images now use local paths from the 'image/' folder")
    print("You can view the updated content at:")
    print("  - API: http://localhost:3000/api/")
    print("  - Admin: http://localhost:3000/admin/")


if __name__ == '__main__':
    main()
