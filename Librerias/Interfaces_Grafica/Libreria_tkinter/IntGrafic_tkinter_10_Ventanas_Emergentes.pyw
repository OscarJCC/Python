from tkinter import *
from tkinter import messagebox # Crea ventanas de dialogo
from tkinter import filedialog # Abre archivos

#---------------------Creacion de ventana--------------------------
raiz = Tk()
#raiz.iconbitmap("C:\\Users\\HP\\OneDrive\\Documentos\\Programacion\\Python\\Interfaces Grafica\\CodePython.ico")
raiz.title("IntGrafic_8_CheckButtona")

     #---------------------------------Menu---------------------------------------
     
     #----------------------------Funciones para menu-----------------------------

def InfoAcercaDe():
     messagebox.showinfo("Procesador de Oscar", "Procesador de textos version 2022") # Crea el mensaje con (titulo,mensaje) y un simbolo circulara con un (!)

def InfoLicencia():
     messagebox.showwarning("Licencia", "Producto bajo licencia GNU")  # Crea el mensaje con (titulo,mensaje) y un simbolo de triangulo con un (!)
     
def AccionSalir():
     v = messagebox.askquestion("Salir", "¿Deseas salir de la aplicacion?") # Crea un mensaje con un pregunta con respuesta de si o no, regresando un valor "yes", "no"
     if v == "yes":
          raiz.destroy()

     v = messagebox.askokcancel("Salir", "¿Deseas salir de la aplicacion?") # Crea un mensaje con un pregunta con respuesta de ok o cancelar, regresando un boliano
     if v == True:
          raiz.destroy()

def AccionCerrar():
     v = messagebox.askretrycancel("Reintentar", "No es posible cerrar el documento bloqueado")
     if v == False:
          raiz.destroy()
          
def AccionAbrir():
     fichero = filedialog.askopenfilename(title = "Abrir", initialdir = "C:\\Users\\HP\\OneDrive\\Documentos\\Programacion\\Python", filetypes = (("Ficheros de Python","*.py"),("Interface de python","*.pyw"),("Ficehros de texto","*.txt"),("Todas los ficheros","*.*")))      
     print(fichero) 
     #------------------------Variables Para Barra De Menu-----------------------------------

BarraMenu = Menu(raiz)
raiz.config(menu = BarraMenu, width = 300, height = 300)

     #----------------------Variables Dentro De La Barra de Menu----------------------
          
          #--- Opcion Archivo En El Menu --------------------
ArchivoMenu = Menu(BarraMenu, tearoff = 0)
BarraMenu.add_cascade(label = "Archivo", menu = ArchivoMenu)

               #--- Subopciones De Archivo ------------------
ArchivoMenu.add_command(label = "Nuevo")
ArchivoMenu.add_command(label = "Guardar")
ArchivoMenu.add_command(label = "Guardar Como")
ArchivoMenu.add_separator()
ArchivoMenu.add_command(label = "Abrir", command = AccionAbrir)
ArchivoMenu.add_command(label = "Cerrar", command = AccionCerrar)
ArchivoMenu.add_command(label = "Salir", command = AccionSalir)

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
HelpMenu.add_command(label = "Licencia"  , command = InfoLicencia)
HelpMenu.add_command(label = "Acerca de...", command = InfoAcercaDe) # command = "funcion del mensaje" Coloca el mensaje


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