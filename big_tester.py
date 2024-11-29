import os
import subprocess
import requests
import time

# Configuración del directorio de mutantes
mutants_dir = "app_mutants"
test_url = "http://127.0.0.1:5000"  # URL del servidor Flask para probar
test_path = "/"  # Ruta que se probará

# Variables para el informe
total_mutants = 0
survived_mutants = 0
killed_mutants = 0
invalid_mutants = 0

def test_mutant(mutant_path):
    """
    Levanta el servidor mutante, realiza el test y determina si el mutante sobrevive.
    """
    try:
        # Inicia el servidor mutante
        process = subprocess.Popen(["python", mutant_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(2)  # Da tiempo al servidor para inicializar

        # Realiza la solicitud HTTP
        try:
            response = requests.get(test_url + test_path, timeout=5)
            if response.status_code == 200:
                print(f"[SOBREVIVIÓ] El mutante {mutant_path} permitió acceso.")
                return "survived"
            else:
                print(f"[MUERTO] El mutante {mutant_path} respondió con código {response.status_code}.")
                return "killed"
        except requests.exceptions.RequestException:
            print(f"[MUERTO] El mutante {mutant_path} no respondió.")
            return "killed"
    except Exception as e:
        print(f"[NO VÁLIDO] El mutante {mutant_path} no se pudo ejecutar: {e}")
        return "invalid"
    finally:
        # Termina el servidor mutante
        process.terminate()
        try:
            process.wait(timeout=2)
        except subprocess.TimeoutExpired:
            process.kill()
        time.sleep(1)  # Da tiempo al sistema para liberar recursos

# Probar cada mutante
if os.path.exists(mutants_dir):
    mutant_files = [os.path.join(mutants_dir, f) for f in os.listdir(mutants_dir) if f.endswith(".py")]
    total_mutants = len(mutant_files)

    for mutant_file in mutant_files:
        result = test_mutant(mutant_file)
        if result == "survived":
            survived_mutants += 1
        elif result == "killed":
            killed_mutants += 1
        elif result == "invalid":
            invalid_mutants += 1
else:
    print(f"No se encontró el directorio de mutantes: {mutants_dir}")

# Calcular porcentaje de cobertura
if total_mutants > 0:
    coverage = (killed_mutants / total_mutants) * 100
else:
    coverage = 0

# Generar informe
print("\n===== INFORME =====")
print(f"Total de mutantes: {total_mutants}")
print(f"Mutantes muertos: {killed_mutants}")
print(f"Mutantes sobrevivientes: {survived_mutants}")
print(f"Mutantes no válidos: {invalid_mutants}")
print(f"Porcentaje de cobertura: {coverage:.2f}%")
