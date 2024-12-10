"""
Funcion que genera una lista de numeros pares
def generapares(limite):
     
     num = 1
     lisnumpar = []
     
     while num < limite:
          
          lisnumpar.append(num*2)
          
          num = num + 1
     
     return lisnumpar

print(generapares(10))

"""

#Ahora a la funcion anterior la convetimos en un generador
 
def generapares(limite):
     
     num = 1
     #lisnumpar = []
     
     while num < limite:
          
          #lisnumpar.append(num*2)
          
          # yield tiene la utilidad de que cadaves que se llama al 
          #generador este devuelve un elemento generado y se queda 
          #en estado de pause o suspencion sin generar mas elementos 
          #o toda la lista como en una funcion
          
          yield num*2 
            
          num = num + 1
     
     #return lisnumpar
     
#print(generapares(10))

DevPar = generapares(10)

print(next(DevPar)) # next() nos da el primer numero generado
print(next(DevPar)) # Si lo escribimos de nuevo ahora nos da el segundo numero generado