import json
import time
import random

# Definició de les dades inicials
dades_satelit = {
    "temperatura": 25.0,
    "bateria": 100
}

print("Iniciant simulació amb sortida JSON...")

try:
    while True:
        # 1. Simulem canvis en els valors
        dades_satelit["temperatura"] = round(random.uniform(20.0, 30.0), 1)
        dades_satelit["bateria"] -= 1
        
        # 2. Guardem les dades en un fitxer JSON
        with open("dades_satelit.json", "w") as fitxer:
            json.dump(dades_satelit, fitxer)
            
        print(f"Dades actualitzades: {dades_satelit}")
        
        # 3. Espera d'un segon
        time.sleep(1)
except KeyboardInterrupt:
    print("\nSimulació aturada.")
