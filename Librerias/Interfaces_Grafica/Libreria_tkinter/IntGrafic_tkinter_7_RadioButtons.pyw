from tkinter import *

#---------------------Creacion de ventana--------------------------
raiz = Tk()
#raiz.iconbitmap("C:\\Users\\HP\\OneDrive\\Documentos\\Programacion\\Python\\Interfaces Grafica\\CodePython.ico")
raiz.title("IntGrafic_7_RadioButtons")
raiz.config(bg = "blue")

#---------------Creacion del cuadro de la ventana o widget------------------
frame = Frame(raiz, width = 1200, height = 600)
frame.pack(fill = "none", expand = "True")
frame.config(bg = "black")

#-------------------------Variables Para Botones--------------------------------

VarOpcion = IntVar()

#------------------------Introduccion de texto---------------------------------

Tit = Label(frame, text = "Genero:", fg = "black", bg = "#03f943")
Tit.grid(row = 0, column = 0, padx = 3, pady = 3, columnspan = 2)

etiqueta = Label(frame)
etiqueta.grid(row = 2, column = 1,padx = 3, pady = 3)
etiqueta.config(text = "Elige Una Opcion", bg = "black", fg = "#03f943")
#----------------------Creacion de cuadro de texto-------------------------

#--------------------------Funciones Para Botones-----------------------------

def Imprimir():
     
     #print(VarOpcion.get())
     
     if VarOpcion.get() == 1:
          etiqueta.config(text = "Has elegido Masculino")
          
     elif VarOpcion.get() == 2:
          etiqueta.config(text = "Has elegido Femenino")
          
     else:
          etiqueta.config(text = "Has elegido Otras Opciones")
          
#-----------------------------------Botones------------------------------------

#------------------------------Botones Forma Radio-----------------------------
# Se caracterisan por que solo se puede seleccionar uno a la vez y no mas

BoM = Radiobutton(frame, text = "Maculino", variable = VarOpcion, value = 1, command = Imprimir) #  Crea un boton como una opcion
BoM.grid(row = 1, column = 0, padx = 3, pady = 3)
BoM.config(fg = "blue", bg = "black")

BoF = Radiobutton(frame, text = "Femenino", variable = VarOpcion, value = 2, command = Imprimir) # --variable = "-- guarda la informacion en una variable para boton
BoF.grid(row = 2, column = 0, padx = 3, pady = 3)                                                 # -- value = -- le da valor a la variable
BoF.config(fg = "blue", bg = "black")

BoO = Radiobutton(frame, text = "Otras Opciones", variable = VarOpcion, value = 3, command = Imprimir)
BoO.grid(row = 3, column = 0, padx = 3, pady = 3)
BoO.config(fg = "blue", bg = "black")


raiz.mainloop()