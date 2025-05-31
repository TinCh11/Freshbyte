from flask import Flask, request, jsonify
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 👉 Esto habilita CORS para todas las rutas

# Carga del modelo entrenado (ajusta el nombre si es diferente)
with open("modelo_agua.pkl", "rb") as f:
    modelo = pickle.load(f)

@app.route("/")
def home():
    return "¡El servidor está corriendo!"

@app.route("/predict", methods=["POST"])
def predict():
    # Obtener los datos del POST como JSON
    data = request.get_json()
    if data is None:
        return jsonify({"error": "No se recibieron datos JSON"}), 400

    # Obtener los valores de conductividad y turbidez
    conductividad = data.get("conductividad")
    turbidez = data.get("turbidez")

    # Validar que existan los datos
    if conductividad is None or turbidez is None:
        return jsonify({"error": "Faltan datos: 'conductividad' y/o 'turbidez'"}), 400

    # El modelo espera un array 2D: [[conductividad, turbidez]]
    prediccion = modelo.predict([[conductividad, turbidez]])[0]

    # Convertir a int puro para que sea serializable
    prediccion = int(prediccion)

    # Devolver la respuesta en JSON
    return jsonify({"resultado": prediccion})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
