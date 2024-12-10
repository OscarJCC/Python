
try:
     archivo = open("archivo.txt","r")
     #No se puede repetir ya que el puntero se mueve al final
     print(archivo.read())
     archivo.seek(0)
     #Ocurre lo mismo que en el anterior solo se puded repetir una vez
     #Mete en una lista cada linea del texto
     lista_a = archivo.readlines()
     print(lista_a[0])
     print(lista_a[1])
     
     archivo.seek(0)
     
     print(archivo.read())
     #Mueve el puntero al numero de caracter que quieras
     archivo.seek(4)
     print(archivo.read())
     
finally:     
     archivo.close()