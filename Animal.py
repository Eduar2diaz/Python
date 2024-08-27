
class Animales:
    """def __init__(self,nombre,edad,color):
        self.nombre = nombre
        self.edad = edad
        self.color = color"""

    def gatos(self,nombre,edad,color):
        print(f"El nombre es : {nombre}")
        print(f"Su edad es : {edad}")
        print(f"Su color es : {color}")

    def perros(nombre,edad,color):
        print(f"El nombre es : {nombre}")
        print(f"Su edad es: {edad}")
        print(f"Su color es : {color}")

Dolly = Animales.perros(
    nombre="Dolly",
    edad="5 años",
    color="Pimienta"
)

Michi = Animales()

Michi.gatos(edad="20 años",nombre="Michi",color="Invicible")
