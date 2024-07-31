from data import *
from ciudades import *

def main():
    while True:
        print("Welcome")
        print("")
        print("1.Register city")
        print("2.List cities")
        print("3.Search cities")
        print("4.Remove cities")
        print("5.Exit")
        opc=int(input("choose an option: "))
        
        if opc == 1:
            nombre = input("Name: ")
            codigo = input("Postal code: ")
            poblacion = input("Poblation: ")
            pais = input("Country: ")
            registrar_ciudad(nombre, codigo, poblacion, pais)
        elif opc == 2:
            roles = listar_ciudades()
            for ciudad in ciudades:
                print(ciudad)
        elif opc == 3:
            print("buscar ciudad (proceso)")
        elif opc == 4:
            nombre = input("Name the city you want to remove: ")
            eliminar_ciudades(nombre)
        elif opc == 5:
            print("")
            print("Goodbye!")
            break
        else:
                print("Invalid option")

if __name__ == "__main__":
    main()

    







