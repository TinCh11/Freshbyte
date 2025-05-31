from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import pickle

app = Flask(__name__)

# Habilitar CORS globalmente
CORS(app, resources={r"/*": {"origins": "*"}})

# Cargar el modelo entrenado
with open("modelo_agua.pkl", "rb") as f:
    modelo = pickle.load(f)

@app.route("/")
def home():
    return "¡El servidor está corriendo!"

@app.route("/predict", methods=["POST", "OPTIONS"])
@cross_origin(origins="*")
def predict():
    # Permitir la respuesta para la petición preflight
    if request.method == "OPTIONS":
        return jsonify({"message": "Preflight OK"}), 200

    # Obtener los datos del POST como JSON
    data = request.get_json()
    if data is None:
        return jsonify({"error": "No se recibieron datos JSON"}), 400

    # Obtener los valores de conductividad y turbidez
    conductividad = data.get("conductividad")
    turbidez = data.get("turbidez")

    if conductividad is None or turbidez is None:
        return jsonify({"error": "Faltan datos: 'conductividad' y/o 'turbidez'"}), 400

    # Hacer la predicción con el modelo
    prediccion = modelo.predict([[conductividad, turbidez]])[0]
    prediccion = int(prediccion)

    return jsonify({"resultado": prediccion})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
