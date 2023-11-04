#!/bin/bash

# Funktion zur Überprüfung, ob ein Befehl verfügbar ist
command_exists () {
    type "$1" &> /dev/null ;
}

echo "Beginne mit der Installation des Netzwerkscanner-Tools..."

# Überprüfe, ob Homebrew auf macOS installiert ist
if [[ "$OSTYPE" == "darwin"* ]]; then
    if ! command_exists brew ; then
        echo "Homebrew wird benötigt, aber nicht gefunden. Bitte installiere Homebrew."
        exit 1
    fi
fi

# Installiere nmap, falls nicht vorhanden
if ! command_exists nmap ; then
    echo "nmap wird benötigt, aber nicht gefunden. Installiere nmap..."
    if [[ "$OSTYPE" == "darwin"* ]]; then
        brew install nmap
    else
        sudo apt-get update
        sudo apt-get install -y nmap
    fi
fi

# Überprüfe, ob Python und Pip installiert sind
if ! command_exists python3 || ! command_exists pip3 ; then
    echo "Python3 und Pip3 werden benötigt, aber nicht gefunden. Bitte installiere Python3 und Pip3."
    exit 1
fi

# Installiere Python-Abhängigkeiten
echo "Installiere Python-Abhängigkeiten..."
pip3 install -r requirements.txt

echo "Installation abgeschlossen. Bitte konfigurieren Sie die Anwendung entsprechend Ihrer Netzwerkumgebung."
