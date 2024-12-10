from manim import *
import numpy as np

class manimTextoAnimacion1(Scene):
    def construct(self):
        texto = Text("Hola, Mundo") # Text nos permite crear un variable tipo texto
        self.add(texto) # nos pemite agragar el texto a la animacion sin ningun efecto especial
        self.wait(3) # Se exiende la animacion el tiempo en segundos que se le de como argumento en este caso 3 segundos
        self.remove(texto) # Permite quitar el texto que se le esta dando como argumento
        self.wait(3)
         
class manimTextoAnimacion2(Scene):
     def construct(self):
         texto = Text("Hola, Mundo")
         self.play(FadeIn(texto)) # .Play permite agregar un efecto especial al texto para incluir o quitar el texto de la animacion
         self.wait(3)
         self.play(FadeOut(texto))
         self.wait(3)
         self.play(Write(texto))
         self.wait(3)
         
class manimTextoAnimacion3(Scene):
     def construct(self):
          
          rejilla = NumberPlane() # Crea una rejilla de lineas blacas en la animacion
          self.add(rejilla)
          
          texto1 = Text("A").move_to(RIGHT+UP) # con .move_to le damos una posicion al texto la cordenada es el centro de la palabra,
          texto2 = Text("B").move_to(LEFT+DOWN) # se mueve una unidad hacia donde se coloque en el argumento
          texto3 = Text("C").move_to(LEFT*2.5) # para mover mas unidades multiplicamos la posicion que se quiere por las unidades que queremos que se muevan en esa direccion
          texto4 = Text("D").move_to(DOWN*3.5)
          
          self.add(texto1,texto2,texto3,texto4)
          self.wait(3)

class manimTextoAnimacion4(Scene):
     def construct(self):
          
          rejilla = NumberPlane()
          self.add(rejilla)
          
          texto1 = Text("A").move_to(np.array([1,1,0])) # para colocar la posicion con cordenadas usamos vectores con numpy
          texto2 = Text("B").move_to(np.array([-1,-1,0])) # Se tiene que colocas las 3 coordenadas x,y,z
          texto3 = Text("C").move_to(np.array([-2.5,0,0])) #
          texto4 = Text("D").move_to(np.array([0,-3.2,0]))
          
          self.add(texto1,texto2,texto3,texto4)
          self.wait(3)
          
class manimTextoAnimacion5(Scene):
     def construct(self):
          
          texto1 = Text("Hola, Mundo").move_to(2*UP)
          texto2 = Text("Hola, Mundo").move_to(3*RIGHT+2*UP)
          texto3 = Text("Hola, Mundo").move_to(3*RIGHT)
          texto4 = Text("Hola, Mundo").move_to(3*RIGHT+2*DOWN)
          texto5 = Text("Hola, Mundo").move_to(2*DOWN)
          texto6 = Text("Hola, Mundo").move_to(3*LEFT+2*DOWN)
          texto7 = Text("Hola, Mundo").move_to(3*LEFT)
          texto8 = Text("Hola, Mundo").move_to(3*LEFT+2*UP)
          texto9 = Text("Hola, Mundo").move_to(2*UP)
          
          self.play(FadeIn(texto1))
          self.wait(1)
          self.play(Transform(texto1,texto2))
          self.wait(1)
          self.play(Transform(texto1,texto3))
          self.wait(1)
          self.play(Transform(texto1,texto4))
          self.wait(1)
          self.play(Transform(texto1,texto5))
          self.wait(1)
          self.play(Transform(texto1,texto6))
          self.wait(1)
          self.play(Transform(texto1,texto7))
          self.wait(1)
          self.play(Transform(texto1,texto8))
          self.wait(1)
          self.play(Transform(texto1,texto9))
          self.wait(1)
          
animacion = manimTextoAnimacion5()
animacion.render()
