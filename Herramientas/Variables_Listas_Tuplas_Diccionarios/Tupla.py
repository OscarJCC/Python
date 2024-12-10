#Las tuplas son como una lista 
#en la que no se puede modificar ningun dato

#Asi se define una tupla
Tuplas = (1, "Hola",True)

# Acceder a la tupla completa
print(Tuplas)

#Acceder a solo un elemento de la tupla
print(Tuplas[0])
print(Tuplas[1])
print(Tuplas[2])

#Pide al usuario que se le asigne un valor a la variable
#El int da el tipo de dato que es la variable
#El input pide el valor de la variable
a = int(input("a = "))

b = 2

#Empaquetar en una tupla
Tpl = a,"+",b

print(Tpl)

print(type(Tpl))

#Transformar una tupla a una lista
print(list(Tuplas))

#Transformar una lista en una tupla
lista = [True,False,3,"FCFM"]
print(tuple(lista))

#Desempaquetar una tupla
x,y,z = Tpl
print(x,y,z)

print(Tuplas+Tpl)

# := se usa para asignar otro nombre a una lista
#que transformamos en tupla o alreves
print(nueva := list(Tuplas))

print(nueva)
