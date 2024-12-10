from tkinter import *

#---------------------Creacion de ventana--------------------------
raiz = Tk()
#raiz.iconbitmap("C:\\Users\\HP\\OneDrive\\Documentos\\Programacion\\Python\\Interfaces Grafica\\CodePython.ico")
raiz.title("IntGrafic_8_CheckButtona")

     #---------------------------------Menu---------------------------------------
     #------------------------Variables Para Barra De Menu-----------------------------------

BarraMenu = Menu(raiz) #Crea una barra para el menu
BarraMenu.configure(bg = "blue")
raiz.config(menu = BarraMenu, width = 300, height = 300) # se define la posicion de la barra de menu

     #----------------------Variables Dentro De La Barra de Menu----------------------
          
          #--- Opcion Archivo En El Menu --------------------
ArchivoMenu = Menu(BarraMenu, tearoff = 0)  # Se crean los elementos de la barra de menu, tearoff = 0 elimina lineas
BarraMenu.add_cascade(label = "Archivo", menu = ArchivoMenu)  # Coloca los elementos en la barra de menu

               #--- Subopciones De Archivo ------------------
ArchivoMenu.add_command(label = "Nuevo") # Crea opciones dentro del elemento
ArchivoMenu.add_command(label = "Guardar")
ArchivoMenu.add_command(label = "Guardar Como")
ArchivoMenu.add_separator()  # Crea una linea entre las opciones
ArchivoMenu.add_command(label = "Cerrar")
ArchivoMenu.add_command(label = "Salir")

          #--- Opcion Edicion En El Menu ----------------------
EdicionMenu = Menu(BarraMenu, tearoff = 0)
BarraMenu.add_cascade(label = "Edicion", menu = EdicionMenu)

               #--- Subopciones De Edicion---------------------
EdicionMenu.add_command(label = "Copiar")
EdicionMenu.add_command(label = "Cortar")
EdicionMenu.add_command(label = "Pegar")

          #--- Opcion Herrramietas En El Menu ----------------------
HerramientasMenu = Menu(BarraMenu, tearoff = 0)
BarraMenu.add_cascade(label = "Herramienta", menu = HerramientasMenu)

               #--- Subopciones de Herramientas
HerramientasMenu.add_command(label = "Reemplazar")

          #--- Opcion Help En El Menu ----------------------
HelpMenu = Menu(BarraMenu, tearoff = 0)
BarraMenu.add_cascade(label = "Help", menu = HelpMenu)

               #--- Subopciones De Help---------------------
HelpMenu.add_command(label = "Licencia")
HelpMenu.add_command(label = "Acerca de...")

#---------------Creacion del cuadro de la ventana o widget------------------
frame = Frame(raiz, width = 600, height = 300)
frame.pack(fill = "none", expand = "True")
frame.config(bg = "blue")

#-------------------------Variables Para Botones--------------------------------

#-------------------------Variables globales-------------------------------------

#------------------------Introduccion de texto---------------------------------

#-------------------------Introduccion de una imagen-------------------

#----------------------Creacion de cuadro de texto-------------------------

#--------------------------Funciones Para Botones-----------------------------

#-----------------------------------Botones------------------------------------

#------------------------------Botones Forma Radio-----------------------------

#-----------------------------Botones De Selecion----------------------------

raiz.mainloop()