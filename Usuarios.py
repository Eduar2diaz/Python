from RolesUsuarios import TipoUsuario

#Clase Usuarios
class Usuario(TipoUsuario):
    #Funcion que muestra nombre
    def mostrar_nombre(self,in_nombre):
        out_nombre = in_nombre
        return out_nombre
    #Funcion que muestra apellido paterno
    def mostrar_app(self,in_app):
        """Almacena variables de entrada hacia la de salida"""
        out_app = in_app
        return out_app
    #Funcion que muestra edad
    def mostrar_edad(self,in_edad):
        out_edad = in_edad
        return out_edad
    def mostrar_rol(self,in_roll):
        out_roll = in_roll
        return out_roll
