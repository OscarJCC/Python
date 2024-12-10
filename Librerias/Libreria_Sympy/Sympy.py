import sympy as sy

#Raiz de 8
print((8)**(1/2))
print(sy.sqrt(8))
print("\n")

#Declaracion de simbolos
#Hace que sympy tome como simbolos las variables que nosotros queremos
x = sy.symbols("x")
#Acomodar en orden
y, z = sy.symbols("y z")

print(x+3*y)

print(type(x))
print("\n")

#Permite que se cambiar de simbolo a numero
print(z)
z = 3
print(z)
print("\n")

#Los toma como simbolos por lo que las operaciones se toman en tre symbolos
Exp = x**2 + y
print(Exp - x**2)
print("\n")

#Funcion factor()
#Factoriza funciones
Exp1 = x**2 + 2*x*y + y**2
print(sy.factor(Exp1))
print("\n")

Exp2 = x**2 + 2*x
print(Exp2)
#Nos permite sustituir el simbolo x por un valor
#subs(simbolo,valor)
print(Exp2.subs(x,1))
print("\n")

a, b = sy.symbols("a b")
Exp3 = (a**2)*b + 2*b - b #b(a**2 + 1)
print(Exp3)
#Nos permite simplificar las funciones
print(sy.simplify(Exp3))
print("\n")

# cos^2(x) + sin^2(x) = 1
#Solo se pueden usar operaciones de el modulo de sympy
h = sy.cos(x)**2 + sy.sin(x)**2
g = 1
#Nos permite preguntar si 2 expresiones o funciones son iguales
print(h.equals(g))
#ya que no permite usar los operadores normale como ==
print(h==g)
print("\n")

#Para que python haga un tratamiento simbolico se utilisa
#Esto permite que no exista el error del punto float
Number = sy.Integer(1)
print(Number)
print(Number+h)
print("\n")

z = sy.symbols("z")
Ec = x**2 + 2*x*y + z
#x = 2, y = 0, z = 1 Ec = 5
#Para darles valores a distintos simbolos de una funcion
print(Ec.subs([(x,2), (y,0), (z,1)]))
print("\n")

"""
IMPRESION EN PANTALLA
 - str
 - ASCII
 - Unicode
 - Latex
 - MathML
"""
w = x**2 + y**2 + 2
#str
print("str:",(w))

#
sy.init_printing()

#Unicode
print("Unicode")
sy.pprint(w,use_unicode = True)

#ASCII
print("ASCII")
sy.pprint(w,use_unicode = False)
print("\n")

In = sy.Integral(sy.exp(-x**2),x)
#str
print("str:",(In))

#
sy.init_printing(In)

#Unicode
print("Unicode")
sy.pprint(In,use_unicode = True)

#ASCII
print("ASCII")
sy.pprint(In,use_unicode = False)

#Obtenemos la operacion en forma de latex
print(sy.latex(In))
