# -*- coding: utf-8 -*-
"""
Script pour renommer les 20 premières images selon l'analyse visuelle réelle
"""
import os

# Chemins
dossier = r'c:\Users\Darius\Desktop\catalogue Menuserie\image'
fichier_noms = os.path.join(dossier, 'vrais-noms-20.txt')

def renommer_20_images():
    # Lire les nouveaux noms
    with open(fichier_noms, 'r', encoding='utf-8') as f:
        nouveaux_noms = [ligne.strip() for ligne in f if ligne.strip()]

    # Vérifier qu'on a bien 20 noms
    if len(nouveaux_noms) != 20:
        print(f"ERREUR: Le fichier contient {len(nouveaux_noms)} noms au lieu de 20")
        return

    # Lister tous les fichiers JPG (sauf exemple.jpg) et trier par ordre alphabétique
    fichiers_actuels = sorted([
        f for f in os.listdir(dossier)
        if f.lower().endswith('.jpg') and f != 'exemple.jpg'
    ])

    # Prendre seulement les 20 premiers
    fichiers_a_renommer = fichiers_actuels[:20]

    print(f"Fichiers a renommer: {len(fichiers_a_renommer)}")
    print(f"Nouveaux noms disponibles: {len(nouveaux_noms)}")
    print()

    # Afficher les correspondances
    print("CORRESPONDANCES:")
    print("="*80)
    for i, (ancien, nouveau) in enumerate(zip(fichiers_a_renommer, nouveaux_noms), 1):
        print(f"{i:2d}. {ancien}")
        print(f"    -> {nouveau}")
        print()

    # Demander confirmation
    reponse = input("\nVoulez-vous proceder au renommage? (oui/non): ")
    if reponse.lower() != 'oui':
        print("Renommage annule")
        return

    # ÉTAPE 1: Renommer vers des noms temporaires pour éviter les conflits
    print("\nETAPE 1: Renommage temporaire...")
    noms_temp = []
    for i, ancien in enumerate(fichiers_a_renommer):
        ancien_chemin = os.path.join(dossier, ancien)
        nom_temp = f"TEMP_RENAME_{i:04d}.jpg"
        temp_chemin = os.path.join(dossier, nom_temp)
        os.rename(ancien_chemin, temp_chemin)
        noms_temp.append(nom_temp)
        print(f"  {ancien} -> {nom_temp}")

    # ÉTAPE 2: Renommer vers les noms finaux
    print("\nETAPE 2: Renommage final...")
    for i, (temp, nouveau) in enumerate(zip(noms_temp, nouveaux_noms)):
        temp_chemin = os.path.join(dossier, temp)
        nouveau_chemin = os.path.join(dossier, nouveau)
        os.rename(temp_chemin, nouveau_chemin)
        print(f"  {temp} -> {nouveau}")

    print(f"\nRenommage termine! {len(fichiers_a_renommer)} fichiers renommes avec succes")

if __name__ == "__main__":
    renommer_20_images()
