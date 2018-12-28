# V10 condicionales

#IF

print("Programa de evaluacion de notas de Alumnos")

nota=input("Introduce la nota del Alumno:")

def evaluacion(nota):

	valoracion="aprobado"
	if nota<5:
		valoracion="suspenso"
	return valoracion
#

print(evaluacion(nota))