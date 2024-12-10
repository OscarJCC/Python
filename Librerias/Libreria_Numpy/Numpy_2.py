
import numpy as np

x = np.arange(1,11)
y = np.arange(11,21)
print(x)
print(y)
print("\n")
print(x+y)
print("\n")
print(3*x)
print("\n")
print(x+10)
print("\n")
print(x**2)
print("\n")

import math as ma

print(round(ma.sin(ma.pi),2))
print("\n")

p = np.pi
x = np.arange(-2*p, 2*p + p,p)
print(x)
print("\n")
print(np.sin(x))
print("\n")
print(np.cos(x))
print("\n")

#Dimencion del arreglo
print("Dimencion del arreglo x :",x.ndim)
print("Tamaño del arreglo x    :",x.size)
print("(M, N)                  :",x.shape)
print("\n")

#Producto punto de 2 vectore
x = np.array([1,2,3])
y = np.array([3,4,5])

print(x.dot(y)) # = print(y.dot(x))
print("\n")

#Producto cruz
w = np.array([1,2,3])
z = np.array([4,5,6])

print(np.cross(w,z))
print(np.cross(z,w))
print("\n")

#Solucion de un sistema de ecuaciones
"""
           x + 2y = 5
          3x + 4y = 6
"""
A = np.array([[1,2],[3,4]])
B = np.array([5,6])
print(np.linalg.solve(A,B))
print("\n")

#Media de los datos de un arreglo

print(np.mean(x))