import time
import random

def log(msg):
    print(msg)
    time.sleep(1)

def random_ip():
    return f"{random.randint(10, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 254)}"

def random_processes():
    return random.randint(1, 5)

log("Initialisiere Überwachung...")
log("Tracking: Tastaturaktivität...")
log("Verdächtige Eingabe erkannt: sudo rm -rf")
log(f"Prozess-Scan: {random_processes()} Programme im Hintergrund")
log(f"Ortung: IP-Adresse {random_ip()}")
log("Status: Überwachung aktiv")
log("...")
log("Nur ein Fake. Hacker.exe war hier 😎")