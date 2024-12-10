from manim import *
import numpy as np

class manimGeometriaAnimacion1(ThreeDScene):
     def construct(self):
          rosa = "#C12786"
          gris = "#AAAAAA"
          azul = "#13316D"
          verde = "#008000"
          
          c0 = Circle(radius = 3, color = gris) #Con Circle creamos un circulo que recibe de argumentos el radio
          self.play(Create(c0),run_time = 2)
          self.wait(2)
          
          coor1 = np.array([3,0,0])
          coor2 = np.array([1.5,2.5980,0])
          coor3 = np.array([-1.5,2.5980,0])
          coor4 = np.array([-3,0,0])
          coor5 = np.array([-1.5,-2.5980,0])
          coor6 = np.array([1.5,-2.5980,0])
          
          p1 = Dot(color = azul).move_to(coor1) #Con Dot creamos un punto
          self.add(p1)
          c1 = Circle(radius = 3, color = rosa).shift(coor1)# Los circulos creados con Circle se mueven con .shift() con el argumento de la posicion del centro del circulo
          self.play(Create(c1),run_time = 2)
          self.wait(2)
          
          p2 = Dot(color = azul).move_to(coor2)
          self.add(p2)
          c2 = Circle(radius = 3, color = rosa).shift(coor2)
          self.play(Create(c2),run_time = 2)
          l1 = Line(p1, p2, color = verde) # Con Line se crea una linea que va desde un punto iniciol a punto final que se colocan en el argumento
          self.play(Create(l1))
          self.wait(2)
          
          p3 = Dot(color = azul).move_to(coor3)
          self.add(p3)
          c3 = Circle(radius = 3, color = rosa).shift(coor3)
          self.play(Create(c3),run_time = 2)
          l2 = Line(p2, p3, color = verde)
          self.play(Create(l2))
          self.wait(2)
          
          p4 = Dot(color = azul).move_to(coor4)
          self.add(p4)
          c4 = Circle(radius = 3, color = rosa).shift(coor4)
          self.play(Create(c4),run_time = 2)
          l3 = Line(p3, p4, color = verde)
          self.play(Create(l3))
          self.wait(2)
          
          p5 = Dot(color = azul).move_to(coor5)
          self.add(p5)
          c5 = Circle(radius = 3, color = rosa).shift(coor5)
          self.play(Create(c5),run_time = 2)
          l4 = Line(p4, p5, color = verde)
          self.play(Create(l4))
          self.wait(2)
          
          p6 = Dot(color = azul).move_to(coor6)
          self.add(p6)
          c6 = Circle(radius = 3, color = rosa).shift(coor6)
          self.play(Create(c6),run_time = 2)
          l5 = Line(p5, p6, color = verde)
          self.play(Create(l5))
          
          l6 = Line(p6, p1, color = verde)
          self.play(Create(l6))
          self.wait(2)
          
          self.play(FadeOut(c1, c2, c3, c4, c5, c6))
          self.wait(2)
          self.play(FadeOut(c0))
          self.wait(2)
          
          self.play(Write(Text("HEXAGONO",color = azul).move_to(3.5*UP)))
          self.wait(2)
          
animacion = manimGeometriaAnimacion1()
animacion.render()