# -*- coding: utf-8 -*-
"""
Script pour restaurer TOUS les fichiers renommes vers leurs noms d'origine
"""
import os

dossier = r'c:\Users\Darius\Desktop\catalogue Menuserie\image'

# Mapping inverse: nouveau nom -> nom d'origine
mapping_inverse = {
    'comptoir-blanc-effet-marbre-exterieur.jpg': 'armoire-rouge-brun-etageres-tiroirs-02.jpg',
    'table-blanche-6-chaises-bleues-exterieur.jpg': 'armoire-rouge-brun-etageres-tiroirs.jpg',
    'artisan-selfie-commode-orange-tiroirs.jpg': 'artisan-commode-rouge-orange-atelier-01.jpg',
    'proprietaire-costume-assis-planches-atelier.jpg': 'artisan-installation-plafond-bois-chevron-01.jpg',
    'proprietaire-costume-assis-planches-atelier-02.jpg': 'artisan-installation-plafond-bois-chevron-02.jpg',
    'artisan-selfie-porte-lamelles-horizontales.jpg': 'artisan-porte-bois-clair-lamelles-horizontales-atelier-01.jpg',
    'artisan-installation-plafond-bois-chevron.jpg': 'atelier-fabrication-portes-bois-01.jpg',
    'artisan-installation-plafond-bois-chevron-02.jpg': 'atelier-fabrication-portes-bois-02.jpg',
    'plafond-bois-chevron-caissons-fini.jpg': 'atelier-fabrication-portes-bois-03.jpg',
    'bibliotheque-grise-portes-vertes-basses.jpg': 'bibliotheque-gris-vert-portes-basses-01.jpg',
    'table-blanche-6-chaises-bleues-exterieur-02.jpg': 'bureau-blanc-bibliotheque-chaise-bois-01.jpg',
    'armoire-rouge-brun-etageres-tiroirs.jpg': 'bureau-etude-enfant-rouge-chaise-vert-01.jpg',
    'armoire-rouge-brun-etageres-tiroirs-02.jpg': 'canape-bleu-exterieur-pieds-bois-01.jpg',
    'chaises-blanches-dossier-noir-lot-4.jpg': 'canape-vert-turquoise-velours-atelier-01.jpg',
}

print("Restauration des fichiers renommes...")
for nouveau, original in mapping_inverse.items():
    nouveau_chemin = os.path.join(dossier, nouveau)
    original_chemin = os.path.join(dossier, original)

    if os.path.exists(nouveau_chemin):
        # Verifier si le nom original existe deja
        if os.path.exists(original_chemin):
            print(f"  CONFLIT: {original} existe deja, skip {nouveau}")
        else:
            os.rename(nouveau_chemin, original_chemin)
            print(f"  {nouveau} -> {original}")
    else:
        print(f"  SKIP: {nouveau} n'existe pas")

print("\nRestauration terminee!")
