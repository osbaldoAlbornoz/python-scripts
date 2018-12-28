# V33 metodos aplicados a Strings
#************** I M P O R T A N T E *************

# nombreusuario=raw_input("Introduce nombre: ")

# print("El nombre es: ", nombreusuario.upper())

# print("El nombre es: ", nombreusuario.lower())

# print("El nombre es: ", nombreusuario.capitalize()) #primera letra en mayusculas

# edad=raw_input("Introduce edad")

# print(edad.isdigit()) #true si es numero




edad=raw_input("Introduce edad  ")

while (edad.isdigit()==False): # si es numerico
	
	print("porfavp introduce un valor numerico")

	edad=raw_input("Introduce edad  ")

	if(int(edad)<18):

		print("No puede pasar")
	else:
		print("Si puede pasar")
