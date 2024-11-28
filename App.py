from flask import Flask, jsonify, request
from flask_cors import CORS
from config import CORSConfig, AppConfig  # Importar configuraciones

# Crear la aplicación Flask
app = Flask(__name__)

# Aplicar configuración general
app.config['API_KEY'] = AppConfig.API_KEY

# Configurar CORS
CORS(
    app,
    resources={
        r"/*": {
            "origins": CORSConfig.ORIGINS,
            "methods": CORSConfig.METHODS,
            "allow_headers": CORSConfig.ALLOW_HEADERS,
            "supports_credentials": CORSConfig.SUPPORTS_CREDENTIALS,
            "max_age": CORSConfig.MAX_AGE,
            "send_wildcard": CORSConfig.SEND_WILDCARD,
            "automatic_options": CORSConfig.AUTOMATIC_OPTIONS,
            "vary_header": CORSConfig.VARY_HEADER,
        }
    }
)

# Rutas básicas
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Bienvenido a la API básica en Flask"}), 200

@app.route("/add", methods=["POST"])
def add():
    data = request.get_json()
    if not data or "num1" not in data or "num2" not in data:
        return jsonify({"error": "Faltan datos en la solicitud"}), 400

    num1 = data["num1"]
    num2 = data["num2"]
    result = num1 + num2
    return jsonify({"num1": num1, "num2": num2, "result": result}), 200

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "OK"}), 200

# Validar API Key en una ruta (ejemplo adicional)
@app.route("/secure-data", methods=["GET"])
def secure_data():
    api_key = request.headers.get("API-Key")
    if api_key != app.config['API_KEY']:
        return jsonify({"error": "API Key inválida"}), 403
    return jsonify({"data": "Acceso autorizado"}), 200

if __name__ == "__main__":
    app.run(debug=True)
