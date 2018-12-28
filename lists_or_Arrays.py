# V7 Listas o Arrays

miLista=["Lunes","Martes","Miercoles","Jueves"]

print(miLista[0]) #Imprimir un solo elemento

print(miLista[:]) #Imprimir toda la lista

print(miLista[-2]) #Imprime el valor dos del final al principio

print(miLista[0:3]) #porcion de la lista (accede a los 3 primeros elementos)

print(miLista[0:-2]) #porcion de la lita (accede a los 2 utimos elementos)

print(miLista[:2]) #porcion abreviada (accede a los 2 primeros elementos)

print(miLista[2:]) #del indice 2 hasta el final)

#--------------------

miLista.append("Sabado") #agrega elemento al final

miLista.insert(4,"Viernes") #agrega elemento en un indice especifico

print(miLista[:])

miLista.extend(["Domingo","Lunes2","Martes2"]) #agrega varios elementos

print(miLista[:])

print(miLista.index("Martes")) # saber cual es el indice de un elemento

print("Miercoles" in miLista) #saber si un elemnto se encuentra en una lista

miLista.remove("Martes2") # eliminar elemento, tambien se puede pone el indice

print(miLista[:])

#   miLista.pop elimina el ultimo elemento

miLista2=["Enero","Ferebro"]

miLista3=miLista+miLista2 # Se pueden sumar, se agrega una lista a la otra

print(miLista3[:])

miLista4=["Maria","Juan"]*3 #la repite 3 veces

print(miLista4[:])





