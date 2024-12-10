from manim import *
import numpy as np

class manimZOOMAnimacion1(MovingCameraScene):
     def construct(self):
          cielo = "#C4DDFF"
          azul = "#001D6E"
          rojo = "#B20600"
          
          self.camera.background_color = cielo
          self.add_sound("Wars Of Faith.mp3")
          
          mapa = ImageMobject("world-map.png").scale(0.29)
          self.add(mapa)
          self.wait(2)
          
          self.camera.frame.save_state() # Se usa para establecer la pantalla inicial
          
          self.add(NumberPlane().set_color(rojo))
          self.wait(2)
          
          # self.camera.frame.animate.scale(0.5).move_to(np.array([-3.5,2,0]))
          # Pemirte hacer un zoom con el .scale() el cual recibe el argumento del aumento
          # y con el .move_to, damos el punto central hacia donde se hara el zoom.
          # Si ya se a hecho algun zoom el siguiente zoom se hara en relacion con el zoom anterior.
          
          self.play(self.camera.frame.animate.scale(0.5).move_to(np.array([-3.5,2,0])))
          self.wait(2)
          
          self.play(self.camera.frame.animate.scale(1).move_to(np.array([-3.5,-2,0])))
          self.wait(2)
          
          self.play(self.camera.frame.animate.scale(1).move_to(np.array([3.5,2,0])))
          self.wait(2)
          
          self.play(self.camera.frame.animate.scale(0.5).move_to(np.array([1,2,0])))
          self.wait(2)
          
          self.play(self.camera.frame.animate.scale(8).move_to(np.array([0,0,0])))
          self.wait(2)
                    
animacion = manimZOOMAnimacion1()
animacion.render()