# V26 poo clases

# ********Muy importante este video******

class Coche():
	largoChasis=250
	anchoChasis=120
	ruedas=4
	enmarcha=False

	def arracar(self): # es obligatorio colocarlo en python como primer parametro obligatorio
					#a diferencia de java que va implicito en el metodo
		self.enmarcha = True

	def estado(self):
		if (self.enmarcha):
			return "El coche esta en marcha"
		else:
			return "El coche esta parado"

miCoche= Coche() #asi instanciamos una clase

print("El largo del chasis es: ",miCoche.largoChasis)

print("El coche tiene: ",miCoche.ruedas," ruedas")

miCoche.arracar()

print(miCoche.estado())

