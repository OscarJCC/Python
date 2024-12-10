
N = int(input("Dame el numero que deseas: "))

i = 1

# Operacion modulo % --a % b--

while i<=N:
     
     if i % 2 == 0:
          print (f"{i} es un numero par")
          
     else:
          print(f"{i} es un numero impar")
     
     i += 1