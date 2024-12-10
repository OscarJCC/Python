
import numpy as np

#Listas normal
x = [1,2,3]
y = [4,5,6]

#Suma de 2 listas normales
print(x+y)
print("\n")

#combierte la lista en un vector
x = np.array(x) 
y = np.array(y) 

#Suma de 2 vectores
print(x+y)
print(type(x))
print("\n")

#Arreglos en forma de lista
A = [[1,2],
     [3,4]]
B = [[5,6],
     [7,8]]

#Suma de 2 arreglos en forma de lista
print(A+B)
print("\n")

#Combierte los arreglos en matrices
A = np.array(A)
B = np.array(B)

#Suma de 2 matrices
print(A+B)
print("\n")

#Lista normal
X = list(range(1,101))
print(X)
print("\n")

#Lista con libreria numpy
Y = np.arange(1,101,1)
print(Y)
print("\n")

dt = 0.2
Q = np.arange(1,11+dt,dt)
print(Q)
print("\n")

#Vector vacio
x = np.array([])
print(x)

x = np.append(x,2)
print(x)
print("\n")

#Vector con ceros
z = np.zeros(10)
print(z)
print("\n")

#Matriz de M filas y N columnas con ceros
#np.zeros((M,N))
Z = np.zeros((100,100))
print(Z)
print("\n")

#Vector y matriz(M,N) con unos
a = np.ones(20)
print(a)
print("\n")

A = np.ones((2,2))
print(A)
print("\n")

#Llenado de vector de ceros con un random
#Que crea numeros aleatorios del 1 al 0
import random as ra

for i in range(len(z)):
     z[i] = ra.random()
     
print(z)
print("\n")

#np.linspace(i, f, N)
#Crea un vector que va de i hasta f tal que N
#es la cantidad de numero en ese arreglo
w = np.linspace(1,10,101)

print(w)

