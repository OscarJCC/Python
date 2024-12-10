from tkinter import *

#---------------------Creacion de ventana--------------------------
raiz = Tk()
raiz.title("IntGrafic_2_Creacion_Frame")
#raiz.iconbitmap("C:\\Users\\HP\\OneDrive\\Documentos\\Programacion\\Python\\Interfaces Grafica\\CodePython.ico")
#raiz.geometry("650x350")
raiz.config(bg = "blue")

# Todo lo que se le aplique al frame en el metodo --.config tambien se puede aplicar a la raiz.

#---------------Creacion del cuadro de la ventana o widget------------------
frame = Frame() # Crea un cuadro
# Metodo --.pack-- Empaquetamos el cuadro en la ventana, y definir la ubicacion dentro de la ventana
frame.pack(side = "top", anchor="center")       # (side = ("left";"right";"top";"bottom"), anchor=("n";"s";"w";"e";"center") el cuadro se coloca en la raiz dependiendo de las opciones para anchor hay (n, ne, e, se, s, sw, w, nw,cente)
#frame.pack(fill = "both", expand = "True")   # (fill = ("x";"y";"none";"both"), expand = ("True";"False")) la ventana se expande con la raiz dependiendo de las opciones

frame.config(bg = "black") # Permite manipular diferentes cosas del cuadro
                           # bg = "color en ingles" -- cambia color del fondo del cuadro
frame.config(width = "650", height = "350")  # Define el tamaño del cuadro (widht = "Ancho", height = "Largo")
#frame.config(relief = "groove") # Coloca borde al cuadro ("groove";"flat";"raised";"ridge";"solid";"sunken") tipos de borde
#frame.config(bd = 40) # Tamaño del borde
#frame.config(cursor = "pirate") # Cambia el cursor dentro del cuadro

raiz.mainloop()