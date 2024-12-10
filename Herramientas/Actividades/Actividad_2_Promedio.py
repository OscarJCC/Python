"""
Nombre: Actividad_2_promedio
Fecha: 01/08/2021
Autor: Oscar Joel Castro Contreras
Descripcion:
Escribir un programa que calcule el promedio de una lista de datos, para esto, 
no pueden utilizar la función sum(), ni la función len().
"""

#Funciones
def promedio(numel):
     i = 0
     suma = 0
     
     while i >= 0 and i < numel:
          print("Dato",i+1,"de la lista")
          datos = float(input())
          suma += datos
          i += 1
     
     return suma/numel
          
#Introduccion
print("""
                     HOLA BIENVENIDOS AL PROGRAMA --Actividad_2_promedio--
     Este programa calcula el promedio de una lista de numeros, el programa te pregunta
     cuantos datos tiene la lista de la que quieres sacar el promedio y despues te pide
     cada uno de los datos de la lista.""")

N = "Si"

while N == "si" or N == "Si" or N == "SI" or N == "sI":
     numel = int(input("\n¿Cuantos datos tiene la lista?\n"))
     print("\nEL promedio es :",promedio(numel))
     
     N = str(input("\n¿Deseas obtener el promedio de otra lista de datos? si:no\n"))