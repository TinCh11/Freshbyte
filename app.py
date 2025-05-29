from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Carga del modelo
with open("modelo.pkl", "rb") as f:
    modelo = pickle.load(f)

@app.route("/")
def home():
    return "API corriendo!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No se enviaron datos"}), 400

    try:
        conductividad = float(data["conductividad"])
        turbidez = float(data["turbidez"])
    except (KeyError, ValueError):
        return jsonify({"error": "Datos inválidos"}), 400

    # El modelo espera un array 2D: [[conductividad, turbidez]]
    prediccion = modelo.predict([[conductividad, turbidez]])[0]

    # Devuelve el resultado
    return jsonify({"resultado": prediccion})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
