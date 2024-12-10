 #Pide nombre , edad y genero de una persona y la va guardando en un fichero llamado FicheroReguard
# El fichero esta codificado en codigo binario
import pickle

class Persona():
     
     def __init__(self,nombre,edad,genero):
          self.Nombre = nombre
          self.Edad = edad
          self.Genero = genero
          print("Se ha creado una persona nueva con el nombre",self.Nombre)
     
     def __str__(self):  #Este metodo convierte en cadena de texto la informacion de un objeto 
          return "{} {} {}".format(self.Nombre,self.Edad,self.Genero)

class ListaPersonas:
     
     Personas = []
     
     def __init__(self):
          Lista_De_Personas = open("FicheroReguard","ab+")
          Lista_De_Personas.seek(0)
          
          try:
               self.Personas = pickle.load(Lista_De_Personas)
               print("Se cargaron {} personas del fichero".format(len(self.Personas)))
          except:
               print("El fichero esta vacio")
               
          finally:
               Lista_De_Personas.close()
               del Lista_De_Personas
     
     def AgregarPersonas(self,P):
          self.Personas.append(P)
          self.GuardarPersonasFichero()
          
     def MostrarPersonas(self):
          for c in self.Personas:
               print(c)
               
     def GuardarPersonasFichero(self):
           Lista_De_Personas = open("FicheroReguard","wb")
           pickle.dump(self.Personas,Lista_De_Personas)
           Lista_De_Personas.close()
           del Lista_De_Personas
           
     def MostrarInfoFichero(self):
          print("La informacion del fichero es la siguente:")
          for c in self.Personas:
               print(c)

MiLista = ListaPersonas()

P = Persona("Oscar",18,"M")
MiLista.AgregarPersonas(P)

MiLista.MostrarInfoFichero()