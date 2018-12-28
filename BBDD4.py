#V58 BBDD2 UNIQUE Y OPERACIONES CRUD
 
import sqlite3 #importamos la libreria que integra la BBDD

# 1.- **** CREAMOS LA CONEXION ******

miConexion= sqlite3.connect("GestionProductos") # se crea la conexion, pero como la BBDD no ha sido creada, la crea con ese nombre

# 2.- ****** CREAMOS EL CURSOR ******

miCursor=miConexion.cursor()

#3.- ****** HACEMOS UNA CONSULTA, EN ESTE CASO CREAR UNA TABLA YA QUE NO HAY

#esta linea comentada abre o crea la BBDD CON SU PRIMARY KEY QUE SERA CODIGO_ARTICULO
miCursor.execute("CREATE TABLE PRODUCTOS (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE_ARTICULO VARCHAR(50) UNIQUE, PRECIO INTEGER, SECCION VARCHAR(20))")


#3.1 **** Insertamos registros en la BBDD

#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON', 15, 'DEPORTES')")

# EN ESTE VIDEO INSERTAREMOS LA INFO ASI: CREAMOS UNA LISTA Y EN SU INTERIOR TUPLAS CON LA INFOR

# **************************************
productos=[
	
	("Camiseta",10,"Deportes"),
	("Jarron",90,"Ceramica"),
	("Camion",20,"Jugueteria"),
	("Carrito",30,"Jugueteria")

]

# #usamos elmetodo executemany()  para insertar varios registros a la vez

miCursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?)", productos) #esta es otra forma de insertar registros, tantos ? como columnas de la tabla
												   # Aqui colocamos NULL porque el id es autoincrementable y en estos casos se coloca asi

#*************************************

#Como hacer una consulta y obtener la informacion de la tabla
		
		#********  SELECT   ********

# miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='Deportes'")
# productos=miCursor.fetchall() # asi asociamos lo que devuelve la consulta con los campos respectivos, fetchall devuelve una lista

#ahora recorremos la lista almacenada en variosProductos
#dos formas:
# 1.- simplemente imprimimos la lista
#print("Resultados de la lista con print:\n")
#print(productos)


# 2 Usamos un bucle for:
# print("\n")
# print("Resultados de la lista con bucle for:\n")
# for producto in productos:
# 	print(producto)

#  ***************   UPDATE     ************

# miCursor.execute("UPDATE PRODUCTOS SET PRECIO =99 WHERE ID=4")

#  ***************   DELETE     ************

#miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=4")



miConexion.commit()# Esta instruccion es para verificar que si queremos hacer ese cambio

#**** CERRAMOS LA CONEXION *****
miConexion.close()









































