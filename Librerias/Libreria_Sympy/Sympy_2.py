import sympy as sy
from sympy.integrals.integrals import integrate
import numpy as np

print("CALCULO")
#CALCULO

x = sy.symbols("x")

f = sy.exp(x**2)
print("f = ",f)
#Se usa para calcular la derivada de una funcion
#diff(funcion a derivar,variable a la que se deriva de la funcion)
print("Derivada de f =",sy.diff(f,x))
print("\n")

g = sy.exp(-x)
print("g =",g)
#Se usa par calcular la integral de una funcion
#sy.integrate(funcion a integrar,variable respecto a la que se integra)
print("Integral de g =",sy.integrate(g,x))
print("\n")

#Se usa par calcular una integral definidad
#sy.integrate(Funciona integrar, (variable respecto a la que se integra, limite inferior, limite superior))
#sy.oo = infinito
print("Integral definida de 0 a infinito de g =",sy.integrate(g,(x, 0, sy.oo)))
print("\n")

#Se usa para guardar una integral en una varianle
#sy.Integral(funcion a integrar, variable respecto a la que se integra)
sum = sy.Integral(sy.exp(-x**2),x)
print(sum)
#Para solucionar esta integral se usa
print("Solucion de la integral sum =",sum.doit())
print("Solucion de la integral sum definidad desde menos infinito hasta infinto =",sy.integrate(sy.exp(-x**2), (x, -sy.oo, sy.oo)))
print("\n")

h = 1/x
#Se usa para calcular el limite de una funcion
#sy.limit(funcion a la que se le calculara el limite, varaible respecto a la que se calculara, dsde donde se desea que se hacerque)
sy.limit(h, x, 0)

print("SOLUCION DE ECUACIONES")
#SOLUCION DE ECUACIONES

#              x^2 + 1 = 0
#Primero se define la expresion
Expr = x**2 + 1
#Despues generamos la ecuacion con
#sy.Eq(Expresion, parte a igualar)
Ec = sy.Eq(Expr,0)
print(Ec)
#Despues resolvemos la ecuacion generada caon
#sy.solveset(Ecuacion generada, variable a despejar)
print("Solucion =",sy.solveset(Ec,x))
print("\n")

print("MATRICES")
#MATRICES

#Para tomar matrices de forma simbolica con sympy
#Primero se define una matriz como una lista
A = np.linspace(-10,10,1001)
#Se usa para tratar una matriz de forma simbolica 
#sy.Matrix(Matriz como lista)
matriz = sy.Matrix(A)
print("A =",matriz)

B = np.linspace(-10,10,1001)
matriz1 = sy.Matrix(B)
print("B =",matriz1)

#Ya se puedentratar como matrices

#Suma
print("A + B =",matriz + matriz1)

print(matriz1)

#Multiplicacion
print("A * B =",matriz * matriz1)

#Calcular su determinante
print("Determinante de A =",matriz.det())

#Obtener su transpuesta
print("La transpuesta de A =",matriz.T)
