# V74 Funcion Decoradora 2 (con parametros)

# Haremos una funcion decoradora para agregar funcionalidad a las funciones suma y resta

def funcion_decoradora(funcion_parametro):

	def funcion_interior(*args, **kwargs): #con *args se indica que se pueden recibir un numero indeterminado de parametros
											# con *kwargs se pueden agregar argumentos de tipo clave-valor
		# Acciones adicionales que decoran

		print("vamos a realizar un calculo")

		funcion_parametro(*args, **kwargs) #con *args se indica que se pueden recibir un numero indeterminado de parametros

		#acciones adicionales que decoran
		print("Hemos terminado el calcuo")

	return funcion_interior


@funcion_decoradora #aqui estamos especificano que la funcion suma tendra funciones adicionales
def suma(num1, num2):

	print(num1+num2)

@funcion_decoradora #aqui estamos especificano que la funcion resta tendra funciones adicionales
def resta(num1, num2):

	print(num1-num2)

@funcion_decoradora
def potencia(base, exponente):
	print(pow(base,exponente))


suma(7,5)

resta(12,10)

potencia(base=5, exponente=3)
















