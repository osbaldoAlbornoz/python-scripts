#V39 Serializacion (codificar un objeto en binario)

#rescatar la informacion del archivo que habiamos creado en la primera parte de este video

import pickle # pickle es la libreria para serializar

#guardamos la informacion que hemos leido en una variable

fichero=open("lista_nombres","rb") # read binary


lista=pickle.load(fichero) # cargamos la informacion

print(lista)



























































