
def main():
    while True:
        print("Bienvenido")
        print("")
        print("1.Registrar ciudad")
        print("2.Ver ciudades")
        print("3.Buscar ciudad")
        print("4.Eliminar ciudad")
        print("5.Salir")
        opc=int(input("Elija una opcion: "))
        
        if opc == 1:
            nombre = input("Nombre: ")
            codigo = input("Codigo postal: ")
            poblacion = input("Poblacion: ")
            pais = input("Pais: ")
            registrar_ciudad(nombre, codigo, poblacion, pais)
        elif opc == 2:
            roles = listar_ciudad()
            for ciudad in ciudades:
                print(ciudad)
        elif opc == 3:
            print("buscar ciudad (proceso)")
        elif opc == 4:
            nombre = input("Ciudad a eliminar: ")
            eliminar_ciudad(nombre)
        elif opc == 5:
            print("")
            print("Hasta pronto")
            break
        else:
                print("Opción no válida")

if __name__ == "__main__":
    main()

    







