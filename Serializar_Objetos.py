#V40 Serializacion objetos y leerlo

import pickle

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


# Empezamos desde aqui, vamos a crear objetos de esta clase y a serializarlos

coche1=vehiculos("Mazda","MX5")

coche2=vehiculos("Seat","Leon")

coche3=vehiculos("Reanault","Megane")

# Los podemos serailizar idividualmente, pero en este video 
# los meteremos en una coleccion y serializamos esa coleccion

coches=[coche1,coche2,coche3]  # coleccion de objetos

#creamos un fichero donde guardaremos los objetos serializados

fichero=open("losCoches","wb") #wb escritura bytes

# hacemos el volcado de la informacion en el fichero

pickle.dump(coches,fichero)

fichero.close()

del(fichero)


# Listo, ahora podemos rescatar la informacion (los objetos) del archivo que hemos creado


ficheroApertura=open("losCoches","rb")

#creamos variables para volcar la informacion de ese fichero

misCoches=pickle.load(ficheroApertura)

ficheroApertura.close()

#recorremos la info de miscoches

for c in misCoches:

	print(c.estado())















































































