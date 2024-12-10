from tkinter import *
from tkinter import messagebox

#---------------------Creacion de ventana--------------------------
raiz = Tk()
#raiz.iconbitmap("C:\\Users\\HP\\OneDrive\\Documentos\\Programacion\\Python\\Interfaces Grafica\\CodePython.ico")
raiz.resizable(False,False)
raiz.title("Calculadora_IntGrafic_Completa")

     #---------------------------------Menu---------------------------------------
     
     #----------------------------Funciones para menu-----------------------------

def InfoAcercaDe():
     messagebox.showinfo("Creador", "Oscar Joel Castro Contreras\n------ Ingeniero Fisico -------")
     
def AccionSalir():
     v = messagebox.askokcancel("Salir", "¿Deseas salir de la aplicacion?")
     if v == True:
          raiz.destroy()

def InfoProducto():
     messagebox.showinfo("Producto", "Calculadora Basica 1")  # Crea el mensaje con (titulo,mensaje) y un simbolo de triangulo con un (!)
     

     #------------------------Variables Para Barra De Menu-----------------------------------

BarraMenu = Menu(raiz, bg = "blue", fg = "#03f943")
raiz.config(menu = BarraMenu)

     #----------------------Variables Dentro De La Barra de Menu----------------------
          
          #--- Opcion Informacion En El Menu ----------------------
InformacionMenu = Menu(BarraMenu, tearoff = 0, background = "black", fg = "#03f943")
BarraMenu.add_cascade(label = "INFORMACION", menu = InformacionMenu)

               #--- Subopciones De Informacion---------------------
InformacionMenu.add_command(label = "Acerca de...", command = InfoAcercaDe)
InformacionMenu.add_command(label = "Producto", command = InfoProducto)
InformacionMenu.add_command(label = "Salir", command = AccionSalir)

#---------------Creacion del cuadro de la ventana o widget------------------
frame = Frame(raiz)
frame.pack(fill = "none", expand = "True")
frame.config(bg = "blue")

#-------------------------Variables Para Botones--------------------------------

NumP = StringVar()

#-------------------------Variables globales-------------------------------------

Op = ""

Resultado = 0

TOp = ""

P = 0

#------------------------Introduccion de texto---------------------------------

#-------------------------Introduccion de una imagen-------------------

#----------------------Creacion de cuadro de texto-------------------------

Pantalla = Entry(frame, textvariable = NumP)
Pantalla.grid(row = 1, column = 1, padx = 0, pady = 0, columnspan = 4)                                                         
Pantalla.config(background = "black", fg = "#03f943", justify = "center")

#--------------------------Funciones Para Botones-----------------------------

def NumPantalla(Num):
     
     global Op # --global-- perMIte utilizar un variable global dentro de la funcion
     global Resultado
     
     print("TnumE",Num,Op,Resultado)
     if  NumP.get() == "ZeroDivisionError":
          NumP.set(Num)
          Op = ""
     elif Op != "":
          NumP.set(Num)
          Op = ""
     else:
          NumP.set(str(NumP.get()) + str(Num))
          
     print("Tnums",Num,Op,Resultado)

def AC():
     global Op,Resultado,P
     
     P = 0
     
     Resultado = 0
     Op = ""
     
     NumP.set(Op)
     
def DEL():
     global Op,Resultado,P
     
     P = 0
     
     Resultado = 0
     Op = ""
     
     NumP.set(Op)
     
def Punto(Num):
     global Op, Resultado,P
     
     print("TnumE",Num,Op,Resultado,P)
     
     if P == 0:
          NumP.set(NumP.get() + Num)
          P = 1
     else:
          NumP.set(NumP.get())
     
     print("Tnums",Num,Op,Resultado,P)
     
def Suma(Num):
     global Op,Resultado,TOp,P
     
     P = 0
     
     print("SumaE",Num,Op,Resultado)
     
     Resultado += float(Num)
     
     Op = "Suma"
     TOp = Op

     NumP.set(float(Resultado))
     
     print("SumaE",Num,Op,Resultado)   
     
def Resta(Num):
     global Op,Resultado,TOp,P
     
     P = 0
     
     print("RestaE",Num,Op,Resultado)
     
     Resultado = float(Num) + Resultado
     
     Op = "Resta"
     TOp = Op

     NumP.set(Resultado)
     
     print("RestaS",Num,Op,Resultado)
     
def Producto(Num):
     global Op,Resultado,TOp,P
     
     P = 0
     
     print("ProductoE",Num,Op,Resultado)
     
     if Resultado == 0:
          Resultado = float(Num)
     else:
          Resultado = float(Num) * Resultado
     
     Op = "Producto"
     TOp = Op

     NumP.set(float(Resultado))
     
     print("ProductoS",Num,Op,Resultado)
     
def Divicion(Num):
     global Op,Resultado,TOp,P
     
     P = 0
     
     print("DivicionE",Num,Op,Resultado)
          
     if Num == 0:
          Resultado = "ZeroDivisionError"
          
     elif Resultado == 0:
          Resultado = float(Num)
          
     else:
          Resultado = Resultado/float(Num)
     
     Op = "Divicion"
     TOp = Op

     NumP.set(float(Resultado))
     
     print("DivicionS",Num,Op,Resultado)
     
def Potencia(Num):
     global Op,Resultado,TOp,P
     
     p = 0
     
     return 0

def Raiz(Num):
     return 0

def Igual(Num):
     global Op,Resultado,TOp,P
     
     P = 0
     
     print("IgualE",Num,Op,Resultado)
     
     if TOp == "Suma":
          Resultado += float(Num)
     elif TOp == "Resta":
          Resultado = Resultado - float(Num)
     elif TOp == "Producto":
          Resultado = Resultado*float(Num)
     elif TOp == "Divicion":
          try:
               Resultado = Resultado/float(Num)
          except ZeroDivisionError:
               Resultado = "ZeroDivisionError"
     
     try:
          NumP.set(float(Resultado))
     except:
           NumP.set(Resultado)

     Resultado = 0
     Op = ""
     
     print("IgualS",Num,Op,Resultado)
     
#-----------------------------------Botones------------------------------------

#-- Fila 2
BotonRaiz = Button(frame, text = "v¯", width = "5", command = Raiz(NumP.get()))
BotonRaiz.grid(row = 2, column = 1, padx = 1, pady = 1)
BotonRaiz.config(fg = "#03f943", bg = "black")

BotonPotencia = Button(frame, text = "x²", width = "5", command = Potencia(NumP.get()))
BotonPotencia.grid(row = 2, column = 2, padx = 1, pady = 1)
BotonPotencia.config(fg = "#03f943", bg = "black")

BotonDEL = Button(frame, text = "DEL", width = "5")
BotonDEL.grid(row = 2, column = 3, padx = 1, pady = 1)
BotonDEL.config(fg = "#03f943", bg = "black")

BotonAC = Button(frame, text = "AC", width = "5", command = lambda:AC())
BotonAC.grid(row = 2, column = 4, padx = 1, pady = 1)
BotonAC.config(fg = "#03f943", bg = "black")

#-- Fila 3
Boton7 = Button(frame, text = "7", width = "5", command = lambda:NumPantalla(7))
Boton7.grid(row = 3, column = 1, padx = 1, pady = 1)
Boton7.config(fg = "#03f943", bg = "black")

Boton8 = Button(frame, text = "8", width = "5", command = lambda:NumPantalla(8))
Boton8.grid(row = 3, column = 2, padx = 1, pady = 1)
Boton8.config(fg = "#03f943", bg = "black")

Boton9 = Button(frame, text = "9", width = "5", command = lambda:NumPantalla(9))
Boton9.grid(row = 3, column = 3, padx = 1, pady = 1)
Boton9.config(fg = "#03f943", bg = "black")

BotonEntre = Button(frame, text = "/", width = "5", command = lambda:Divicion(NumP.get()))
BotonEntre.grid(row = 3, column = 4, padx = 1, pady = 1)
BotonEntre.config(fg = "#03f943", bg = "black")

#-- Fila 4
Boton4 = Button(frame, text = "4", width = "5", command = lambda:NumPantalla(4))
Boton4.grid(row = 4, column = 1, padx = 1, pady = 1)
Boton4.config(fg = "#03f943", bg = "black")

Boton5 = Button(frame, text = "5", width = "5", command = lambda:NumPantalla(5))
Boton5.grid(row = 4, column = 2, padx = 1, pady = 1)
Boton5.config(fg = "#03f943", bg = "black")

Boton6 = Button(frame, text = "6", width = "5", command = lambda:NumPantalla(6))
Boton6.grid(row = 4, column = 3, padx = 1, pady = 1)
Boton6.config(fg = "#03f943", bg = "black")

BotonPor = Button(frame, text ="x", width = "5", command = lambda:Producto(NumP.get()))
BotonPor.grid(row = 4, column = 4, padx = 1, pady = 1)
BotonPor.config(fg = "#03f943", bg = "black")


#-- Fila 5
Boton1 = Button(frame, text = "1", width = "5", command = lambda:NumPantalla(1))
Boton1.grid(row = 5, column = 1, padx = 1, pady = 1)
Boton1.config(fg = "#03f943", bg = "black")

Boton2 = Button(frame, text = "2", width = "5", command = lambda:NumPantalla(2))
Boton2.grid(row = 5, column = 2, padx = 1, pady = 1)
Boton2.config(fg = "#03f943", bg = "black")

Boton3 = Button(frame, text = "3", width = "5", command = lambda:NumPantalla(3))
Boton3.grid(row = 5, column = 3, padx = 1, pady = 1)
Boton3.config(fg = "#03f943", bg = "black")

BotonMenos = Button(frame, text ="-", width = "5", command = lambda:Resta(NumP.get()))
BotonMenos.grid(row = 5, column = 4, padx = 1, pady = 1)
BotonMenos.config(fg = "#03f943", bg = "black")

#-- Fila 6
BotonPunto = Button(frame, text = ".", width = "5", command = lambda:Punto("."))
BotonPunto.grid(row = 6, column = 1, padx = 1, pady = 1)
BotonPunto.config(fg = "#03f943", bg = "black")

Boton0 = Button(frame, text = "0", width = "5", command = lambda:NumPantalla(0))
Boton0.grid(row = 6, column = 2, padx = 1, pady = 1)
Boton0.config(fg = "#03f943", bg = "black")

BotonIgual = Button(frame, text = "=", width = "5", command = lambda:Igual(NumP.get()))
BotonIgual.grid(row = 6, column = 3, padx = 1, pady = 1)
BotonIgual.config(fg = "#03f943", bg = "black")

BotonMas = Button(frame, text ="+", width = "5", command = lambda:Suma(NumP.get()))
BotonMas.grid(row = 6, column = 4, padx = 1, pady = 1)
BotonMas.config(fg = "#03f943", bg = "black")

#------------------------------Botones Forma Radio-----------------------------

#-----------------------------Botones De Selecion----------------------------

raiz.mainloop()