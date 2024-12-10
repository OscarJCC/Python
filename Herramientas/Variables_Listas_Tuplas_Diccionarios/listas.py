
#Asi se define una lista
#        0     1       2      3
lista = [2, "Python", True, [1,1]]

#Acceder a la lista completa
print(*lista)

#Acceder a solo un elemento de la lista
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

#Acceder a varios elementos de la lista
print(lista[:1])
print(lista[:2])
print(lista[:3])           

#Cambiar elemento de una lista
print(lista[1])
lista[2] = 100
print(lista[2])

x = [1,2,3] #vector

# matriz
#    1    2
#    3    4

#Listas dentro de una lista
# matriz = [[1,2],[3,4]]
matriz = [[1,2],
          [3,4]]

print(matriz)

#Crear una lista vacia
lista_vacia = []

# metodo append
#Agrega un dato a una lista vasio
lista_vacia.append(23)
lista_vacia.append("FCFM")

print(lista_vacia)

# metodo extend
#Agrega varios datos a una lista vacia
lista_vacia.extend([False, 56, "hola"])

print(lista_vacia)

#Las lista tambien se pueden sumar
print(lista_vacia + lista)

#              funcion sum
# Suma todos los datos que tiene una lista
#              funcion len
# Cuenta cuantos datos tiene una lista

datos = [1,2,3,4,5]

print("Datos : ",datos)
print("La suma de la datos es :",sum(datos))

def promedio(datos):
     
     return sum(datos)/len(datos)

print("El promedio es :",promedio(datos))

lista_2 = [2,True,"Hola"] #No se puede sumar str con int
                          #Las bolianas lastoma como Falso = 0 y True = 1

print(lista_2)

#List es el tipo de dato que tiene una lista
print(type(lista))

print(len(lista))