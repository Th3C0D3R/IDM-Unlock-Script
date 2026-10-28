$basePath = "HKCU:\Software\Classes\CLSID"

Get-ChildItem $basePath -ErrorAction SilentlyContinue | ForEach-Object {
    $key = $_
    $props = Get-ItemProperty -Path $key.PSPath -ErrorAction SilentlyContinue
    
    # Prüfen, ob die IDM-Signaturwerte vorhanden sind
    if ($props.MData -or $props.Therad -or $props.Model) {
        Write-Host "IDM-Schlüssel gefunden: $($key.Name)" -ForegroundColor Yellow
        
        # Schlüssel löschen
        Remove-Item -Path $key.PSPath -Recurse -Force -ErrorAction SilentlyContinue
        Write-Host "-> Gelöscht!" -ForegroundColor Green
    }
}