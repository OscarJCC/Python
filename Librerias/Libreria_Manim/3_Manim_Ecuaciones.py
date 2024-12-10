from manim import *
import numpy as np

class manimEcuacionesAnimacion1(Scene):
     def construct(self):
          eqn0 = MathTex("2x^2 + 6x + 7 = 0").move_to(3*UP)
          eqn1 = MathTex("x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}").move_to(1.5*UP)
          eqn2 = MathTex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}").move_to(1.5*DOWN)
          eqn3 = MathTex(r"\left( \begin{array}{cc} 1 & 2 \\ 3 & 4 \end{array} \right)").move_to(3*DOWN)
         
          self.play(Write(eqn0))
          self.wait(3)

          self.play(Write(eqn1))
          self.wait(3)

          self.play(Write(eqn2))
          self.wait(3)

          self.play(Write(eqn3))
          self.wait(3)

class manimEcuacionesAnimacion2(Scene):
     def construct(self):
          eqn0 = MathTex("2x^2 + 6x + 7 = 0").move_to(2*UP).scale(2)
          eqn1 = MathTex("2x^2","+ 6x","+ 7"," = 0").move_to(2*DOWN).scale(2) # Dividir la ecuacion de esta forma hace que este se vea como un vector por lo que podemos llamar a animar una parte especifica de la ecuacion
         
          self.play(Write(eqn0))
          self.wait(3)

          self.play(Write(eqn1[0]))
          self.wait(3)
          
          self.play(Write(eqn1[1]))
          self.wait(3)
          
          self.play(Write(eqn1[2]))
          self.wait(3)
          
          self.play(Write(eqn1[3]))
          self.wait(3)

class manimEcuacionesAnimacion3(Scene):
     def construct(self):
          color1 = "#0F2C67"
          color2 = "#CD1818"
          color3 = "#F3950D"
          color4 = "#F4E185"
          
          eqn0 = MathTex("2x^2 + 6x + 7 = 0").move_to(UP).scale(1.5)
          eqn1 = MathTex(r"{-b \pm \sqrt{b^2 - 4ac}}",r"\over",r"{2a}",color = color1).move_to(DOWN).scale(1.5)
          eqn1[1].set_color(color3)
          eqn1[2].set_color(color2)
          
          self.play(Write(eqn0))
          self.wait(3)

          self.play(Write(eqn1[0]))
          self.wait(3)
          
          self.play(Write(eqn1[1]))
          self.wait(3)
          
          self.play(Write(eqn1[2]))
          self.wait(3)

class manimEcuacionesAnimacion4(Scene):
     def construct(self):
          color1 = "#0F2C67"
          color2 = "#CD1818"
          color3 = "#F3950D"
          color4 = "#F4E185"
          
          self.camera.background_color = color1
          
          eqn0 = MathTex("x = ","2.5").move_to(2*UP+2*LEFT).scale(1.5)
          eqn1 = MathTex("y = ","1.5").move_to(2*UP+2*RIGHT).scale(1.5)
          eqn2 = MathTex(r"z^2 = (","2.5",r")^2 + (","1.5",r")^2",color = color4).move_to(DOWN
                                                                                      ).scale(1.5)
          eqn0.set_color(color3)
          eqn1.set_color(color2)
          
          self.play(Write(eqn0))
          self.wait(3)

          self.play(Write(eqn1))
          self.wait(3)
          
          self.play(Write(eqn2[0]),Write(eqn2[2]),Write(eqn2[4]))
          self.wait(3)
          
          self.play(Transform(eqn0[1],eqn2[1]),Transform(eqn1[1],eqn2[3]))
          self.wait(3)
          
animacion = manimEcuacionesAnimacion4()
animacion.render()