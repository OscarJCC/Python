#------Variables------

# Asi se declaran las variables
x = 5

y = 6

#Imprime el valor de las variables
print(x+y)

#Declaracion de una variable string
nombre = "Mi nombre es Oscar"

#Imprime el valor de una variable
print(nombre)

#Imprime un salto de linea
print("\n")

#Imprime el valor de la variable por el numero que se multiplica
print(3*nombre)

#Declaracion de una variable string
comentario = """estoy aqui
programando en python
esta muy loco
"""

print(comentario)

#------Tipos de datos------

"""
int
float
str
complex
bool - (True,False)
"""
#Variable float
pi = 3.1416

#Variables bool >> boliana
var = True
var_2 = False

     #Operacion de numeros complejos

# tomamos raiz(-1) = j enves de i
z = 1+1j

print(z)

#Variable compleja
w = 2+2j

print(z+w)
print(z*w)

print("\n")

     #Operadores bolianas
     
#Imprimen si es verdad o falso
print(7==6)
print(7==7)
print(10!=4)
print(7<2)

     #Operadores logicos (and, or, not)

#Imprimen si es verdad o falso
print(7==7 and 10!=4)
print(7==7 and 10==4)
print(5!=5 or 4>10)

     #Funcion type

print(type(x))
print(type(nombre))
print(type(pi))
print(type(z))
print(type(var))