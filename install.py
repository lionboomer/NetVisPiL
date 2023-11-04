import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def main():
    print("Beginne mit der Installation der Python-Abhängigkeiten...")

    # Lies die requirements.txt Datei und installiere jedes Paket
    with open('requirements.txt', 'r') as f:
        packages = f.readlines()
    
    for package in packages:
        package = package.strip()
        if package:
            try:
                install(package)
                print(f"{package} erfolgreich installiert.")
            except Exception as e:
                print(f"Fehler beim Installieren von {package}: {e}")

    print("Alle Abhängigkeiten wurden installiert.")

if __name__ == "__main__":
    main()
