# -*- coding: utf-8 -*-
"""
Script pour sauvegarder l'analyse progressive des 169 images
"""
import os

# Lister tous les fichiers
fichiers = sorted([f for f in os.listdir('.') if f.endswith('.jpg')])

print(f"Total fichiers: {len(fichiers)}\n")

# Fichier de sortie pour l'analyse
with open('analyse-images-temp.txt', 'w', encoding='utf-8') as f:
    f.write(f"ANALYSE DES {len(fichiers)} IMAGES\n")
    f.write("="*80 + "\n\n")

    for i, fichier in enumerate(fichiers, 1):
        f.write(f"{i:3d}. {fichier}\n")
        f.write(f"     VRAI NOM: [À COMPLÉTER]\n\n")

print("Fichier 'analyse-images-temp.txt' créé")
print("Vous pouvez maintenant compléter l'analyse image par image")
