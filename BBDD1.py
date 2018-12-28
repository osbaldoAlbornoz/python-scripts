#V55 BBDD1 CON SQLite (esta base de datos viene integrada al programa)
 
import sqlite3 #importamos la libreria que integra la BBDD

# 1.- **** CREAMOS LA CONEXION ******

miConexion= sqlite3.connect("PrimeraBase") # se crea la conexion, pero como la BBDD no ha sido creada, la crea con ese nombre

# 2.- ****** CREAMOS EL CURSOR ******

miCursor=miConexion.cursor()

#3.- ****** HACEMOS UNA CONSULTA, EN ESTE CASO CREAR UNA TABLA YA QUE NO HAY

#esta linea comentada abre o crea la BBDD
#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")


#3.1 **** Insertamos registros en la BBDD

miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON', 15, 'DEPORTES')")

miConexion.commit()# Esta instruccion es para verificar que si queremos hacer ese cambio

#**** CERRAMOS LA CONEXION *****
miConexion.close()









































