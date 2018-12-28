# V9 Diccionarios

miDiccionario={"Alemania":"Berlin","Venezuela":"Caracas","Francia":"Paris","Angentina":"Buenos Aires"} #clave:valor


miDiccionario["Italia"]="Lisboa"  #agregar elemento

miDiccionario["Italia"]="Roma" #cambiar el valor de una elemento

print(miDiccionario["Italia"])


mitupla=["Espanha", "Francia", "Reino Unido", "Alemania"]

miDiccionario2={mitupla[0]:"Madrid", mitupla[1]:"Paris",mitupla[2]:"Londres",mitupla[3]:"Berlin"}
#Asignar a un diccionario valores usando una tupla

print(miDiccionario2["Francia"])

#podemos almacenar una tupla dentro de un diccionario asi:



# ******** TAMBIEN PODEMOS ASIGNAR VARIOS VALORES A UNA SOLA CLAVE *******

miDiccionario3={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","anillos":[1991,1992,1993,1996,1997,1998]}

print(miDiccionario3["anillos"])

# *********TAMBIEN PODEMOS GUARDA UN DICCIONARI DENTRO DE OTRO *******

miDiccionario4={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}

#ver claves de un dicionario
print(miDiccionario4.keys())

#ver valores de un dicionario
print(miDiccionario4.values())

#longitud de un diccionario
print(len(miDiccionario4))

print(miDiccionario4["anillos"])



















