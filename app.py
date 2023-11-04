from flask import Flask, jsonify
import subprocess
import re

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('templates/index.html')

@app.route('/scan', methods=['GET'])
def scan():
    # Der Befehl, um einen schnellen Scan der meistgenutzten Ports durchzuführen.
    # Sie können die Optionen ändern, um einen vollständigen Scan oder einen spezifischen Port-Scan durchzuführen.
    command = ["nmap", "-T4", "-F", "192.168.0.1-255"]
    
    # Führen Sie den nmap-Befehl aus
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    # Verarbeiten Sie das Ergebnis des nmap-Befehls
    devices = []
    output = result.stdout
    ip_addresses = re.findall(r'Nmap scan report for (.*?)\n', output)
    port_info = re.findall(r'(\d+/tcp.*?)\n', output)

    for i, ip in enumerate(ip_addresses):
        ports = port_info[i].split(', ') if i < len(port_info) else []
        devices.append({"ip": ip, "ports": ports})

    # Gibt die gescannten Geräte und ihre Ports als JSON zurück
    return jsonify(devices)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
