from Usuarios import Usuario
"""
    Seccionar todo el codigo (Diferentes Clases)
"""

flag = True
list_usuarios = []

try:
    us = Usuario()
except Exception as NoSeEncontro:
    print("Clase no se encontró")


while flag == True:
    print("Plataforma de Usuarios")
    print(" 1.- Agrega Usuarios ")
    print(" 2.- Agrega Usuarios ")
    print(" 3.- Actualizar Usuarios ")
    print(" 4.- Mostrar datos")
    print(" 5.- Salida ")

    opciones_menu = input("Introduce una opcion:  ")

    if int(opciones_menu) == 1:
        print(" Agregar Usuarios ")
        nom = input("Introduce un nombre:  ")
        list_usuarios.append(us.mostrar_nombre(in_nombre=nom))
        print(list_usuarios)
    
    elif int(opciones_menu) == 2:
        print(" Eliminar Usuarios ")
        print(list_usuarios)
        try:
            nombre = input('A quien eliminas')
            list_usuarios.remove(nombre)
            list_usuarios.sort()
            print(list_usuarios)
        except Exception as user_not_found:
            print("Ese usuario no se encontró")
    
    elif int(opciones_menu) == 3:
        print(" Actualizar Usuarios ")
        print(list_usuarios)
        id = input("Que valor deseas actualizar: ")
        id_index = list_usuarios.index(id)

        new_name = input("Cual es el nuevo nombre: ")
        list_usuarios.insert(id_index,new_name)
        list_usuarios.remove(id)
    
    elif int(opciones_menu) == 4:
        print("DATOS")
        print(list_usuarios)
        print(list_usuarios.sort())
    
    else: 
        flag = False
        print("Salida")