from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dades')
def dades():
    with open('dades_satelit.json', 'r') as f:
        dades = json.load(f)
    return jsonify(dades)

@app.route('/ordre', methods=['POST'])
def ordre():
    data = request.json
    accio = data.get('accio')
    with open('ordre_satelit.txt', 'w') as f:
        f.write(accio)
    return {"status": "success", "ordre": accio}

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)


