from manim import *
import numpy as np

class manimFuncionAnimacion1(ThreeDScene):
     def construct(self):
          rojo = "#CC0000"
          gris = "#666666"
          azul = "#0000FF"
          blanco = "#FFFFFF"
          
          self.camera.background_color = blanco
          
          eq = MathTex(r"y = e^{kx}", color = azul).to_corner(UL).scale(1.5)
          ax  = Axes(x_range = [-3,3,1], y_range = [-1,2,1], x_length = 16, y_length = 8).set_color(gris)
          self.play(Write(eq),Write(ax))
          self.wait(2)
          
          curva = ax.plot(lambda x: np.exp(-3*x), color = rojo)
          t = ValueTracker(-3)
          d = DecimalNumber(-3)
          d.add_updater(lambda z: z.set_value(t.get_value()))
          d.move_to(np.array([-5.1,2,0])).set_color(rojo)
          curva.add_updater(lambda z: z.become(ax.plot(lambda x: np.exp(t.get_value() * x), color = rojo)))
          
          k = MathTex("k = ", color = azul).move_to(np.array([-6.2,2,0]))
          
          self.add(k,d,curva)
          self.play(t.animate.set_value(3), run_time = 18)
          self.wait(2)
          
animacion = manimFuncionAnimacion1()
animacion.render()