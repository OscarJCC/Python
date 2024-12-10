"""
Nombre: Actividad_1_Calculadora
Fecha: 30/07/2021
Autor: Oscar Joel Castro Contreras
Descripcion:
Realizar un programa de una calculadora con las operaciones aritméticas vista en clase (clase 7). 
Lo único que pido es que hagan un menú para poder seleccionar la operación que el usuario deseé. 
Intente utilizar todo lo que hemos visto.
Tome en cuenta que en la operación división el usuario puede digitar 0 como denominador, 
lo que causaría un error. Evite que se presente ese error.
"""
#Funciones
def calculadora (a,b,c):
     
     operaciones = [(a,"+",b,"=",a + b),
                    (a,"-",b,"=",a - b),
                    (a,"x",b,"=",a * b),
                    (a,"/",b,"=",a / b),
                    (a,"%",b,"=",a % b),
                    (a,"^",b,"=",a ** b),
                    (a,"//",b,"=",a // b)]

     return operaciones[c]

#Introduccion
print("""
                    HOLA BIENVENIDO AL PROGRAMA --Actividad_1_Calculadora--
     Este programa realiza operaciones entre 2 numeros que se muestran en un menu, el programa 
     te pide colocar el numero que le corresponde a la operacion que deseas que se realice del 
     menu y despues te pide que escribas los 2 numeros con lo que quieres que se haga la operacion.""")

N = "Si"

while N == "si" or N == "Si" or N == "SI" or N == "sI":
     
     print("""
                     MENU
          - suma              = 0
          - resta             = 1
          - multiplicacion    = 2
          - division          = 3
          - modulo            = 4
          - exponente         = 5
          - division entera   = 6
          """)

     op = int(input("Coloca el numero de la operacion que deseas realisar: "))
     
     if op < 0 or op > 6:
          print("El numero ",op," no coresponde a ninguna operacion")
     
     elif op >= 0 and op <= 2:
          a = float(input("Primer numero  :"))
          b = float(input("Segundo numero :"))
          d,e,f,g,h = calculadora (a,b,op)
          print(d,e,f,g,h)

     elif op == 4:
          a = float(input("Numerador   :"))
          b = float(input("Denominador :"))
          d,e,f,g,h = calculadora (a,b,op)
          print(d,e,f,g,h)
     
     elif op == 5:
          a = float(input("Base  :"))
          b = float(input("Exponente :"))
          d,e,f,g,h = calculadora (a,b,op)
          print(d,e,f,g,h)
     
     while op == 3 or op == 6:
          a = float(input("Numerador   :"))
          b = float(input("Denominador :"))
     
          if b == 0:
               print("\nLa division no es valida, (--no se puede dividir entre cero--)\n")
          
          else:
               d,e,f,g,h = calculadora (a,b,op)
               print(d,e,f,g,h)
               op += 1
               
     N = str(input("\n¿Deseas hacer otra operacion? si:no\n"))

     