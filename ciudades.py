from data import *

ciudades = data_loader('roles.json')

def registrar_ciudad(nombre, codigo, poblacion, pais):
    ciudad = {
        "nombre": nombre,
        "codigo": codigo,
        "poblacion": poblacion,
        "pais": pais,
    }
    ciudades.append(ciudad)
    data_Saver('ciudades.json', ciudades)

def listar_ciudades():
    return ciudades

def eliminar_ciudades(nombre_ciudad):
    ciudad = next((r for r in ciudades if r["nombre"] == nombre_ciudad), None)
    if ciudad:
        ciudades.remove(ciudad)
        data_Saver('ciudades.json', ciudades)
    else:
        raise Exception("ciudad no encontrada")
