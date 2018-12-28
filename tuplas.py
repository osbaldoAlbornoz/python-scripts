# V8 Tuplas

#se cren con ()  se leen con []

miTupla=("Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo")

print(miTupla[2])

print(miTupla[:])

#Convertir una tupla en una lista

miLista=list(miTupla)


#Convertir una list en una tupla

miTupla2=tuple(miLista)


print("Lunes" in miTupla2) # true si existe Lunes

print(miTupla2.count("Lunes")) #cuantas veces esta el elemento

print(len(miTupla2)) #uantos elementos hay

miTupla3=("Enero",) #tupla unitaria (un unico elemento)

miTupla4="Hola","Adios" #tupla sin parentesis otra sintaxys (empaquetado de tupla)

# ******** desempaquetado de tuplas ********
dialunes, diamartes, diaMiercoles, diaJueves, diaViernes, diaSabado, diaDomingo =miTupla2

# python asigna a esas variables en ese orden los valores de la tupla a las variables

print(dialunes)






