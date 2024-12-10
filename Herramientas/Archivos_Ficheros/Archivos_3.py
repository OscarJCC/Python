
Datos = list(range(1,20))

try:

     archivo = open("Datos.txt","w")
     
     for i in Datos:
          archivo.write(f"{i}\n")

     print(Datos)
     
finally:
     archivo.close()
     
try:
     archivo = open("Datos.txt","r")
     
     lista = (archivo.readlines())

     datos = []
     
     for i in lista:
          datos.append(float(i))
     
     
finally:
     archivo.close()

print(datos)