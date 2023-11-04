@echo off
echo Beginne mit der Installation des Netzwerkscanner-Tools...

:: Überprüfe, ob Chocolatey vorhanden ist
where /q choco
if %errorlevel% neq 0 (
    echo Chocolatey wird benötigt, aber nicht gefunden. Bitte installiere Chocolatey.
    goto end
)

:: Installiere nmap, falls nicht vorhanden
where /q nmap
if %errorlevel% neq 0 (
    echo nmap wird benötigt, aber nicht gefunden. Installiere nmap...
    choco install nmap -y
)

:: Überprüfe, ob Python und Pip installiert sind
where /q python
if %errorlevel% neq 0 (
    echo Python wird benötigt, aber nicht gefunden. Bitte installiere Python.
    goto end
)

:: Installiere Python-Abhängigkeiten
echo Installiere Python-Abhängigkeiten...
python -m pip install -r requirements.txt

echo Installation abgeschlossen. Bitte konfigurieren Sie die Anwendung entsprechend Ihrer Netzwerkumgebung.
:end
