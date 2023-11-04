# 🌐 Netzwerkscanner-Tool

Dieses Tool dient als Netzwerkscanner, der mit einem Raspberry Pi 🍓 und einer Webanwendung arbeitet, um Geräte im lokalen Netzwerk zu identifizieren und Informationen über diese Geräte, wie z.B. offene Ports, anzuzeigen.

## ✨ Features

- Netzwerkscan zur Identifizierung aller Geräte im Netzwerk 🖥️
- Anzeige von Informationen zu jedem Gerät, einschließlich offener Ports 🔍
- Interaktive Netzwerktopologie, die im Webbrowser visualisiert wird 🕸️
- Einfache Installation und Konfiguration auf Raspberry Pi 🛠️

## 📋 Voraussetzungen

Bevor Sie beginnen, stellen Sie sicher, dass die folgenden Voraussetzungen erfüllt sind:

- Ein Raspberry Pi (3B oder neuer) mit Raspbian OS installiert 🍓
- Netzwerkzugang und die Berechtigung, Scans in diesem Netzwerk durchzuführen 🔑
- `nmap` muss auf dem Raspberry Pi installiert sein 🧰
- `python3` und `pip` müssen auf dem System vorhanden sein 🐍

## 🚀 Installation

Um das Tool zu installieren, folgen Sie diesen Schritten:

1. Klone das Repository auf deinen Raspberry Pi:

   ```bash
   git clone https://github.com/your-username/netzwerkscanner-tool.git
   cd netzwerkscanner-tool
   ```

2. Führe das Installationsskript aus (für Unix-ähnliche Systeme):

   ```bash
   ./install.sh
   ```

   Für Windows-Benutzer:

   ```bat
   install.bat
   ```

3. Um die Python-Abhängigkeiten zu installieren, führe das Python-Installations-Skript aus:

   ```bash
   python3 install_requirements.py
   ```

Das Installationsskript wird alle benötigten Abhängigkeiten installieren und die Anwendung für den Einsatz vorbereiten.

## ⚙️ Konfiguration

Nach der Installation müssen Sie die `config.json` Datei entsprechend Ihrem Netzwerk anpassen. Stellen Sie sicher, dass Sie die richtige Subnetzmaske und den IP-Bereich für das Netzwerkscanning angeben.

## 🖥️ Verwendung

Nach der Installation und Konfiguration können Sie die Anwendung mit dem folgenden Befehl starten:

```bash
python3 app.py
```

Öffne deinen Webbrowser und gehe zu `http://<Raspberry-Pi-IP>:5000`, um die Anwendung zu verwenden.

## 🤝 Beitrag

Kontributionen sind willkommen! Für große Änderungen bitte zuerst ein Issue eröffnen, um darüber zu diskutieren. 📬

## 📜 Lizenz

[NONE yet](LICENSE)
