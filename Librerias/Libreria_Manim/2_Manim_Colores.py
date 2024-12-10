from manim import *
import numpy as np

class manimColoresAnimacion1(Scene):
    def construct(self):
        texto1 = Text("Hola, Mundo - PURPLE", color = PURPLE).move_to(3.5*UP) # Le da un color al texto con --color = "NameColor"---
        texto2 = Text("Hola, Mundo - YELLOW", color = YELLOW).move_to(2.5*UP)
        texto3 = Text("Hola, Mundo - BLUE", color = BLUE).move_to(1.5*UP)
        texto4 = Text("Hola, Mundo - GREEN", color = GREEN).move_to(0.5*UP)
        texto5 = Text("Hola, Mundo - GRAY", color = GRAY).move_to(0.5*DOWN)
        texto6 = Text("Hola, Mundo - RED", color = RED).move_to(1.5*DOWN)
        texto7 = Text("Hola, Mundo - ORANGE", color = ORANGE).move_to(2.5*DOWN)
        texto8 = Text("Hola, Mundo - PINK", color = PINK).move_to(3.5*DOWN)
          
        self.add(texto1)
        self.add(texto2)
        self.add(texto3)
        self.add(texto4)
        self.add(texto5)
        self.add(texto6)
        self.add(texto7)
        self.add(texto8)
        
        self.wait(3)
          
class manimColoresAnimacion2(Scene):
    def construct(self):
        color1 = "#0F2C67"
        color2 = "#CD1818"
        color3 = "#F3950D"
        color4 = "#F4E185"
        
        self.camera.background_color = color1 # Con este metodo cambiamos el color del fondo del video
        
        texto1 = Text("Pitagoras", color = color2).move_to(2*UP).scale(2) # --.scale(%)-- Permite Cambiar el tamaño del texto o cualquier otro objeto si tenemos 2 equivale al 200% del tamaño del objeto
        texto2 = Text("Pitagoras").move_to(0.5*UP).scale(1.5).set_color(color3) # Tambien podemos cambiar color con --.set_color("NumeroHexaColor")-- pero solo usa codigo Hexadecimal del color
        texto3 = Text("Pitagoras").move_to(DOWN)
        texto3.set_color(color4)
        texto4 = Text("Pitagoras", color = BLUE).move_to(2*DOWN).scale(0.75)
        texto5 = Text("Pitagoras").move_to(3*DOWN).scale(0.5)
          
        self.add(texto1)
        self.add(texto2)
        self.add(texto3)
        self.add(texto4)
        self.add(texto5)
        
        self.wait(3)

class manimColoresAnimacion3(Scene):
    def construct(self):
        color1 = "#0F2C67"
        color2 = "#CD1818"
        color3 = "#F3950D"
        color4 = "#F4E185"
        
        texto1 = Text("Pitagoras").move_to(2*UP).scale(2).set_color_by_gradient(color1,color2) # Permite hacer un degradado entre los colores del argumento
        texto2 = Text("Pitagoras").move_to(1*UP).scale(2).set_color_by_gradient(color1,color2,color3,color4)
        
        self.play(Write(texto1))
        self.wait(3)
        
        self.play(Write(texto2))
        self.wait(3)

class manimColoresAnimacion4(Scene):
    def construct(self):
        color1 = "#0F2C67"
        color2 = "#CD1818"
        color3 = "#F3950D"
        color4 = "#F4E185"
        
        texto1 = MarkupText(f'Hola <span fgcolor = "{color1}">Mundo</span>',color = color2).move_to(3.5*UP).scale(2) # Con MarkupText permite usar un entorno de html para poder elegir el color de cada letra o palabra
        texto2 = Text("Hola Mundo",t2c = {'[3:6]':color1}).move_to(1*UP).scale(2) #t2c = {'[caracteInicial:caracterFinal]':NameColorHex} Permite hacer lo mismo que en el anterior texto
        texto3 = Text("0123456789",t2c = {'[1:6]':color1}).move_to(1*DOWN).scale(2)
        texto4 = Text("0123456789",t2c = {'[5:-2]':color1}).move_to(3.5*DOWN).scale(2)
        
        self.play(Write(texto1))
        self.wait(3)
        
        self.play(Write(texto2))
        self.wait(3)
        
        self.play(Write(texto3))
        self.wait(3)
        
        self.play(Write(texto4))
        self.wait(3)

animacion = manimColoresAnimacion4()
animacion.render()
