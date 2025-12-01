# Script de renommage des fichiers IMG-
# Encodage UTF-8

$imageDir = "C:\Users\Darius\Desktop\catalogue Menuserie\image"

# Mapping des anciens noms vers les nouveaux noms
$renameMap = @{
    "IMG-20250906-WA0085.jpg" = "porte-double-bois-clair-panneaux-geometriques-01.jpg";
    "IMG-20250906-WA0086.jpg" = "porte-double-bois-clair-panneaux-geometriques-02.jpg";
    "IMG-20250906-WA0087.jpg" = "porte-simple-bois-clair-panneaux-classiques-01.jpg";
    "IMG-20250906-WA0088.jpg" = "porte-double-bois-clair-panneaux-geometriques-03.jpg";
    "IMG-20250906-WA0089.jpg" = "porte-double-bois-clair-panneaux-geometriques-04.jpg";
    "IMG-20250906-WA0090.jpg" = "lit-bois-fonce-tete-panneau-simple-01.jpg";
    "IMG-20250906-WA0091.jpg" = "lit-bois-fonce-tete-panneau-simple-02.jpg";
    "IMG-20250906-WA0092.jpg" = "lit-bois-fonce-tete-panneau-simple-03.jpg";
    "IMG-20250906-WA0093.jpg" = "table-basse-bois-massif-rectangulaire-01.jpg";
    "IMG-20250906-WA0094.jpg" = "table-basse-bois-massif-rectangulaire-02.jpg";
    "IMG-20250906-WA0095.jpg" = "canape-vert-velours-pieds-bois-01.jpg";
    "IMG-20250906-WA0096.jpg" = "canape-vert-velours-pieds-bois-02.jpg";
    "IMG-20250906-WA0097.jpg" = "fauteuil-vert-velours-pieds-bois-01.jpg";
    "IMG-20250906-WA0098.jpg" = "salon-complet-canape-fauteuils-vert-01.jpg";
    "IMG-20250906-WA0099.jpg" = "fauteuil-vert-velours-pieds-bois-02.jpg";
    "IMG-20250906-WA0100.jpg" = "atelier-fabrication-portes-bois-01.jpg";
    "IMG-20250906-WA0101.jpg" = "porte-simple-bois-clair-moderne-01.jpg";
    "IMG-20250906-WA0102.jpg" = "porte-double-bois-clair-vitree-01.jpg";
    "IMG-20250906-WA0103.jpg" = "porte-simple-bois-clair-moderne-02.jpg";
    "IMG-20250906-WA0104.jpg" = "porte-simple-bois-clair-moderne-03.jpg";
    "IMG-20250906-WA0105.jpg" = "commode-bois-fonce-tiroirs-01.jpg";
    "IMG-20250906-WA0106.jpg" = "table-ronde-bois-fonce-pied-central-01.jpg";
    "IMG-20250906-WA0107.jpg" = "commode-bois-fonce-tiroirs-02.jpg";
    "IMG-20250906-WA0108.jpg" = "table-ronde-bois-fonce-pied-central-02.jpg";
    "IMG-20250906-WA0109.jpg" = "porte-simple-bois-clair-panneaux-01.jpg";
    "IMG-20250906-WA0110.jpg" = "porte-double-bois-clair-asymetrique-01.jpg";
    "IMG-20250906-WA0111.jpg" = "porte-simple-bois-clair-panneaux-02.jpg";
    "IMG-20250906-WA0112.jpg" = "porte-simple-bois-clair-panneaux-03.jpg";
    "IMG-20250906-WA0113.jpg" = "porte-simple-bois-clair-panneaux-04.jpg";
    "IMG-20250906-WA0114.jpg" = "commode-bois-fonce-tiroirs-03.jpg";
    "IMG-20250906-WA0115.jpg" = "atelier-fabrication-meubles-01.jpg";
    "IMG-20250906-WA0116.jpg" = "atelier-fabrication-meubles-02.jpg";
    "IMG-20250906-WA0117.jpg" = "atelier-fabrication-meubles-03.jpg";
    "IMG-20250906-WA0118.jpg" = "atelier-fabrication-meubles-04.jpg";
    "IMG-20250906-WA0119.jpg" = "atelier-fabrication-meubles-05.jpg";
    "IMG-20250906-WA0120.jpg" = "atelier-fabrication-meubles-06.jpg";
    "IMG-20250906-WA0121.jpg" = "porte-simple-bois-clair-lamelles-01.jpg";
    "IMG-20250906-WA0122.jpg" = "porte-simple-bois-clair-lamelles-02.jpg";
    "IMG-20250906-WA0123.jpg" = "porte-simple-bois-clair-lamelles-03.jpg";
    "IMG-20250906-WA0124.jpg" = "commode-bois-fonce-moderne-01.jpg";
    "IMG-20250906-WA0125.jpg" = "commode-bois-fonce-moderne-02.jpg";
    "IMG-20250906-WA0126.jpg" = "porte-simple-bois-clair-moderne-04.jpg";
    "IMG-20250906-WA0127.jpg" = "porte-simple-bois-clair-moderne-05.jpg";
    "IMG-20250906-WA0128.jpg" = "commode-bois-fonce-tiroirs-04.jpg";
    "IMG-20250906-WA0129.jpg" = "porte-simple-bois-clair-panneau-central-01.jpg";
    "IMG-20250906-WA0130.jpg" = "porte-simple-bois-clair-panneau-central-02.jpg";
    "IMG-20250906-WA0131.jpg" = "table-basse-bois-massif-moderne-01.jpg";
    "IMG-20250906-WA0132.jpg" = "commode-bois-fonce-classique-01.jpg";
    "IMG-20250906-WA0133.jpg" = "porte-simple-bois-clair-design-moderne-01.jpg";
    "IMG-20250906-WA0134.jpg" = "porte-simple-bois-clair-design-moderne-02.jpg";
    "IMG-20250906-WA0135.jpg" = "porte-simple-bois-clair-design-moderne-03.jpg";
    "IMG-20250906-WA0136.jpg" = "table-basse-bois-massif-moderne-02.jpg";
    "IMG-20250906-WA0137.jpg" = "commode-bois-fonce-classique-02.jpg";
    "IMG-20250906-WA0138.jpg" = "commode-bois-fonce-classique-03.jpg";
    "IMG-20250906-WA0139.jpg" = "commode-bois-fonce-moderne-03.jpg";
    "IMG-20250906-WA0140.jpg" = "commode-bois-fonce-moderne-04.jpg";
    "IMG-20250906-WA0141.jpg" = "table-basse-bois-massif-rectangulaire-03.jpg";
    "IMG-20250906-WA0142.jpg" = "porte-simple-bois-clair-panneau-vitre-01.jpg";
    "IMG-20250906-WA0143.jpg" = "porte-simple-bois-clair-panneau-vitre-02.jpg";
    "IMG-20250906-WA0144.jpg" = "table-ronde-bois-fonce-moderne-01.jpg";
    "IMG-20250906-WA0145.jpg" = "commode-bois-fonce-tiroirs-05.jpg";
    "IMG-20250906-WA0146.jpg" = "porte-simple-bois-clair-classique-01.jpg";
    "IMG-20250906-WA0147.jpg" = "porte-simple-bois-clair-classique-02.jpg";
    "IMG-20250906-WA0148.jpg" = "commode-bois-fonce-tiroirs-06.jpg";
    "IMG-20250906-WA0149.jpg" = "porte-simple-bois-clair-classique-03.jpg";
    "IMG-20250906-WA0150.jpg" = "table-basse-bois-massif-carree-01.jpg";
    "IMG-20250906-WA0151.jpg" = "porte-simple-bois-clair-moderne-06.jpg";
    "IMG-20250906-WA0152.jpg" = "porte-double-bois-clair-moderne-01.jpg";
    "IMG-20250906-WA0153.jpg" = "commode-bois-fonce-moderne-05.jpg";
    "IMG-20250906-WA0154.jpg" = "commode-bois-fonce-moderne-06.jpg";
    "IMG-20250906-WA0155.jpg" = "atelier-fabrication-portes-bois-02.jpg";
    "IMG-20250906-WA0156.jpg" = "porte-simple-bois-clair-moderne-07.jpg";
    "IMG-20250906-WA0157.jpg" = "atelier-fabrication-portes-bois-03.jpg";
    "IMG-20250906-WA0158.jpg" = "table-basse-bois-massif-carree-02.jpg";
    "IMG-20250906-WA0159.jpg" = "porte-double-bois-clair-moderne-02.jpg";
    "IMG-20250906-WA0160.jpg" = "table-basse-bois-massif-moderne-03.jpg";
    "IMG-20250906-WA0161.jpg" = "atelier-fabrication-meubles-07.jpg";
    "IMG-20250906-WA0162.jpg" = "atelier-fabrication-meubles-08.jpg";
    "IMG-20250906-WA0163.jpg" = "atelier-fabrication-meubles-09.jpg";
    "IMG-20250906-WA0164.jpg" = "porte-simple-bois-clair-moderne-08.jpg";
    "IMG-20250906-WA0165.jpg" = "porte-simple-bois-clair-moderne-09.jpg";
    "IMG-20250906-WA0166.jpg" = "atelier-fabrication-meubles-10.jpg";
    "IMG-20250906-WA0167.jpg" = "atelier-fabrication-meubles-11.jpg";
    "IMG-20250906-WA0168.jpg" = "atelier-fabrication-meubles-12.jpg";
    "IMG-20250906-WA0169.jpg" = "atelier-fabrication-meubles-13.jpg";
    "IMG-20250906-WA0170.jpg" = "atelier-fabrication-meubles-14.jpg";
    "IMG-20250906-WA0171.jpg" = "atelier-fabrication-meubles-15.jpg";
    "IMG-20250906-WA0172.jpg" = "atelier-fabrication-meubles-16.jpg";
    "IMG-20250906-WA0173.jpg" = "atelier-fabrication-meubles-17.jpg";
    "IMG-20250906-WA0174.jpg" = "atelier-fabrication-meubles-18.jpg";
    "IMG-20250906-WA0175.jpg" = "porte-simple-bois-clair-moderne-10.jpg";
    "IMG-20250906-WA0176.jpg" = "porte-simple-bois-clair-moderne-11.jpg";
    "IMG-20250906-WA0177.jpg" = "porte-simple-bois-clair-moderne-12.jpg";
    "IMG-20250906-WA0178.jpg" = "commode-bois-fonce-tiroirs-07.jpg";
    "IMG-20250906-WA0179.jpg" = "commode-bois-fonce-tiroirs-08.jpg";
    "IMG-20250906-WA0180.jpg" = "atelier-fabrication-meubles-19.jpg";
    "IMG-20250906-WA0181.jpg" = "atelier-fabrication-meubles-20.jpg";
    "IMG-20250906-WA0182.jpg" = "atelier-fabrication-meubles-21.jpg";
    "IMG-20250906-WA0183.jpg" = "atelier-fabrication-meubles-22.jpg";
    "IMG-20250906-WA0184.jpg" = "atelier-fabrication-meubles-23.jpg";
    "IMG-20250906-WA0185.jpg" = "atelier-fabrication-meubles-24.jpg";
    "IMG-20250906-WA0186.jpg" = "atelier-fabrication-meubles-25.jpg";
    "IMG-20250906-WA0187.jpg" = "atelier-fabrication-meubles-26.jpg";
    "IMG-20250906-WA0188.jpg" = "atelier-fabrication-meubles-27.jpg";
    "IMG-20250906-WA0189.jpg" = "atelier-fabrication-meubles-28.jpg";
    "IMG-20250906-WA0190.jpg" = "atelier-fabrication-meubles-29.jpg";
    "IMG-20250906-WA0191.jpg" = "atelier-fabrication-meubles-30.jpg";
    "IMG-20250906-WA0192.jpg" = "atelier-fabrication-meubles-31.jpg";
    "IMG-20250906-WA0193.jpg" = "atelier-fabrication-meubles-32.jpg";
    "IMG-20250906-WA0194.jpg" = "porte-simple-bois-clair-moderne-13.jpg";
    "IMG-20250906-WA0195.jpg" = "porte-simple-bois-clair-moderne-14.jpg";
    "IMG-20250906-WA0196.jpg" = "porte-simple-bois-clair-moderne-15.jpg";
    "IMG-20250906-WA0197.jpg" = "commode-bois-fonce-tiroirs-09.jpg";
    "IMG-20250906-WA0198.jpg" = "commode-bois-fonce-moderne-07.jpg";
    "IMG-20250906-WA0199.jpg" = "commode-bois-fonce-moderne-08.jpg";
    "IMG-20250906-WA0200.jpg" = "commode-bois-fonce-tiroirs-10.jpg";
    "IMG-20250906-WA0201.jpg" = "commode-bois-fonce-classique-04.jpg"
}

# Compteurs
$renamed = 0
$skipped = 0
$errors = 0

Write-Host "Debut du renommage des fichiers..." -ForegroundColor Cyan
Write-Host "Repertoire: $imageDir" -ForegroundColor Cyan
Write-Host ""

foreach ($oldName in $renameMap.Keys) {
    $oldPath = Join-Path $imageDir $oldName
    $newName = $renameMap[$oldName]
    $newPath = Join-Path $imageDir $newName
    
    if (Test-Path $oldPath) {
        try {
            if (Test-Path $newPath) {
                Write-Host "ATTENTION: Le fichier $newName existe deja. Ignore." -ForegroundColor Yellow
                $skipped++
            } else {
                Rename-Item -Path $oldPath -NewName $newName -ErrorAction Stop
                Write-Host "OK Renomme: $oldName -> $newName" -ForegroundColor Green
                $renamed++
            }
        } catch {
            Write-Host "ERREUR lors du renommage de $oldName : $_" -ForegroundColor Red
            $errors++
        }
    } else {
        Write-Host "Fichier non trouve: $oldName" -ForegroundColor Red
        $errors++
    }
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Resume du renommage:" -ForegroundColor Cyan
Write-Host "  Fichiers renommes: $renamed" -ForegroundColor Green
Write-Host "  Fichiers ignores: $skipped" -ForegroundColor Yellow
Write-Host "  Erreurs: $errors" -ForegroundColor Red
Write-Host "========================================" -ForegroundColor Cyan
