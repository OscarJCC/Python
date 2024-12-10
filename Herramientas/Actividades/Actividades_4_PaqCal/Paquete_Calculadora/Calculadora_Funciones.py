"""
Nombre: Calculadora_Funciones
Fecha: 12/08/2021
Autor: Oscar Joel Castro Contreras
Este codigo contiene funciones de cada una de las operaciones aritmeticas que se
utilizaron en la actividad Acomodadas de forma que para la actividad 4 el codigo
sea mas pequeño-
"""
#Funciones
def S(op):
     def suma(a,b):
          return a + b
     a = float(input("Primer numero  :"))
     b = float(input("Segundo numero :"))
     return print(a,"+",b,"=",suma(a,b))

def R(op):
     def resta(a,b):
          return a - b
     a = float(input("Primer numero  :"))
     b = float(input("Segundo numero :"))
     return print(a,"-",b,"=",resta(a,b))

def M(op):
     def multiplicacion(a,b):
          return a * b
     a = float(input("Primer numero  :"))
     b = float(input("Segundo numero :"))
     return print(a,"*",b,"=",multiplicacion(a,b))

def D(op):
     def division(a,b):
          return a / b
     i = 0
     while i ==0:
          try:
               a = float(input("Numerador   :"))
               b = float(input("Denominador :"))
               return print(a,"/",b,"=",division(a,b))
               i = 1
          except:
               print("NO se puede dividir entre cero\n")

def MD(op):
     def modulo(a,b):
          return a % b
     i = 0
     while i == 0:
          try:
               a = float(input("Numerador   :"))
               b = float(input("Denominador :"))
               return print(a,"%",b,"=",modulo(a,b))
               i = 1
          except:
               print("NO se puede dividir entre cero\n")
               
def E(op):
     def exponencial(a,b):
          return a ** b
     a = float(input("Base      :"))
     b = float(input("Exponente :"))
     return print(a,"**",b"=",exponencial(a,b))

def DI(op):
     def divint(a,b):
          return a // b
     i = 0
     while i == 0:
          try:
               a = float(input("Numerador   :"))
               b = float(input("Denominador :"))
               return print(a,"//",b,"=",divint(a,b))
               i = 1
          except:
               print("NO se puede dividir entre cero\n")