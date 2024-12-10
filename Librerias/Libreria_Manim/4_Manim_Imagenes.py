from manim import *
import numpy as np

class manimImagenesAnimacion1(Scene):
     def construct(self):
          imagen = ImageMobject("fondo.jpg").scale(1.5) # Permite colocar una imagen
          self.add_sound("Wars Of Faith.mp3")
          self.add(imagen)
          
          titulo = Text("Movimiento Rectilineo",color = BLACK).move_to(3.5*UP)
          self.play(Write(titulo))
          self.wait(2)
          
          lugar0 = ImageMobject("Lamborghini-Car.png").move_to(2.3*DOWN+5.1*LEFT).scale(0.4)
          self.add(lugar0)
          self.wait(2)
          
          lugar1 = lugar0.copy() # Pemite compiar el elemento al que seéle aplica el metodo
          lugar1.move_to(2.3*DOWN+5.1*RIGHT)
          self.play(Transform(lugar0,lugar1),run_time = 3) # con run_time le damos el tiempo que queremos que dure la trnsformacion en segundo
          self.wait(2)
          
          tiempo = SVGMobject("Reloj.svg").move_to(2*UP+5.1*RIGHT).scale(2) # Permite colocar imagenes del formato .svg
          self.play(Write(tiempo)) # La imagenes .svg se pueden escribir como un texto
          self.wait(2)
          
animacion = manimImagenesAnimacion1()
animacion.render()