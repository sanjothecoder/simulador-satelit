from flask import Flask, render_template, jsonify
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
