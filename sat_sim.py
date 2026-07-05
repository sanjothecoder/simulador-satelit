import json
import time

bateria_actual = 100
print("Iniciant simulació amb sortida JSON...")

try:
    while True:
        # [La part de llegir l'ordre que ja tens...]
        try:
            with open("ordre_satelit.txt", "r") as f:
                accio = f.read().strip()
        except FileNotFoundError:
            accio = "normal"

        if accio == "camera":
            bateria_actual -= 5
        elif accio == "solar":
            bateria_actual += 2
        else:
            bateria_actual -= 1
        bateria_actual = max(0, min(100, bateria_actual))

        # [La part que faltava]
        dades = {"temperatura": 25.0, "bateria": bateria_actual}
        with open("dades_satelit.json", "w") as f:
            json.dump(dades, f)
        print(f"Dades actualitzades: {dades}")
        time.sleep(1)

except KeyboardInterrupt:
    print("\nSimulació aturada per l'usuari.")
