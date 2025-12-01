#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de renommage automatique des images
Associe chaque image (ordre alphabétique) avec le nom correspondant dans noms-images.txt
"""

import os
import sys

def renommer_images():
    # Dossier contenant les images
    dossier = os.path.dirname(os.path.abspath(__file__))
    fichier_noms = os.path.join(dossier, 'noms-images.txt')

    # Vérifier que le fichier des noms existe
    if not os.path.exists(fichier_noms):
        print(f"[ERREUR] Le fichier {fichier_noms} n'existe pas!")
        return False

    # Lire les nouveaux noms depuis le fichier
    with open(fichier_noms, 'r', encoding='utf-8') as f:
        nouveaux_noms = [ligne.strip() for ligne in f if ligne.strip()]

    # Lister tous les fichiers .jpg dans le dossier (ordre alphabétique)
    fichiers_actuels = sorted([
        f for f in os.listdir(dossier)
        if f.lower().endswith('.jpg') and f != 'exemple.jpg'
    ])

    print(f"\n{'='*80}")
    print(f"DOSSIER: {dossier}")
    print(f"Fichiers trouves: {len(fichiers_actuels)}")
    print(f"Nouveaux noms: {len(nouveaux_noms)}")
    print(f"{'='*80}\n")

    # Vérifier que le nombre correspond
    if len(fichiers_actuels) != len(nouveaux_noms):
        print(f"[ERREUR] Le nombre de fichiers ({len(fichiers_actuels)}) ne correspond pas")
        print(f"         au nombre de noms ({len(nouveaux_noms)}) dans le fichier!")
        return False

    # Afficher les 10 premières correspondances
    print("APERCU DES 10 PREMIERES CORRESPONDANCES:\n")
    for i in range(min(10, len(fichiers_actuels))):
        print(f"  {i+1:3d}. {fichiers_actuels[i]:50s} -> {nouveaux_noms[i]}")

    if len(fichiers_actuels) > 10:
        print(f"\n  ... et {len(fichiers_actuels) - 10} autres fichiers\n")

    # Afficher les 5 dernières correspondances
    if len(fichiers_actuels) > 10:
        print("APERCU DES 5 DERNIERES CORRESPONDANCES:\n")
        for i in range(max(0, len(fichiers_actuels) - 5), len(fichiers_actuels)):
            print(f"  {i+1:3d}. {fichiers_actuels[i]:50s} -> {nouveaux_noms[i]}")
        print()

    # Demander confirmation
    print(f"{'='*80}")
    reponse = input("\n[!] Voulez-vous renommer tous ces fichiers? (oui/non): ").strip().lower()

    if reponse not in ['oui', 'o', 'yes', 'y']:
        print("\n[ANNULE] Renommage annule.")
        return False

    # Créer un dossier temporaire pour éviter les conflits
    temp_prefix = "TEMP_RENAME_"

    # Étape 1: Renommer tous les fichiers avec un préfixe temporaire
    print(f"\n{'='*80}")
    print("ETAPE 1/2: Renommage temporaire...")
    print(f"{'='*80}\n")

    temp_noms = []
    for i, ancien_nom in enumerate(fichiers_actuels):
        ancien_chemin = os.path.join(dossier, ancien_nom)
        temp_nom = f"{temp_prefix}{i:04d}.jpg"
        temp_chemin = os.path.join(dossier, temp_nom)
        temp_noms.append(temp_nom)

        try:
            os.rename(ancien_chemin, temp_chemin)
            if (i + 1) % 20 == 0:
                print(f"  [OK] {i+1}/{len(fichiers_actuels)} fichiers traites...")
        except Exception as e:
            print(f"  [ERREUR] Erreur lors du renommage de {ancien_nom}: {e}")
            return False

    print(f"  [OK] {len(fichiers_actuels)}/{len(fichiers_actuels)} fichiers renommes temporairement\n")

    # Étape 2: Renommer avec les noms finaux
    print(f"{'='*80}")
    print("ETAPE 2/2: Renommage final...")
    print(f"{'='*80}\n")

    succes = 0
    echecs = []

    for i, temp_nom in enumerate(temp_noms):
        temp_chemin = os.path.join(dossier, temp_nom)
        nouveau_nom = nouveaux_noms[i]
        nouveau_chemin = os.path.join(dossier, nouveau_nom)

        try:
            os.rename(temp_chemin, nouveau_chemin)
            succes += 1
            if (i + 1) % 20 == 0:
                print(f"  [OK] {i+1}/{len(temp_noms)} fichiers renommes...")
        except Exception as e:
            print(f"  [ERREUR] Erreur: {temp_nom} -> {nouveau_nom}: {e}")
            echecs.append((temp_nom, nouveau_nom, str(e)))

    print(f"  [OK] {succes}/{len(temp_noms)} fichiers renommes avec succes\n")

    # Afficher le résumé
    print(f"{'='*80}")
    print("RESUME DU RENOMMAGE")
    print(f"{'='*80}\n")
    print(f"  [SUCCES] Fichiers renommes: {succes}")

    if echecs:
        print(f"  [ECHECS] Echecs: {len(echecs)}")
        print("\n  Details des echecs:")
        for temp, nouveau, erreur in echecs:
            print(f"    - {temp} -> {nouveau}")
            print(f"      Erreur: {erreur}")
    else:
        print(f"  [ECHECS] Echecs: 0")
        print(f"\n  [SUCCES] Tous les fichiers ont ete renommes avec succes!")

    print(f"\n{'='*80}\n")
    return True

if __name__ == "__main__":
    try:
        renommer_images()
    except KeyboardInterrupt:
        print("\n\n[ANNULE] Interruption par l'utilisateur. Renommage annule.")
        sys.exit(1)
    except Exception as e:
        print(f"\n[ERREUR] ERREUR INATTENDUE: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
