from manim import *
import numpy as np

class manimGraficasAnimacion1(Scene):
     def construct(self):
          cielo = "#C4DDFF"
          azul = "#001D6E"
          rojo = "#B20600"
          
          self.camera.background_color = cielo
          
          #Con Axes() creamos los ejes de la grafica
          #Con los argumentos x_range, y_range le damos el rango a cada eje con una lista que incluye [x o y minimo, x o y maximo, divicion en partes]
          #Con el argumento x_axis_config = {"numbers_to_include":[]} permite marcar los numeros que queremos que se muestren con la lista [] pero hadce un redondeo
          
          ax = Axes(x_range = [-1,14,PI], y_range = [-4,4,1], x_length = 9, y_length = 3)#x_axis_config = {"numbers_to_include":[3.14,6.28,9.42,12.56]})
          ax.set_color(azul)
          
          p1x = MathTex('\pi', color = azul).move_to(ax.coords_to_point(PI,-1))     # Para no usar axis_config = {} colocamos directamente con formato latex
          p2x = MathTex('2\pi', color = azul).move_to(ax.coords_to_point(2*PI,-1))  # para que se coloque en las coordenadas de los ejes en .move_to()
          p3x = MathTex('3\pi', color = azul).move_to(ax.coords_to_point(3*PI,-1))  # damos el argumentoax.coords_to_point(), el cual resive otrso argumentos que son
          p4x = MathTex('4\pi', color = azul).move_to(ax.coords_to_point(4*PI,-1))  # (Posicion x, Posicion y)
          
          p1y =  MathTex('1', color = azul).move_to(ax.coords_to_point(-1,1))
          p2y =  MathTex('-1', color = azul).move_to(ax.coords_to_point(-1,-1))
          p1yc = p1y.copy()
          p2yc = p2y.copy()
          p1yc1 =  MathTex('3', color = azul).move_to(ax.coords_to_point(-1,3))
          p2yc1 =  MathTex('-3', color = azul).move_to(ax.coords_to_point(-1,-3))
          p1yc2 =  MathTex('0.5', color = azul).move_to(ax.coords_to_point(-1,0.5))
          p2yc2 =  MathTex('-0.5', color = azul).move_to(ax.coords_to_point(-1,-0.5))
          
          self.play(Write(ax),Write(p1x),Write(p2x),Write(p3x),Write(p4x))
          self.wait(3)
          
          curva0 = ax.plot(lambda x: np.sin(x), color = rojo, x_range = [0,4*PI])
          
          curva1 = curva0.copy()
          
          curva2 = ax.plot(lambda x: 3*np.sin(x), color = rojo, x_range = [0,4*PI])
          
          curva3 = ax.plot(lambda x: 0.5*np.sin(x), color = rojo, x_range = [0,4*PI])
          
          eqn0 = MathTex(r"y = \sin{x}", color = azul).move_to(UP*2.5).scale(2)
          
          eqn1 = eqn0.copy()
          
          eqn2 = MathTex(r"y = 3\sin{x}", color = azul).move_to(UP*2.5).scale(2)
          
          eqn3 = MathTex(r"y = 0.5\sin{x}", color = azul).move_to(UP*2.5).scale(2)
          
          self.play(Write(curva1),Write(eqn1),Write(p1y),Write(p2y))
          self.play(Transform(curva1,curva2),Transform(eqn1,eqn2),Transform(p1y,p1yc1), Transform(p2y,p2yc1), run_time = 5)
          self.play(Transform(curva1,curva3),Transform(eqn1,eqn3),Transform(p1y,p1yc2), Transform(p2y,p2yc2), run_time = 5)
          self.play(Transform(curva1,curva0),Transform(eqn1,eqn0),Transform(p1y,p1yc), Transform(p2y,p2yc), run_time = 5)
          
animacion = manimGraficasAnimacion1()
animacion.render()