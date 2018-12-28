# V13 operador in

#In

print("Asiganturas de anho 2017")
print("Asignaturas optativas: Informatica Grafica - Pruebas de Software - accesibilidad")

opcion=raw_input("Escribe la asignatura escogida ")

materia=opcion.lower() #pasa el texto a minusculas

if materia in ("informatica grafica","pruebas de software","accesibilidad"):

	print("Asignatura elegida " + materia)
else:
	print("Asigantura no es valida")