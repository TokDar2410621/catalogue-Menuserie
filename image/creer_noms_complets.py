# -*- coding: utf-8 -*-
import os

# Liste complète des 169 noms dans l'ordre
noms = [
    # 1-2: Artisan
    "artisan-commode-rouge-orange-presentation.jpg",
    "artisan-porte-lamelles-horizontales-presentation.jpg",

    # 3-34: atelier-fabrication-meubles-01 à 32
    "etagere-orange-atelier-construction.jpg",  # 3
    "equipe-installation-etagere-boutique.jpg",  # 4
    "equipe-installation-etagere-boutique-02.jpg",  # 5
    "comptoir-blanc-effet-marbre-atelier.jpg",  # 6
    "table-salle-manger-blanche-chaises-bleues.jpg",  # 7
    "table-salle-manger-blanche-chaises-bleues-02.jpg",  # 8
    "armoire-rouge-brun-etageres-tiroirs.jpg",  # 9
    "armoire-rouge-brun-etageres-tiroirs-02.jpg",  # 10
    "chaises-salle-manger-blanches-assise-noire-lot-4.jpg",  # 11
    "porte-simple-bois-rouge-orange-panneaux-courbes.jpg",  # 12
    "porte-simple-bois-clair-panneaux-courbes-atelier.jpg",  # 13
    "portes-bois-rouge-orange-panneaux-courbes-lot-3.jpg",  # 14
    "plancher-bois-construction-solives.jpg",  # 15
    "plancher-bois-construction-solives-02.jpg",  # 16
    "plancher-bois-fini-installation.jpg",  # 17
    "escalier-bois-construction-atelier.jpg",  # 18
    "proprietaire-atelier-planches-bois-portes-01.jpg",  # 19
    "proprietaire-atelier-planches-bois-portes-02.jpg",  # 20
    "proprietaire-atelier-planches-bois-portes-03.jpg",  # 21
    "proprietaire-atelier-rabot-planches-bois-01.jpg",  # 22
    "proprietaire-atelier-rabot-planches-bois-02.jpg",  # 23
    "proprietaire-atelier-rabot-planches-bois-03.jpg",  # 24
    "proprietaire-atelier-assis-planches-bois-01.jpg",  # 25
    "proprietaire-atelier-assis-planches-bois-02.jpg",  # 26
    "proprietaire-atelier-debout-planches-bois.jpg",  # 27
    "plafond-bois-chevron-poutres-01.jpg",  # 28
    "plafond-bois-chevron-poutres-02.jpg",  # 29
    "artisan-installation-plafond-bois-chevron-01.jpg",  # 30
    "artisan-installation-plafond-bois-chevron-02.jpg",  # 31
    "plafond-bois-chevron-caissons-poutres.jpg",  # 32

    # 35-37: atelier-fabrication-portes-bois
    "atelier-fabrication-portes-bois-01.jpg",  # 35
    "atelier-fabrication-portes-bois-02.jpg",  # 36
    "atelier-fabrication-portes-bois-03.jpg",  # 37
]

# Lire le fichier existant et prendre les noms à partir de la ligne 22 (index 21)
with open('noms-images.txt', 'r', encoding='utf-8') as f:
    lignes = [l.strip() for l in f if l.strip()]

# Ajouter les lignes 22 à 165 du fichier existant (qui correspondent aux positions 38-169)
noms.extend(lignes[21:])

# Vérifier
print(f"Total noms créés: {len(noms)}")

# Écrire dans le nouveau fichier
with open('noms-images-complet.txt', 'w', encoding='utf-8') as f:
    for nom in noms:
        f.write(nom + '\n')

print(f"Fichier 'noms-images-complet.txt' créé avec {len(noms)} lignes")
