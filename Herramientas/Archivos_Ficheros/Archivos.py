
#Abre un archivo o lo crea
archivo = open("archivo.txt","w")

texto ="Hola a todos\nEste es mi primer archivo locococ"

#Escribe algo en el archivo 
archivo.write(texto)

#Cierra el archivo
archivo.close()

archivo = open("archivo.txt","r")

#Lee el archivo
text = archivo.read()

print(text)

archivo.close()