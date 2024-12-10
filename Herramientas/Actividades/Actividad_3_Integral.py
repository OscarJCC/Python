"""
Nombre: Actividad_3_Integral
Fecha: 01/08/2021
Autor: Oscar Joel Castro Contreras
Descripcion:
La integración es un problema numérico muy interesante, en general una integral podemos aproximarla 
por medio de una sumatoria
∫_a^b f(x)dx ≈ ∑_(x=a)^b f(x)dx

Si el intervalo [a,b] esta dividido en N espacios, tal que
N=(b-a)/dx

Entonces, la sumatoria es lo siguiente,
∑_(x=a)^b f(x)dx = f(a)dx + f (a+dx)dx + f(a+2dx)dx + ⋯ + f(a+Ndx)dx

que podemos observar,
f(a + Ndx) = f(b)

Para probar este método, escriba un programa que realice la siguiente integral
∫_0^1〖4√(1-x^2 )〗 dx

Para esto considere la sumatoria, puede tomar en cuenta que dx es un número muy pequeño, 
por ejemplo dx=0.0001. Por último, el resultado ¿A qué número se parece? ¿Qué bucle es mejor utilizar?

"""

print("""
                    HOLA BIENVENIDO AL PROGRAMA --Actividad_3_Integral--
     Este programa calcula la integral definidad de 0 a 1 de la funcion 4(raiz(1 - (x^2)))
     usando una sumatoria.
     """)

lim_a = 0
lim_b = 1
dx = .0001
N = (lim_b - lim_a)/dx

print("∫_0^1(4√(1-(x^2)))dx\n")

i = 0
resultado = 0

while i <= N:
     funcion = (4*((1-(lim_a+(i*dx))**(2))**(1/2))*dx)
     resultado += funcion
     i += 1
     
print("El resultado al resolver la integral es:",resultado)

print("""
     ¿A que numero se parece?
     Se parece al numero Pi""")
print("""
     ¿Que bucle es mejor utilizar?
     Para mi fue mas facil usar el bucle while,
     por lo que creo que ese es el mejor utilizar el bucle while
      """)