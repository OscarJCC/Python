# range (Final)
# range (inicio, Final)
# range (inicio, Final, Salto)

for i in range(7,11,2):
     
     print(i)
     
print("\n",range(11)) # list ---- tuple

x = list(range(1,101))

print(x)

#Una cadena de textos tambien se puede interar en el
#bucle for

H = "Hola mundo, estamos aprendiendo bucles"

for letra in H:
     
     print(letra,end="")
     print(f"La letra es: {letra}") #print("La letra es: ",letra)

for k in range(11):
     
     print(f"El numero es {k}")