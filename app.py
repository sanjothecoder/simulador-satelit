from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    # Obrim el fitxer on el satèl·lit guarda les dades
    with open('dades_satelit.json', 'r') as f:
        dades = json.load(f)
    return jsonify(dades)

if __name__ == '__main__':
    # El port 5000 és l'estàndard per a Flask
    app.run(host='0.0.0.0', debug=True, port=5000)
