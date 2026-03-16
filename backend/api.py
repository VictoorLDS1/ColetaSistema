from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

ENTITIES_FILE = "entities.json"
OCCURENCES_FILE = "occurences.json"

def load_json(filepath, default):
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    return default

def save_json(filepath, data):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

entities = load_json(ENTITIES_FILE, [])
occurences = load_json(OCCURENCES_FILE, [])

@app.route("/entities/<string:bairro>/<string:tipo>", methods=["GET"])
def get_entitities_by_infos(bairro, tipo):

    resultado = []

    for i in entities:
        if i["bairro"] == bairro and i["tipo"] == tipo:
            resultado.append(i)

    return jsonify(resultado), 200

@app.route("/occurences/", methods=["GET"])
def get_occurences():
    return jsonify(occurences), 200

@app.route("/occurences", methods=["POST"])
@app.route("/occurences", methods=["POST"])
def create_occurence():
    data = request.get_json()
    new = data
    occurences.append(new)
    save_json(OCCURENCES_FILE, occurences)
    return jsonify(new), 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)