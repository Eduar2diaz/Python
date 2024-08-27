#Un ejemplo de Error
#print(1/0)
numero_var = "Hola"

try:
    print(int(numero_var))
except Exception as error :
    print(error)

print("Hola")
