from tkinter import *

#---------------------Creacion de ventana--------------------------
raiz = Tk()
raiz.iconbitmap("C:\\Users\\HP\\OneDrive\\Documentos\\Programacion\\Python\\Interfaces Grafica\\CodePython.ico")
raiz.title("IntGrafic_8_CheckButtona")
raiz.config(bg = "blue")

#---------------Creacion del cuadro de la ventana o widget------------------
frame = Frame(raiz, width = 1200, height = 600)
frame.pack(fill = "none", expand = "True")
frame.config(bg = "black")

#-------------------------Variables Para Botones--------------------------------

Playa = IntVar()

Montana = IntVar()

Turismo = IntVar()

OpEs = "Opcion ....."

#------------------------Introduccion de texto---------------------------------

Tit = Label(frame, text = "Elige Destinos", width = 50, fg = "red", bg = "black")
Tit.grid(row = 1,  padx = 3, pady = 5)

TexOp = Label(frame)
TexOp.grid(row = 5,  padx = 3, pady = 5)
TexOp.config(text = OpEs, fg = "white", bg = "black")

#-------------------------Introduccion de una imagen-------------------

Im = PhotoImage(file = "C:\\Users\\HP\\OneDrive\\Documentos\\Programacion\\Python\\Interfaces Grafica\\Avion.png")
Label(frame, image = Im).grid(row = 0)

#----------------------Creacion de cuadro de texto-------------------------

#--------------------------Funciones Para Botones-----------------------------

def OpViaje():
     
     OpEs = ""
     
     if Playa.get() == 1:
          OpEs += " _Playa_ "
     
     if Montana.get() == 1:
          OpEs += " _Montaña_ "
     
     if Turismo.get() == 1:
          OpEs += " _Turismo Rural_ "
          
     TexOp.config(text = OpEs)

#-----------------------------------Botones------------------------------------

#------------------------------Botones Forma Radio-----------------------------

#-----------------------------Botones De Selecion----------------------------
#Se caracterisa por que se pueden seleccionar mas de uno a la vez

Checkbutton(frame, text = "Playa", variable = Playa , onvalue = 1 , offvalue = 0, command = OpViaje, fg = "blue", bg = "black").grid(row = 2, padx = 3, pady = 3) # onvalue si esta elegido la opcion le da un valor a la variable asignada
                                                                                                                                                                   # offvalue si no esta elegida la opcion le da otro valor a la variable

Checkbutton(frame, text = "Montaña", variable = Montana , onvalue = 1 , offvalue = 0, command = OpViaje, fg = "blue", bg = "black").grid(row = 3, padx = 3, pady = 3)

Checkbutton(frame, text = "Turismo Rural", variable = Turismo, onvalue = 1 , offvalue = 0, command = OpViaje, fg = "blue", bg = "black").grid(row = 4, padx = 3, pady = 3)

raiz.mainloop()