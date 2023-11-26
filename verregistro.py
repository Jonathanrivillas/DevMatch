import json

# Ruta completa del archivo JSON
archivo = "registro.json"

# Intenta leer el archivo JSON
try:
    with open(archivo, "r", encoding="utf-8") as f:
        contenido = json.load(f)
    print("Contenido actual del archivo JSON:")
    print(json.dumps(contenido, indent=2))  # Imprime el contenido con formato JSON
except FileNotFoundError:
    print(f"El archivo {archivo} no se encuentra.")
except json.JSONDecodeError as e:
    print(f"Error al decodificar JSON: {str(e)}")
except Exception as e:
    print(f"Error general: {str(e)}")