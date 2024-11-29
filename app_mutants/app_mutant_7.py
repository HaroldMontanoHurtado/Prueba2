from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Configuración inicial de CORS
cors_config = {
    "origins": ["http://example.com", "http://localhost:3000"],  # Dominios permitidos
    "methods": ["GET", "POST"],  # Métodos HTTP permitidos
    "allow_headers": ["Content-Type", "Authorization"],  # Headers permitidos
    "supports_credentials": True,  # Permitir cookies o autenticación entre dominios
}

# Aplicar configuración de CORS
CORS(app, resources={r"/*": cors_config})

@app.route("/")
def home():
    return jsonify({"message": "CORS configurado correctamente"}), 200

if __name__ == "__main__":
    print("Configuración de CORS sin cambio: ", cors_config)
    # Ejemplo de modificación dinámica antes de iniciar la app
    cors_config["origins"].append("*")
    print("Configuración de CORS actualizada: ", cors_config)
    app.run(debug=True)


# Mutacion de configuracion
from flask_cors import CORS
CORS(app,
     origins=['http://example.com', 'http://another-example.com'],
     methods=['GET', 'POST', 'PUT', 'DELETE'],
     allow_headers="Content-Type,Authorization",
     supports_credentials=False,
     max_age=3600,
     send_wildcard=False,
     automatic_options=True,
     vary_header=True
)