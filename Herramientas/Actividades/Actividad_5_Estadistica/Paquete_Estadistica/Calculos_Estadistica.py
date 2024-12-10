"""
Nombre: Calculos
Fecha: 16/08/2021
Autor: Oscar Joel Castro Contreras
Este codigo contiene funciones de para poder calcular el promedio, la mediana, la varianza,
la desviacion estandar de un conjunto de datos
"""

def promedio(Datos):
     suma = 0
     ent = 0
     for i in Datos:
          suma += i
          ent += 1
          
     return suma/ent

def mediana(Datos):
     ent = 0
     for i in Datos:
          ent +=1
          
     #ordenamiento de forma cresiente
     for i in range(1,ent):
          for j in range(ent-i):
               if(Datos[j] > Datos[j+1]):
                    aux = Datos[j]
                    Datos[j] = Datos[j+1]
                    Datos[j+1] = aux
     
     if ent % 2 == 0:
          div = ent/2
          med = Datos[int(div)]
     else:
          div = ent //2
          print(div)
          med = ((Datos[div]+Datos[div+1]))/2
     
     return med

def varianza(Datos):
     prom = promedio(Datos)
     suma = 0
     ent = 0
     for i in Datos:
          suma += (i-prom)**2
          ent += 1
     
     return suma/ent

def desviacion_est(Datos):
     var = varianza(Datos)
     return (var)**(1/2)
