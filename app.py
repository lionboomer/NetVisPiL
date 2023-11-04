from flask import Flask, jsonify
import subprocess
import re

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scan', methods=['GET'])
def scan():
    command = ["nmap", "-T4", "-F", "192.168.0.1-255"]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    devices = []
    output = result.stdout
    ip_addresses = re.findall(r'Nmap scan report for (.*?)\n', output)
    port_info = re.findall(r'(\d+/tcp.*?)\n', output)

    for i, ip in enumerate(ip_addresses):
        ports = port_info[i].split(', ') if i < len(port_info) else []
        hostname = re.search(r'\((.+)\)', ip)  # Extrahieren des Hostnamens, falls vorhanden
        if hostname:
            hostname = hostname.group(1)
            ip = ip.split(' ')[0]  # Extrahieren der IP-Adresse
        else:
            hostname = ''  # Kein Hostname verfügbar
        devices.append({"ip": ip, "hostname": hostname, "ports": ports})

    return jsonify(devices)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
