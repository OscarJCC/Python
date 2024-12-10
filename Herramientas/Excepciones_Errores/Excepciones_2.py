
x = 1
y = 5

try:
     print(x/y)

except ZeroDivisionError:
     
     print("\nNo puedes dividir entre cero\n")

letra ="H"

try:
     print(letra + 10)
     
except TypeError:
     
     print("No puedes sumar letras con numeros\n")

print("Programa terminado!!\n")