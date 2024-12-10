try:
     archivo = open("archivo.txt","a")
     
     archivo.write("\nHemos agregado esta linea\n")

     
finally:     
     archivo.close()