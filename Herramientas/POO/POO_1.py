# --class-- nos permite crear una clase que es la base o estructura
# principal para crear un objetos o varios que tengan en comun esta 
# base para su creacion, ejemplo los coches, todos tienen de base 
# un chasis y 4 ruedas.

class Coche():
     
     # Propiedades del coche
     LargoChasis = 250
     AnchoChasis = 120
     Ruedas = 4
     EnMarcha = False

     # A la clase se le da un comportamiento con un metodo
     # En este caso el coche puede tener de comportamiento Girar, Arrancar,
     # Acelerar, Frenar, Etc.
     # El metodo se le aplica a la clase con
     # def function(self):  # self hace referencia al objeto perteneciente a la clase
     #    pass
     
     #Metodo o comportamiento
     def arrancar(self):
          self.EnMarcha = True #--self-- permite cambiar una de las propiedades ocacionando un comportamiento

     def Estado(self): #Ahora el coche nos puede decir si tea apagado o arrancado
          if(self.EnMarcha):
               return "El coche esta en marcha"
          else:
               return "El coche esta parado"
#Construccion de los objetos peretencecientes a la clase

Micoche = Coche() #Primer objeto, a esto se le llama Instanciar o ejemplarizar una clase

print("El largo del coche es:",Micoche.LargoChasis,"m") #Permite ver las propiedades del coche
print("El coche tiene:",Micoche.Ruedas,"Ruedas")
print("El ancho del coche es:",Micoche.AnchoChasis,"m")
print("El esta apagado:",Micoche.EnMarcha)

print("\n")

Micoche.arrancar()  #Aqui se llama al metodo arrancar que recibe de parametro el objeto
                    # Micoche para que ejecute el comportamiento o metodo que se llamo

print(Micoche.Estado())

# --> Entonces la clase Coche tiene:
#    4 Propiedades (LargoChasis, AnchoChasis, Ruedas, EnMarcha)
#    2 Comportamientos (Arrancar, Estado)