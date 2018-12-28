# V34 modulos

#si usamos import
import funcionesMatematicas

funcionesMatematicas.sumar(2,4) # se debe colocar el NombreDelArchivoAusar.metodo()


#**********************************


#si usamos from
#from funcionesMatematicas import sumar

from funcionesMatematicas import * # importamos todas las funciones si las necesitaremos

sumar(2,4) # No se debe colocar el NombreDelArchivoAusar.metodo()