
calificacion = int(input("Escribe tu calificacion: "))

if calificacion < 70 and calificacion >=0:
     print("Califacacion deficiente")
     
elif calificacion >= 70 and  calificacion < 80:
     print("Calificacion regular")
     
elif calificacion >= 80 and calificacion < 90:
     print("Calificacion buena")
     
elif calificacion >= 90 and calificacion <= 100:
     print("Calificacion excelente")

else:
     print("Calificacion incorrecta")