import pickle

lista_nombres = ["Pedro","Ana","Maria","Isabel"]

fichero_binario = open("Lista_Nombre","wb") # wb, permite crear el archivo con escritura binaria

pickle.dump(lista_nombres,fichero_binario)   #modulo ,dump permite guardar informacion en un archivo o fichero
                                             #con escritura binaria
                                             

fichero_binario.close()

del fichero_binario

fichero = open("Lista_Nombre","rb") # rb, permite leer el archivo codificado en codigo binario

lista = pickle.load(fichero) #modulo, load permite tomar la informacion del archivo o fichero 
                              # en codigo binario y guerdarla en una variable
                              
print(lista)

fichero.close()