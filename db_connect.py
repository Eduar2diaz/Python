import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password= '1234',
    database= 'mysql'

    )

cursor = conn.cursor()

cursor.execute("select * from db ")

resultados = cursor.fetchall()

for dato in resultados:
    print(dato)
else:
    print("No tiene datos")

conn.close