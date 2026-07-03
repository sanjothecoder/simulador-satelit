import json
import time
import random

# 1. Definim una variable inicial per a la bateria fora del diccionari
bateria_actual = 100 

dades_satelit = {
    "temperatura": 25.0,
    "bateria": bateria_actual
}

print("Iniciant simulació amb sortida JSON...")

try:
    while True:
        # 1. Simulem canvis
        dades_satelit["temperatura"] = round(random.uniform(20.0, 30.0), 1)
        
        # Restem bateria i apliquem el límit (clamping) aquí mateix
        bateria_actual -= 1
        if bateria_actual < 0:
            bateria_actual = 100 # Reiniciem a 100 si arriba a 0
            
        dades_satelit["bateria"] = bateria_actual

        # 2. Guardem
        with open("dades_satelit.json", "w") as fitxer:
            json.dump(dades_satelit, fitxer)

        print(f"Dades actualitzades: {dades_satelit}")
        time.sleep(1)
except KeyboardInterrupt:
    print("\nSimulació aturada.")
