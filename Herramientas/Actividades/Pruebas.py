Datos = [10,9,8,7,6,5,4,3,2,1,0]

ent = 0
for i in Datos:
     ent +=1

for i in range(1,ent):
     for j in range(ent-i):
          if(Datos[j] > Datos[j+1]):
               aux = Datos[j]
               Datos[j] = Datos[j+1]
               Datos[j+1] = aux

print("Ordenamiento de forma desendente")
print(Datos)

if ent % 2 == 0:
     div = ent/2
     med = Datos[int(div)]
     
else:
     div = ent //2
     print(div)
     med = ((Datos[div]+Datos[div+1]))/2