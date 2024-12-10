class Coche():
     
     # Propiedades del coche
     def __init__(self): #Este se le llama constructor y tiene lo que es el estado inicial de la clase
          self.__LargoChasis = 250
          self.__AnchoChasis = 120
          self.__Ruedas = 4 # Se encapsula colocando self.__ y no se puede usar fuera de la clase pero dentro si
          self.__EnMarcha = False
     
     #Metodo o comportamiento
     def arrancar(self,Arrancamos):
          self.__EnMarcha = Arrancamos
          
          if self.__EnMarcha:
               chequeo = self.__ChequeoInt()
          
          if self.__EnMarcha and chequeo:
               return "El coche esta en marcha"
          elif self.__EnMarcha and chequeo == False:
               return "Algo anda mal en el chequeo, no se puede arrancar"
          else:
               return "El coche esta parado"
               

     def Estado(self): 
          print("El largo del coche es:",self.__LargoChasis,"m") 
          print("El coche tiene:",self.__Ruedas,"Ruedas") #Encapsulada con self.__, al hacer esto siempre se debe colocar el self.__
          print("El ancho del coche es:",self.__AnchoChasis,"m")
          
     def __ChequeoInt(self): #Metodo encapsulaso colocando __Nombre del metodo Dos gione bajos
          print("Realizando chequeo interno")
          
          self.Gasolina = "ok"
          self.Aceite ="ok"
          self.Puertas = "cerradas"
          
          if self.Gasolina == "ok" and self.Aceite == "ok" and self.Puertas == "cerradas":
               return True
          else:
               return False

print("------- Primer objeto: -------------")

Micoche = Coche()

Micoche.Estado()

print(Micoche.arrancar(True))

#print(Micoche.ChequeoInt()) #no deve de porder ya que el coche ya esta arrancado por lo que se debe de encapsular el metodo

print("\n")

print("------- segundo objeto: -------------")

Micoche2 = Coche()

Micoche2.Ruedas = 2 #Esto no se debe poder ya que es un estado incial, por lo que se encapsula

Micoche2.Estado()

print(Micoche2.arrancar(False))

#print(Micoche2.ChequeoInt())# no se debe poder ya que el coChe no esta encendido por lo que se encapsula el metodo

# --> Entonces la clase Coche tiene:
#    4 Propiedades (LargoChasis, AnchoChasis, Ruedas, EnMarcha) Se les conocen como estado inicial
#    2 Comportamientos (Arrancar, Estado)