from tkinter import *

#---------------------Creacion de ventana--------------------------
raiz = Tk()
raiz.iconbitmap("C:\\Users\\HP\\OneDrive\\Documentos\\Programacion\\Python\\Interfaces Grafica\\CodePython.ico")
raiz.title("IntGrafic_3_Texto")

#---------------Creacion del cuadro de la ventana o widget------------------
frame = Frame(raiz, width = 1210, height = 600)
frame.pack(fill = "none", expand = "True")
frame.config(bg = "black")

#--------------------------Introduccion de texto------------------
label = Label(frame, text = "Label: Sintaxis", fg = "white", font = ("Comic sans MS",20), bg = "black").place(x = 500, y = 0) # Creamos el texto y place Indica ubicacion del texto al texto
                                        # fg = "Color letra"
                                        # font = ("Tipo letra", tamaño)
                                        # bg = "color fondo"
label1 = Label(frame, text = "variableLabel = Label(Contenedor, opciones)", fg = "red", font = ("Comic sans MS",12), bg = "black").place(x = 450, y = 50)


#-------------------------Introduccion de una imagen--------------
imagen = PhotoImage(file = "C:\\Users\\HP\OneDrive\\Documentos\\Programacion\\Python\\Interfaces Grafica\\CuadroOpcionesLabel.png") # Guarda una imagen en una variable
Label(frame, image = imagen).place(x = 10, y = 75)# Coloca imagen en un texto

raiz.mainloop()