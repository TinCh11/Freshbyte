@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    if data is None:
        return jsonify({"error": "No se recibieron datos JSON"}), 400

    conductividad = data.get("conductividad")
    turbidez = data.get("turbidez")

    if conductividad is None or turbidez is None:
        return jsonify({"error": "Faltan datos"}), 400

    # Simula la predicción: aquí podrías usar tu modelo
    import numpy as np
    prediccion = np.int64(1) if conductividad > 5.0 else np.int64(0)

    # CONVIERTE A int PURO
    prediccion = int(prediccion)

    return jsonify({"resultado": prediccion})

    # Devuelve el resultado (ej. "agua limpia" o "agua sucia")
    return jsonify({"resultado": prediccion})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
