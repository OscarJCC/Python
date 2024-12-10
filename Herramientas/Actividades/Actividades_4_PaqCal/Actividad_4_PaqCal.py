"""
Nombre: Actividad_4_PaqCal
Fecha: 15/08/2021
Autor: Oscar Joel Castro Contreras
Descripcion:
A partir de la calculadora hecha en el Actividad 1, crear un paquete llamado Calculadora,
de tal manera que el menú que creaste lo hagas en un archivo aparte y a partir de ese archivo
importes el paquete. Es muy parecido al ejercicio que se realizo en el apartado de módulos.
"""

#Modulo o paquetes
from Paquete_Calculadora.Calculadora_Funciones import *

#Introduccion
print("""
                    HOLA BIENVENIDO AL PROGRAMA --Actividad_1_Calculadora--
     Este programa realiza operaciones entre 2 numeros que se muestran en un menu, el programa 
     te pide colocar el numero que le corresponde a la operacion que deseas que se realice del 
     menu y despues te pide que escribas los 2 numeros con lo que quieres que se haga la operacion.""")

N = "Si"

while N == "si" or N == "Si" or N == "SI" or N == "sI" or N == "s" or N == "S":
     
     print("""
                     MENU
          - suma              = 1
          - resta             = 2
          - multiplicacion    = 3
          - division          = 4
          - modulo            = 5
          - exponente         = 6
          - division entera   = 7
          """)

     op = int(input("Coloca el numero de la operacion que deseas realisar: "))
     
     if op < 1 or op > 7:
          print("El numero ",op," no coresponde a ninguna operacion")
     
     elif op == 1:
          S(op)
          
     elif op == 2:
          R(op)
     
     elif op == 3:
          M(op)
     
     elif op == 4:
          D(op)
     
     elif op == 5:
          MD(op)
     
     elif op == 6:
          E(op)

     elif op == 7:
          DI(op)
          
     N = str(input("\n¿Deseas hacer otra operacion? si:no\n"))