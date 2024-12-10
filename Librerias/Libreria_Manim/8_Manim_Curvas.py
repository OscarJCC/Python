from manim import *
import numpy as np

class manimCurvasAnimacion1(ThreeDScene):
     def construct(self):
          cielo = "#C4DDFF"
          azul = "#001D6E"
          rojo = "#B20600"
          
          self.camera.background_color = cielo
          self.play(Write(Text("Epicicloide",color = azul).move_to(3.5*UP)))
          
          ax = Axes(x_range = [-3.5,3.5,1], y_range = [-3.5,3.5,1], x_length = 7, y_length = 7).move_to(np.array([-3.5,0,0]))
          ax.set_color(azul)
          self.play(Write(ax))
          
          circuloG = ParametricFunction(lambda u: np.array([2*np.cos(u),2*np.sin(u),0]), color = BLUE, t_range = np.array([0,2*PI,0.01])).move_to(ax.coords_to_point(0,0))
          self.play(Write(circuloG), run_time = 1)
          self.wait(2)
          
          epicicliode = ParametricFunction(lambda u: np.array([2.5*np.cos(u) - 0.5*np.cos(5*u),2.5*np.sin(u) - 0.5*np.sin(5*u),0]), color = PURPLE, t_range = np.array([0,4*PI,0.01])).move_to(ax.coords_to_point(0,0))
          
          namex = MathTex(r"x = 2.5\cos(\theta) - 0.5\cos(5\theta)").move_to(3.5*RIGHT + UP).set_color(BLACK)
          namey = MathTex(r"y = 2.5\sin(\theta) - 0.5\sin(5\theta)").move_to(3.5*RIGHT).set_color(BLACK)
          rango = MathTex(r"\theta \in(0,5\pi)").move_to(3.5*RIGHT + DOWN).set_color(BLACK)
          
          self.play(Write(epicicliode),Write(namex),Write(namey),Write(rango), run_time = 10)
          self.wait(2)
          
animacion = manimCurvasAnimacion1()
animacion.render()