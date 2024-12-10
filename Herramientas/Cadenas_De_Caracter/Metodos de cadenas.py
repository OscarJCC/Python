nombre_usuario = " Oscar Joel Castro Contreras "

print("\nNombvre de Usuario:",nombre_usuario)

print("\nNombvre de Usuario:",nombre_usuario.upper()) #Convierte los caracteres de una variable str en mayusculas

print("\nNombvre de Usuario:",nombre_usuario.lower()) #Convierte los caracteres de una variable str en minusculas

print("\nNombvre de Usuario:",nombre_usuario.capitalize()) # Convierte el primer caracter de una variable str en mayuscula

print("\nNombvre de Usuario:",nombre_usuario.count("o")) # Nos dice cuantas veces aparece el mismo caracter en una variable str

print("\nNombvre de Usuario:",nombre_usuario.find("O")) # Toma a la variable str como una lista y nos dice en que espacio se encuantra el caracter pedido

print("\nNombvre de Usuario:",nombre_usuario.isdigit()) # Nos dice si la variable es un digito o un caracter

print("\nNombvre de Usuario:",nombre_usuario.isalnum()) # Comprueva si la variable es un alphanumerico

print("\nNombvre de Usuario:",nombre_usuario.isalpha()) #Compruve si la variable solo tiene letras sin contar los espacios

print("\nNombvre de Usuario:",nombre_usuario.split()) # Separa en una lista las palabras en una cadena de caracteres por los espacios

print("\nNombvre de Usuario:",nombre_usuario.strip()) # Borra los espacios por delante y por detras

print("\nNombvre de Usuario:",nombre_usuario.replace("Joel","Luis")) # Cambia una palabra por otra dentro de la variable str

#-----------------------------

Edad = input("\nIntroduce la edad:")

while Edad.isdigit() == False:
     print("Valor de edad no es numerico")
     
     Edad = input("\nIntroduce la edad:")

if int(Edad) < 18:
     print("Menor de edad")
else:
     print("Mayor de edad")