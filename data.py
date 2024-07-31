import json

def data_loader (ruta):
    try:
        with open(ruta, 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

def data_Saver (ruta, datos):
    with open(ruta, 'w') as archivo:
        json.dump(datos, archivo, indent=4)
