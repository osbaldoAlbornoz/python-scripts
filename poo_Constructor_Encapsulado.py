# V27 poo metodo constructor

# ********Muy importante este video******

class Coche():

	def __init__(self): #asi es un metodo constructor en python

		self.__largoChasis=250 # __ analogo de private 
		self.__anchoChasis=120
		self.__ruedas=4   # __ analogo de private 
		self.__enmarcha=False
		#colocamos self a aquellas propiedades que formen parte del estado inicial

	def arracar(self,arrancamos): # es obligatorio colocarlo en python como primer parametro obligatorio
					#a diferencia de java que va implicito en el metodo
		self.enmarcha=arrancamos

		if (self.enmarcha):
			return "El coche esta en marcha"
		else:
			return "El coche esta parado"

	def estado(self):
		print("El coche tiene ",self.__ruedas," ruedas")
		print("El coche tiene un ancho de ",self.anchoChasis)
		print("El coche tiene un largo de ",self.largoChasis)

miCoche= Coche() #asi instanciamos una clase


print(miCoche.arracar(True))

miCoche.estado()


miCoche2= Coche()

print(miCoche2.arracar(False))

miCoche2.__ruedas=2

miCoche2.estado()


















