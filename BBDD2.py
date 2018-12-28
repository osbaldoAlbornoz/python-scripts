#V56 BBDD2 INSERTAR REGISTROS CON SQLite (esta base de datos viene integrada al programa)
 
import sqlite3 #importamos la libreria que integra la BBDD

# 1.- **** CREAMOS LA CONEXION ******

miConexion= sqlite3.connect("PrimeraBase") # se crea la conexion, pero como la BBDD no ha sido creada, la crea con ese nombre

# 2.- ****** CREAMOS EL CURSOR ******

miCursor=miConexion.cursor()

#3.- ****** HACEMOS UNA CONSULTA, EN ESTE CASO CREAR UNA TABLA YA QUE NO HAY

#esta linea comentada abre o crea la BBDD
#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")


#3.1 **** Insertamos registros en la BBDD

#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON', 15, 'DEPORTES')")

# EN ESTE VIDEO INSERTAREMOS LA INFO ASI: CREAMOS UNA LISTA Y EN SU INTERIOR TUPLAS CON LA INFOR

# **************************************
# variosProductos=[
	
# 	("Camiseta",10,"Deportes"),
# 	("Jarron",90,"Ceramica"),
# 	("Camion",20,"Jugueteria"),
# 	("Carrito",30,"Jugueteria")

# ]

# #usamos elmetodo executemany()  para insertar varios registros a la vez

# miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)", variosProductos) #esta es otra forma de insertar registros


#*************************************

#Como hacer una consulta y obtener la informacion de la tabla

miCursor.execute("SELECT * FROM PRODUCTOS")
variosProductos=miCursor.fetchall() # asi asociamos lo que devuelve la consulta con los campos respectivos, fetchall devuelve una lista

#ahora recorremos la lista almacenada en variosProductos
#dos formas:
# 1.- simplemente imprimimos la lista
print("Resultados de la lista con print:\n")
print(variosProductos)


# 2 Usamos un bucle for:
print("\n")
print("Resultados de la lista con bucle for:\n")
for producto in variosProductos:
	print(producto)


# 2 Usamos un bucle for mas espeficifo:
print("\n")
print("Resultados de la lista con bucle for Solo Nombre y Seccion\n")
for producto in variosProductos:
	print("Nombre Articulo: ",producto[0]," Seccion: ",producto[2])

miConexion.commit()# Esta instruccion es para verificar que si queremos hacer ese cambio

#**** CERRAMOS LA CONEXION *****
miConexion.close()









































