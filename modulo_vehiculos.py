# V34 modulos

class vehiculos(): #clase padre
	
	def __init__(self,marca,modelo): #constructor

		self.marca=marca
		self.modelo=modelo
		self.enmarcha=False
		self.acelera=False
		self.frena=False

	def arrancar(self):

		self.enmarcha=True

	def acelerar(self):
		self.acelera=True

	def frenar(self):
		self.frena=True

	def estado(self):
		print("Marca: ",self.marca, "\nModelo: ", self.modelo, "\nEn Marcha ",
			self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: " , self.frena)


class Furgoneta(vehiculos):

	def carga(self,cargar):
		self.cargado=cargar

		if(self.cargado):
			return "la Furgoneta esta cargada"
		else:
			return "la Furgoneta no esta cargada"


#creamos una clase moto que hereda de Vehiculo

class Moto(vehiculos): #asi se hereda en python
	hcaballito=""

	def caballito(self):
		self.hcaballito="Voy haciendo el caballito"

	#sobreecribims el metodo estado, porque el metodo estado que heredamos no contempla el caballito

	def estado(self): #asi lo sobreescribimos, para agregarle una funcionalidad
		print("Marca: ",self.marca, "\nModelo: ", self.modelo, "\nEn Marcha ",
			self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: " , self.frena, "\n", self.hcaballito)


class VElectricos(vehiculos):
	def __init__(self,marca,modelo): #marca y modelo seran usados en el super

		super().__init__(marca, modelo) #asi llamamos a un metodo de la clase padre, en este caso llamaremos al cosntructor
										#lo hacemos para que los objetos tipo VElectricos tengan los atributos de los vehiculos
										#ademas de los que ya tiene en su propio constructor
		self.autonomia=100

	def cargarEnergia(self):
		self.cargando=True



