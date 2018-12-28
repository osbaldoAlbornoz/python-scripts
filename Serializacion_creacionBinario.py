#V39 Serializacion (codificar un objeto en binario)

import pickle # pickle es la libreria para serializar

lista_nombres=["Pedro","Ana","Maria","Isabel"]

#creamos un archivo externo 

fichero_binario=open("lista_nombres","wb") # wb = escritura binaria

#volcado de la lista al fichero externo (metodo dump)

pickle.dump(lista_nombres, fichero_binario) # arg1: informacion a volcar, ar2: fichero en memoria
# acabamos de crear un archivo binario codificado llamado lista_nombres 

# cerramos

fichero_binario.close()

del(fichero_binario) #borramos el archivo de memoria


# Ahora vamos a rescatar la informacion contenida en el



























































