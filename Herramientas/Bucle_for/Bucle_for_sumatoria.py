# 1+2+3+4+5+6+7+8+.....
# Sumar hasta el numero 100
suma=0
for i in range(101):
     suma += i
     
print("La suma de los primeros 100 enteros es:",suma)

suma=0
for j in range(1001):
     suma += j
     
print("La suma de los primeros 1000 enteros es:",suma)

#Si queremos sumar hasta n, entonces
#suma = n(n+1)/2

n = 1000
suma=0
for k in range(n+1):
     suma += k
     
print(suma)
