# -*- coding: utf-8 -*-
"""
Script pour restaurer les fichiers TEMP vers leurs noms d'origine
"""
import os

dossier = r'c:\Users\Darius\Desktop\catalogue Menuserie\image'

# Mapping des fichiers TEMP vers leurs noms d'origine
mapping = {
    'TEMP_RENAME_0014.jpg': 'canape-vert-turquoise-velours-atelier-02.jpg',
    'TEMP_RENAME_0015.jpg': 'canape-vert-velours-pieds-bois-01.jpg',
    'TEMP_RENAME_0016.jpg': 'canape-vert-velours-pieds-bois-02.jpg',
    'TEMP_RENAME_0017.jpg': 'chaises-salle-manger-blanches-assise-noire-lot-4.jpg',
    'TEMP_RENAME_0018.jpg': 'chevet-vert-tiroirs-atelier-02.jpg',
    'TEMP_RENAME_0019.jpg': 'commode-bois-fonce-classique-01.jpg'
}

print("Restauration des fichiers TEMP...")
for temp, original in mapping.items():
    temp_chemin = os.path.join(dossier, temp)
    original_chemin = os.path.join(dossier, original)

    if os.path.exists(temp_chemin):
        os.rename(temp_chemin, original_chemin)
        print(f"  {temp} -> {original}")
    else:
        print(f"  SKIP: {temp} n'existe pas")

print("\nRestauration terminee!")
