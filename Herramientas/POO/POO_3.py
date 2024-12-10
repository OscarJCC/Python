
class Vehiculos():
     
     def __init__(self,marca,modelo):
          
          self.Marca = marca
          self.Modelo = modelo
          self.EnMarcha = False
          self.Acelera = False
          self.Frena = False
     
     def arrancar(self):
          self.EnMarcha = True
          
     def acelerar(self):
          self.Acelera = True
     
     def frenar(self):
          self.Frena = True
     
     def estado(self):
          print("Marca:", self.Marca, "\nModelo:", self.Modelo,
                "\nEn Marcha:", self.EnMarcha, "\nAcelerando:", 
                self.Acelera, "\nFrenando:", self.Frena)
          
class Moto(Vehiculos): #Para que la clase Moto herede las propiedades y metodos de la clase Vehiculos
     
     hcaballito = ""
     
     def caballito(self):
          self.hcaballito = "Va haciendo el caballito"
     
     def estado(self): #Al escribir este metodo que tambien se encuantra la clase se heredo, este se sobre escribe
          print("Marca:", self.Marca, "\nModelo:", self.Modelo,
                "\nEn Marcha:", self.EnMarcha, "\nAcelerando:", 
                self.Acelera, "\nFrenando:", self.Frena,
                "\n", self.hcaballito)
          
class Camioneta(Vehiculos):
     
     def carga(self,cargar):
          
          self.cargado = cargar
          
          if self.cargado:
               return "Camioneta cargada"
          else:
               return "Camioneta no cargada"

class VElectric():
     
     def __init__(self):
          self.autonomia = 100
          
     def cargarEnergia(self):
          
          self.cargando = True
          
class BiciElectric(VElectric,Vehiculos): #Como se ve esta clase esta herdando 2 clases y se le da preferencia a la primera clase colocada como su constructor
                                        #En este caso el constructor que se hereda es el de la clase VElectric
     
     pass


MiMoto = Moto("Honda", "CBR") #Como se esta heredando se necesita replicar las condiciones necesarias de clase heredada

MiMoto.caballito()

MiMoto.estado()

print("\n")

MiCamioneta = Camioneta("Renault","Kangoo")

MiCamioneta.arrancar()

MiCamioneta.estado()

print(MiCamioneta.carga(True))

print("\n")

MiBici = BiciElectric("Orebea","HT1030") #Esto causa error ya que el constructor heredade 
                                         #es de la clase VElectric por lo que en los parentesis no pide nada
                                         #Esto depende de cual es la primera clase que se escribe al heredar las clases
                                         #VElectric y Vehiculo 

MiBici.estado()
