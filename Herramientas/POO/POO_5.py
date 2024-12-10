class Coche():
     def desplazamiento(self):
          print("Se desplaza utilizando 4 ruedas")
          
class Moto():
     def desplazamiento(self):
          print("Se desplaza utilizando 2 ruedas")
          
class Camion():
     def desplazamiento(self):
          print("Se desplaza utilizando 6 ruedas")

#Como se ve todas las clases tiene el mismo metodo, aunque se comporta diferente en cada una
#Y no sotros podemos hace esto:

MiVehiculo = Moto()
#
#MiVehiculo.desplazamiento()
#
MiVehiculo2 = Coche()
#
#MiVehiculo2.desplazamiento()
#
MiVehiculo3 = Camion()
#
#MiVehiculo3.desplazamiento()

#Para no hacer lo anterior podemos usar una funcion que nos permita usar el metodo
#usar el metodo con solo tener de que tipo el el objeto
def desplazamientoVehiculo(vehiculo):
     vehiculo.desplazamiento()

desplazamientoVehiculo(MiVehiculo)

desplazamientoVehiculo(MiVehiculo2)

desplazamientoVehiculo(MiVehiculo3)