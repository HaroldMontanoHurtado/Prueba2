import os
import importlib
import unittest


def discover_mutants(mutants_folder):
    """
    Descubre todos los archivos de mutantes en la carpeta especificada.
    """
    mutants = []
    for root, _, files in os.walk(mutants_folder):
        for file in files:
            if file.endswith(".py") and not file.startswith("__"):
                mutant_path = os.path.join(root, file)
                module_path = mutant_path.replace(os.sep, ".").rstrip(".py")
                mutants.append(module_path)
    return mutants


def run_tests_on_module(module_path):
    """
    Ejecuta las pruebas unitarias en un módulo importado dinámicamente.
    """
    try:
        # Importar el módulo dinámicamente
        imported_module = importlib.import_module(module_path)

        # Sustituir CORSConfig y AppConfig en el espacio de nombres global
        globals()["CORSConfig"] = imported_module.CORSConfig
        globals()["AppConfig"] = imported_module.AppConfig

        # Correr las pruebas unitarias
        test_loader = unittest.TestLoader()
        test_suite = test_loader.loadTestsFromTestCase(TestCORSConfig)
        test_result = unittest.TextTestRunner(stream=open(os.devnull, "w")).run(test_suite)

        # Determinar si pasó o falló
        return test_result.wasSuccessful()

    except Exception as e:
        # Manejar errores si el módulo no es válido
        print(f"Error ejecutando pruebas en {module_path}: {e}")
        return False


if __name__ == "__main__":
    mutants_folder = "mutants"
    mutants = discover_mutants(mutants_folder)

    total_mutants = len(mutants)
    failed_tests = 0

    print(f"Total de mutantes encontrados: {total_mutants}\n")

    for mutant in mutants:
        result = run_tests_on_module(mutant)
        if not result:
            failed_tests += 1
        status = "✅" if not result else "❌"
        print(f"{mutant}: {status}")

    passed_tests = total_mutants - failed_tests
    coverage_percentage = (failed_tests / total_mutants) * 100 if total_mutants > 0 else 0

    print("\nResumen:")
    print(f"- Total de mutantes: {total_mutants}")
    print(f"- Mutantes que pasaron las pruebas: {passed_tests}")
    print(f"- Mutantes que fallaron las pruebas: {failed_tests}")
    print(f"- Cobertura de pruebas: {coverage_percentage:.2f}%")
