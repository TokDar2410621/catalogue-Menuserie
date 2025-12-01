# -*- coding: utf-8 -*-
import os

# Dossier des images
dossier = os.path.dirname(os.path.abspath(__file__))

# Lister tous les JPG dans l'ordre alphabétique
fichiers = sorted([f for f in os.listdir(dossier) if f.lower().endswith('.jpg')])

print(f"Total: {len(fichiers)} fichiers\n")
print("Premier fichier:", fichiers[0] if fichiers else "Aucun")
print("Dernier fichier:", fichiers[-1] if fichiers else "Aucun")
print("\nPremiers 10 fichiers:")
for i, f in enumerate(fichiers[:10], 1):
    print(f"  {i}. {f}")
