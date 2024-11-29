import ast
import os
import shutil

"""
Mi forma de modificar las configuraciones es llevar a todas a una forma base 'correcta'
para luego pasar a mutarlos, lo cual no deberia ser, y en vez de eso solo ir una a una
remplanzado o agregando los valores que se desean modificar, esto con el fin de que la
APP que tenga el usuario pueda probrar sus configuraciones propias.
"""

# Configuración segura
secure_config = {
    "origins": "['http://example.com', 'http://another-example.com']",
    "methods": "['GET', 'POST', 'PUT', 'DELETE']",
    "allow_headers": '"Content-Type,Authorization"',
    "supports_credentials": "False",
    "max_age": "3600",
    "send_wildcard": "False",
    "automatic_options": "False",
    "vary_header": "True",
}

# Configuración vulnerable
vulnerable_config = {
    "origins": "'*'",
    "methods": "'*'",
    "allow_headers": "'*'",
    "supports_credentials": "True",
    "max_age": "3600",
    "send_wildcard": "True",
    "automatic_options": "True",
    "vary_header": "False",
}

# Ruta de salida para mutaciones
mutants_dir = "app_mutants"

if not os.path.exists(mutants_dir):
    os.makedirs(mutants_dir)

# Generar configuraciones mutadas
def generate_mutations():
    mutations = []

    # Mutaciones individuales
    for key in secure_config.keys():
        mutation = secure_config.copy()
        mutation[key] = vulnerable_config[key]
        mutations.append(mutation)

    # Combinaciones de múltiples mutaciones
    keys = list(secure_config.keys())
    for i in range(2, len(keys) + 1):  # Desde 2 hasta todas las combinaciones
        from itertools import combinations
        for combo in combinations(keys, i):
            mutation = secure_config.copy()
            for key in combo:
                mutation[key] = vulnerable_config[key]
            mutations.append(mutation)

    return mutations

# Crear nuevas versiones de la aplicación

def create_mutant_files(original_file):
    with open(original_file, "r") as file:
        original_code = file.read()

    tree = ast.parse(original_code)

    # Verificar que el archivo contiene "if __name__ == '__main__'"
    if_main_found = any(
        isinstance(node, ast.If) and isinstance(node.test, ast.Compare)
        and isinstance(node.test.left, ast.Name) and node.test.left.id == "__name__"
        for node in tree.body
    )

    if not if_main_found:
        print("El archivo proporcionado no contiene un bloque 'if __name__ == \"__main__\"'.")
        return

    mutations = generate_mutations()

    for idx, mutation in enumerate(mutations):
        if idx < 50:
            mutated_code = original_code + "\n\n" + generate_cors_config_code(mutation)
            mutant_file_path = os.path.join(mutants_dir, f"app_mutant_{idx + 1}.py")
            with open(mutant_file_path, "w") as mutant_file:
                mutant_file.write(mutated_code)
        else:
            break

# Generar código de configuración CORS
def generate_cors_config_code(config):
    cors_config = [
        "# Mutacion de configuracion",
        "from flask_cors import CORS",
        "CORS(app,",
    ]

    for key, value in config.items():
        cors_config.append(f"     {key}={value},")

    cors_config[-1] = cors_config[-1].rstrip(",")  # Eliminar la última coma
    cors_config.append(")")
    return "\n".join(cors_config)

# Uso del script
original_file = "App2.py"  # Cambia esta ruta al archivo .py de tu aplicación Flask
if os.path.exists(original_file):
    create_mutant_files(original_file)
    print(f"Mutaciones creadas en la carpeta '{mutants_dir}'.")
else:
    print(f"El archivo '{original_file}' no existe.")
