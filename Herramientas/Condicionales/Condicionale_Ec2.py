# ax^2 + bx + c = 0

a = float(input("Termino  cuadratico    a :"))

b = float(input("Termino lineal         b :"))

c = float(input("Termino independiente  c :"))

# Formula general
# (-b +- raiz(b^2-4ac))/2a

def formula_general(a,b,c):
     x1 = (-b + (b**2-4*a*c)**(1/2))/2*a
     x2 = (-b - (b**2-4*a*c)**(1/2))/2*a
     return x1, x2

#Si solo queremos soluciones reales, entonces el discriminate
# debe ser mayor a cero

dis = b**2-4*a*c

if dis < 0:
     print("No hay raices reales")

else:
     x1,x2 = formula_general(a,b,c)
     print("La primera raiz  :",x1)
     print("La segunada raiz :",x2)
     