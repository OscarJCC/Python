from manim import *
import numpy as np

class manimSuperficiesAnimacion1(ThreeDScene):
     def construct(self):
          cielo = "#C4DDFF"
          azul = "#001D6E"
          rojo = "#B20600"
          
          self.camera.background_color = cielo
          self.add_sound("Ekstrak - Belt (Need For Speed Carbon FLAC).mp3 ")
          
          axes = ThreeDAxes().set_color(azul) # Crea los ejes en 3D
          
          x = MathTex("x", color = azul).move_to(np.array([5,0.5,0]))
          
          y = MathTex("y", color = azul).move_to(np.array([0.5,5,0]))
          
          self.set_camera_orientation(phi = 65*DEGREES, theta = 60*DEGREES) # Con este metodo  le damos la orientacion a la grafica 3D, los angulos son de las coordenadas esfericas
          
          self.add(axes,x,y)
          
          text3d = MathTex("z = (x^2 + 3y^2)e^{1 - x^2 - y^2}", color = BLACK).to_corner(UL) # Usamos .to_corner() para ubicar en las esquinas se usa un argumento 
                                                                                               # UL -> Esquina superior derecha, UR -> Esquina superior izquierda
                                                                                               # DL -> Esquina inferior derecha, DR -> Esquina inferior izquierda
          self.add_fixed_in_frame_mobjects(text3d) # Este metodo hace que si tiene movimiento o rotacion este objeto se queda estatico
          self.play(Write(text3d))
          
          # checkerboard_colors = [RED_D,RED_E] - Permite pintar la curva como un tablero de ajedres en la lsita pide 2 colores diferentes
          # resolution = (15,32)) - 
          curva = Surface(lambda u,v: np.array([u,v,(u**2 + 3*v**2)*np.exp(1 - u**2 - v**2)]), v_range = [-3,3], u_range = [-3,3], checkerboard_colors = [RED_D,RED_E], resolution = (15,32))
          curva.set_fill_by_checkerboard(rojo,azul, opacity = 0.5) # Permite pintar la curva con un tablero de ajedres, resive de argumentos 2 colores y la transparencia con opacity
          
          self.play(Write(curva))
          self.wait(5)
          
          text = MathTex(r"\theta\rightarrow\quad", r"0^\circ", r"\\ \phi\rightarrow\quad", r"0^\circ", color = BLACK).to_corner(DR)
          self.add_fixed_in_frame_mobjects(text)
          
          self.move_camera(theta = 0, phi = 0) # Permite hacer el movimiento de la camara, recibe de argumentos los angulos de las coordenadas esfericas
          self.wait(5)
          
          text1 = MathTex(r"\theta\rightarrow\quad", r"0^\circ", r"\\ \phi\rightarrow\quad", r"{45}^\circ", color = BLACK).to_corner(DR)
          self.play(FadeOut(text[1],text[3]))
          self.add_fixed_in_frame_mobjects(text1[1],text1[3])
          
          self.move_camera(theta = 0, phi = PI/4)
          self.wait(5)
          
          text2 = MathTex(r"\theta\rightarrow\quad", r"0^\circ", r"\\ \phi\rightarrow\quad", r"{90}^\circ", color = BLACK).to_corner(DR)
          self.play(FadeOut(text1[1],text1[3]))
          self.add_fixed_in_frame_mobjects(text2[1],text2[3])
          
          self.move_camera(theta = 0, phi = PI/2)
          self.wait(5)
          
          text3 = MathTex(r"\theta\rightarrow\quad", r"{45}^\circ", r"\\ \phi\rightarrow\quad", r"{90}^\circ", color = BLACK).to_corner(DR)
          self.play(FadeOut(text2[1],text2[3]))
          self.add_fixed_in_frame_mobjects(text3[1],text3[3])
          
          self.move_camera(theta = PI/4, phi = PI/2)
          self.wait(5)
          
          text4 = MathTex(r"\theta\rightarrow\quad", r"{45}^\circ", r"\\ \phi\rightarrow\quad", r"{60}^\circ", color = BLACK).to_corner(DR)
          self.play(FadeOut(text3[1],text3[3]))
          self.add_fixed_in_frame_mobjects(text4[1],text4[3])
          
          self.move_camera(theta = PI/4, phi = PI/3)
          self.wait(5)
          
          self.begin_ambient_camera_rotation(rate = 0.5 ) # Este metodo hace una rotacion de la graficá continua, recibe el argumento rate = al cual se le da la rapides del giro 
          self.wait(20)                                  # esta rotacion se detiene hasta que pase el tiempo del .wait()

class manimSuperficiesAnimacion2(ThreeDScene):
     def construct(self):
          cielo = "#C4DDFF"
          azul = "#001D6E"
          rojo = "#B20600"
          
          self.camera.background_color = cielo
          
          axes = ThreeDAxes().set_color(azul)
          
          x = MathTex("x", color = azul).move_to(np.array([5,0.5,0]))
          
          y = MathTex("y", color = azul).move_to(np.array([-0.5,5,0]))
          
          self.set_camera_orientation(phi = 65*DEGREES, theta = 60*DEGREES)
          
          self.add(axes,x,y)
          
          textEsfera = MathTex("Esfera", color = BLACK).to_corner(UL)
          self.add_fixed_in_frame_mobjects(textEsfera)
          self.play(Write(textEsfera))
          
          esfera = Surface(lambda u,v: np.array([2*np.cos(u)*np.sin(v),2*np.sin(u)*np.sin(v),2*np.cos(v)]), u_range = [-PI,PI], v_range = [0,2*PI], resolution = (15,32))
          #esfera.set_fill_by_checkerboard(rojo,azul, opacity = 0.5)
          self.play(Write(esfera), run_time = 5)
          self.wait(2)
          
          self.play(FadeOut(textEsfera))
          textToro = MathTex("Toro", color = BLACK).to_corner(UL)
          self.add_fixed_in_frame_mobjects(textToro)
          self.play(Write(textToro))
                    
          toro = Surface(lambda u,v: np.array([(2 + np.cos(v))*np.cos(u),(2 + np.cos(v))*np.sin(u),np.sin(v)]), u_range = [-PI,PI], v_range = [0,2*PI], resolution = (15,32))
          #toro.set_fill_by_checkerboard(rojo,azul, opacity = 0.5)
          self.play(Transform(esfera,toro), run_time = 5)
          self.wait(2)
          
          self.play(FadeOut(textToro))
          textCatenoide = MathTex("Catenoide", color = BLACK).to_corner(UL)
          self.add_fixed_in_frame_mobjects(textCatenoide)
          self.play(Write(textCatenoide)) 
                    
          catenoide = Surface(lambda u,v: np.array([np.cosh(u)*np.cos(v),np.cosh(u)*np.sin(v),u]), u_range = [-1,1], v_range = [-PI,PI], resolution = (15,32))
          catenoide.set_fill_by_value(axes = axes, colors = [(RED,-1),(YELLOW,0),(BLUE,1)], axis = 2)
          #catenoide.set_fill_by_checkerboard(rojo,azul, opacity = 0.5)
          self.play(Transform(esfera,catenoide), run_time = 5)
          self.wait(2)
          
animacion = manimSuperficiesAnimacion2()
animacion.render()