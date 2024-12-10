# Generador que nos permite conocer las ciudades que recibe
def Dev_Ciudades(*ciudades):
     for element in ciudades:
          yield element
          
Ciudades_Dev = Dev_Ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(Ciudades_Dev))
print(next(Ciudades_Dev))

print("\n")

#Generador que nos permite conocer las letras que tiene el nombre de las
#ciudades que recibe
def Dev_Ciudades(*ciudades):
     
     #for element in ciudades:
     #     for Subelement in element:
     #          yield Subelement
     
     # Para poder acortar esto podemos usar lo que es el -- yield from--
     # y nos permite reducir un for
     
     for element in ciudades:
          yield from element
          
Ciudades_Dev = Dev_Ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(Ciudades_Dev))
print(next(Ciudades_Dev))
