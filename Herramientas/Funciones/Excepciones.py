# Divicion entre cero
x = int(input("Escribe el primer numero:"))
y = int(input("Escribe el segundo numero:"))

#try ejecuta una instruccion
try:
     print(x/y)
     
#except se ejecuta si ocurre un error de sintaxis en la instruccion del try
except:
     
     print("Divicion entre cero")
     
#finally se ejecuta sin importar cualquer cosa que ocurra en el try y el except
finally:
     print("Programa terminado\n")
     
#Suma de palabras con numeros
palabra ="Hola"

try:
     print(palabra + 10)

except:
     print("No se puede sumar")

finally:
     print("Programa terminado\n")