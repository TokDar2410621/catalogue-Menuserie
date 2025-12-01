"""
Script pour mettre à jour les images de la base de données
avec les vraies images du dossier image/
"""
import os
import sys
import django

# Configuration Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SECRET_KEY', 'django-insecure-dev-key-for-local-only')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dkbois_backend.settings')
django.setup()

from portfolio.models import Project, Service, Testimonial, TeamMember

def get_image_files():
    """Récupère toutes les images du dossier image/"""
    image_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'image')

    if not os.path.exists(image_dir):
        print(f"[ERREUR] Le dossier {image_dir} n'existe pas!")
        return []

    # Récupérer tous les fichiers .jpg
    images = sorted([f for f in os.listdir(image_dir) if f.lower().endswith('.jpg')])
    print(f"[OK] {len(images)} images trouvees dans le dossier image/")
    return images

def distribute_images(images, num_groups, images_per_group):
    """Distribue les images en groupes"""
    groups = []
    start = 0

    for i in range(num_groups):
        end = start + images_per_group
        group = images[start:end] if end <= len(images) else images[start:]
        groups.append(group)
        start = end

        if start >= len(images):
            break

    return groups

def update_projects():
    """Met à jour les images des projets"""
    print("\n[PROJETS] Mise a jour des projets...")

    images = get_image_files()
    if not images:
        return

    projects = Project.objects.all().order_by('id')

    # Distribuer les images: 6 images par projet
    images_per_project = 6
    project_image_groups = distribute_images(images, len(projects), images_per_project)

    for i, project in enumerate(projects):
        if i < len(project_image_groups):
            # Prendre la première image comme image principale
            main_image = f"image/{project_image_groups[i][0]}" if project_image_groups[i] else "image/IMG-20250906-WA0002.jpg"

            # Les autres images pour la galerie
            gallery_images = [f"image/{img}" for img in project_image_groups[i][1:]] if len(project_image_groups[i]) > 1 else []

            project.image = main_image
            project.images = gallery_images
            project.save()

            print(f"  [OK] {project.title_fr}: {main_image} + {len(gallery_images)} images de galerie")

def update_services():
    """Met à jour les images des services"""
    print("\n[SERVICES] Mise a jour des services...")

    images = get_image_files()
    if not images:
        return

    services = Service.objects.all().order_by('id')

    # Distribuer les images: 4 images par service
    images_per_service = 4
    # Commencer après les images des projets (environ 30 images utilisées)
    service_images = images[30:]
    service_image_groups = distribute_images(service_images, len(services), images_per_service)

    for i, service in enumerate(services):
        if i < len(service_image_groups):
            # Prendre la première image comme image principale
            main_image = f"image/{service_image_groups[i][0]}" if service_image_groups[i] else "image/IMG-20250906-WA0050.jpg"

            # Les autres images pour la galerie
            gallery_images = [f"image/{img}" for img in service_image_groups[i][1:]] if len(service_image_groups[i]) > 1 else []

            service.image = main_image
            service.images = gallery_images
            service.save()

            print(f"  [OK] {service.title_fr}: {main_image} + {len(gallery_images)} images")

def update_testimonials():
    """Met à jour les images des témoignages (portraits)"""
    print("\n[TEMOIGNAGES] Mise a jour des temoignages...")

    images = get_image_files()
    if not images:
        return

    testimonials = Testimonial.objects.all().order_by('order')

    # Utiliser des images de la fin pour les portraits
    portrait_images = images[-20:]  # Dernières 20 images

    for i, testimonial in enumerate(testimonials):
        if i < len(portrait_images):
            testimonial.image = f"image/{portrait_images[i]}"
            testimonial.save()
            print(f"  [OK] {testimonial.name}: {testimonial.image}")

def update_team():
    """Met à jour les images de l'équipe"""
    print("\n[EQUIPE] Mise a jour de l'equipe...")

    images = get_image_files()
    if not images:
        return

    team_members = TeamMember.objects.all().order_by('id')

    # Utiliser des images du milieu pour les photos d'équipe
    team_images = images[60:80]  # Images 60-80

    for i, member in enumerate(team_members):
        if i < len(team_images):
            member.image = f"image/{team_images[i]}"
            member.save()
            print(f"  [OK] {member.name}: {member.image}")

def main():
    print("=" * 60)
    print("MISE A JOUR DES IMAGES AVEC LES VRAIES PHOTOS LOCALES")
    print("=" * 60)

    try:
        update_projects()
        update_services()
        update_testimonials()
        update_team()

        print("\n" + "=" * 60)
        print("MISE A JOUR TERMINEE AVEC SUCCES!")
        print("=" * 60)
        print("\nLes images sont maintenant:")
        print("   - Projets: image/IMG-*.jpg (6 images par projet)")
        print("   - Services: image/IMG-*.jpg (4 images par service)")
        print("   - Temoignages: image/IMG-*.jpg (portraits)")
        print("   - Equipe: image/IMG-*.jpg (photos)")
        print("\nRechargez la page d'accueil pour voir les changements!")

    except Exception as e:
        print(f"\nErreur: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
