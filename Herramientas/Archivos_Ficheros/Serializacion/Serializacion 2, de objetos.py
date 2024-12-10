import pickle

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
          
coche1 = Vehiculos("Mazda","RX7")

coche2 = Vehiculos("Seat","Leon")

coche3 = Vehiculos("Renault","Megane")

coches = [coche1,coche2,coche3]

fichero = open("Los_Coches","wb")

pickle.dump(coches,fichero)

fichero.close()

del fichero

ficheroA = open("Los_Coches","rb") # Esto no se puede hacer desde otro archivo ya que
                                   # se estan usando objetos y los metodos los tiene

Mis_Coches = pickle.load(ficheroA)

ficheroA.close()

for c in Mis_Coches:
     print(c.estado(),"\n")

del ficheroA