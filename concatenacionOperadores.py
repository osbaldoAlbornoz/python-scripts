# V12 condicionales

#Ejemplo1

# edad=100

# if 0<edad<100: #contatenacion de operadores
# 	print("Edad correcta")
# else:
# 	print("edad incorrecta")

	
#Ejemplo2

salario_presidente= input("Introduce salario de el presidente ")
print("Salario presidente: ") + str(salario_presidente)

salario_director= input("Introduce salario de el director ")
print("Salario director: ") + str(salario_director)

salario_jefe_area= input("Introduce salario de el Jefe de ares ")
print("Salario jefe area: ") + str(salario_jefe_area)

salario_administrativo= input("Introduce salario de el administrativo ")
print("Salario administrativo: ") + str(salario_administrativo)

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
	print("Todo funciona bien")
else:
	print("Algo no anda bien")





























