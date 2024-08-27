from Usuarios import Usuario
"""
    Seccionar todo el codigo (Diferentes Clases)
"""

flag = True
list_usuarios = []
us = Usuario()
us.mostrar_rol

while flag == True:
    print("Plataforma de Usuarios")
    print(" 1.- Agrega Usuarios ")
    print(" 2.- Agrega Usuarios ")
    print(" 3.- Actualizar Usuarios ")
    print(" 4.- Salida ")

    opciones_menu = input("Introduce una opcion:  ")

    if int(opciones_menu) == 1:
        print(" Agregar Usuarios ")
        nom = input("Introduce un nombre:  ")
        list_usuarios.append(us.mostrar_nombre(in_nombre=nom))
        print(list_usuarios)
    elif int(opciones_menu) == 2:
        print(" Eliminar Usuarios ")
    elif int(opciones_menu) == 3:
        print(" Actualizar Usuarios ")
    else: 
        flag = False
        print("Salida")