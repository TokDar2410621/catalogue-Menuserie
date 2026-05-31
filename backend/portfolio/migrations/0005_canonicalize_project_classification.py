"""Convert legacy English codes on Project (category, type, material)
to the French labels now used as canonical values in the admin form."""
from django.db import migrations


CATEGORY_MAP = {
    'kitchen': 'Cuisine',
    'living': 'Salon',
    'exterior': 'Extérieur',
}

TYPE_MAP = {
    'creation': 'Création',
    'restoration': 'Restauration',
    'fitting': 'Agencement',
    'installation': 'Agencement',  # legacy alias from older admin
}

MATERIAL_MAP = {
    'oak': 'Chêne',
    'walnut': 'Noyer',
    'maple': 'Érable',
}


def forwards(apps, schema_editor):
    Project = apps.get_model('portfolio', 'Project')
    for project in Project.objects.all():
        new_category = CATEGORY_MAP.get(project.category, project.category)
        new_type = TYPE_MAP.get(project.type, project.type)
        new_material = MATERIAL_MAP.get(project.material, project.material)
        if (new_category != project.category
                or new_type != project.type
                or new_material != project.material):
            project.category = new_category
            project.type = new_type
            project.material = new_material
            project.save(update_fields=['category', 'type', 'material'])


def backwards(apps, schema_editor):
    Project = apps.get_model('portfolio', 'Project')
    inverse_category = {v: k for k, v in CATEGORY_MAP.items()}
    inverse_type = {'Création': 'creation', 'Restauration': 'restoration', 'Agencement': 'fitting'}
    inverse_material = {v: k for k, v in MATERIAL_MAP.items()}
    for project in Project.objects.all():
        project.category = inverse_category.get(project.category, project.category)
        project.type = inverse_type.get(project.type, project.type)
        project.material = inverse_material.get(project.material, project.material)
        project.save(update_fields=['category', 'type', 'material'])


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_alter_project_category_alter_project_material_and_more'),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]
