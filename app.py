from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

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

    # Ejemplo de "predicción" sencilla:
    # (aquí normalmente pondrías tu modelo real)
    if conductividad > 5.0:
        prediccion = np.int64(1)
    else:
        prediccion = np.int64(0)

    # Convertir a int puro para que sea serializable
    prediccion = int(prediccion)

    # Devolver la respuesta en JSON
    return jsonify({"resultado": prediccion})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
