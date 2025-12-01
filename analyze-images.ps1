# Script pour lister tous les fichiers IMG- et préparer le renommage
$imageDir = "C:\Users\Darius\Desktop\catalogue Menuserie\image"
$outputFile = "C:\Users\Darius\Desktop\catalogue Menuserie\renaming-map.csv"

# Récupérer tous les fichiers IMG-
$imgFiles = Get-ChildItem -Path $imageDir -Filter "IMG-20250906-WA*.jpg" | Sort-Object Name

# Créer le fichier CSV
$results = @()
foreach ($file in $imgFiles) {
    $results += [PSCustomObject]@{
        OldName = $file.Name
        NewName = ""  # À remplir manuellement ou par analyse
        Size = $file.Length
        Path = $file.FullName
    }
}

# Exporter vers CSV
$results | Export-Csv -Path $outputFile -NoTypeInformation -Encoding UTF8

Write-Host "Analyse terminée. $($imgFiles.Count) fichiers trouvés."
Write-Host "Fichier de mapping créé: $outputFile"
Write-Host ""
Write-Host "Liste des fichiers:"
$imgFiles | ForEach-Object { Write-Host "  - $($_.Name)" }
