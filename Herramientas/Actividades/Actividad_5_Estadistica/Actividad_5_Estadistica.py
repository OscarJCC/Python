"""
Nombre: Actividad_5_Estadistica
Fecha: 16/08/2021
Autor: Oscar Joel Castro Contreras
Descripcion:
Crea un módulo que contenga cuatro funciones:
 - Para determinar el promedio de un conjunto de datos.
          x ̅  = ∑_(i=1)^n x_1/n
 - Para determinar la mediana de un conjunto de datos.
 - Para determinar la varianza de un conjunto de datos.
          γ = ∑_(i=1)^n (x_i-x ̅ )^2/n
 - Para determinar la desviación estándar de un conjunto de datos.
          σ = √γ
No puedes utilizar ninguna de las librerías de Python para estas funciones,
además tampoco podrás usar la función sum() ni la función len().
Por último, guarda en un archivo .txt los siguientes datos: Datos
Con estos datos, en otro programa, importa el módulo que creaste con las funciones de estadística.
Mediante manipulación de archivos extrae los datos anteriores y aplica cada una de las funciones.
Es decir, determina el promedio, la mediana, la varianza y desviación estándar de los datos.
"""

#Modulos o paquetes
from Paquete_Estadistica.Calculos_Estadistica import *

#Estraccion de los datos del archivo
archivo = open("DatosActivida5.txt","r")
datos = archivo.readlines()
archivo.close()

#Convercion de los datos del archivo a float
Datos = []
for i in datos:
     Datos.append(float(i))

print("Datos =",Datos,"\n")

print("Promedio =",promedio(Datos),"\n")

print("Mediana = ",mediana(Datos),"\n")

print("Varianza =",varianza(Datos),"\n")

print("Desviacion estandar =",desviacion_est(Datos),"\n")