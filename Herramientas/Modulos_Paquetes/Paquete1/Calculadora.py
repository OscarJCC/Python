
#Modulo de calculadora

def suma(x,y):
     return x+y

def resta(x,y):
     return x-y

def multiplicacion(x,y):
     return x*y

def division (x,y):
     try:
          return x/y
     
     except:
          print("No se puede dividir entre cero")
          
def potencia(x,n):
     
     if isinstance(x,int):
          return x**abs(n)

     else:
          raise ValueError("La potencia debe ser un entero")
