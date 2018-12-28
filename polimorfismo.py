# V32 polimorfismo
#************** I M P O R T A N T E *************

class Coche():

	def desplazamiento(self):
		print("me desplazo usando 4 ruedas")


class Moto():

	def desplazamiento(self):
		print("me desplazo usando 2 ruedas")

class Camion():

	def desplazamiento(self):
		print("Me desplazo con 6 ruedas")

#tradicional
#****************
# miVehiculo=Moto()

# miVehiculo.desplazamiento()

# miVehiculo2=Coche()

# miVehiculo2.desplazamiento()


# miVehiculo3=Camion()

# miVehiculo3.desplazamiento()



#con polimorfismo
#**********************

def desplazamientoVehiculo(vehiculo): #aqui esta el polimorfismo
	vehiculo.desplazamiento()

miVehiculo=Camion()

desplazamientoVehiculo(miVehiculo)

# aqui el metodo desplazamientoVehiculo() llamara al metodo desplazamiento()
# de Camion porque el objeto miVehiculo es tipo camion













































