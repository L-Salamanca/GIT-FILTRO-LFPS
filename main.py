

while True:
    print("Bienvenido")
    print("")
    print("1.Registrar ciudad")
    print("2.Ver ciudades")
    print("3.Buscar ciudad")
    print("4.Editar ciudad")
    print("5.Salir")
    opc=int(input("Elija una opcion: "))
    
    if opc == 1:
        nombre = input("Nombre: ")
        codigo = input("Codigo postal: ")
        poblacion = input("Poblacion: ")
        pais = input("Pais: ")
        registrar_ciudad(nombre, codigo, poblacion, pais)
    elif opc == 2:
        print("ver ciudades  (proceso)")
    elif opc == 3:
        print("editar ciudad (proceso)")
    elif opc == 4:
        print("buscar ciudad (proceso)")
    elif opc == 5:
        print("")
        print("Hasta pronto")
        break
    







