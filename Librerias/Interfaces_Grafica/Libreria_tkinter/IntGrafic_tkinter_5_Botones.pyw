from tkinter import *

#---------------------Creacion de ventana--------------------------
raiz = Tk()
#raiz.iconbitmap("C:\\Users\\HP\\OneDrive\\Documentos\\Programacion\\Python\\Interfaces Grafica\\CodePython.ico")
raiz.title("IntGrafic_5_Botones")
raiz.config(bg = "orange")

#---------------Creacion del cuadro de la ventana o widget------------------
frame = Frame(raiz, width = 1200, height = 600)
frame.pack(fill = "none", expand = "True")
frame.config(bg = "black")

#------------------------Variables Para Boton--------------------------------

MiNombre = StringVar() # StringVar define de que tipo es la variable que usara el un boton

MiApellido = StringVar()

MiEdad = IntVar()

MiPassword = StringVar()

MiDireccion = StringVar()

MiComentario = StringVar()

#--------------------------Introduccion de texto------------------
Nombre = Label(frame, text = "Nombre:", fg = "white", bg = "black")
Nombre.grid(row = 0, column = 0, sticky = "e", padx = 50, pady = 10)

Apellido = Label(frame, text = "Apellido:", fg = "white", bg = "black")
Apellido.grid(row = 1, column = 0, sticky = "e", padx = 50, pady = 10)

Edad = Label(frame, text = "Edad:", fg = "white", bg = "black")
Edad.grid(row = 2, column = 0, sticky = "e", padx = 50, pady = 10)

Password = Label(frame, text = "Password:", fg = "white", bg = "black")
Password.grid(row = 3, column = 0, sticky = "e", padx = 50, pady = 10)

Direccion = Label(frame, text = "Direccion:", fg = "white", bg = "black")
Direccion.grid(row = 4, column = 0, sticky = "e", padx = 50, pady = 10)

Comentarios = Label(frame, text = "Comentarios:", fg = "white", bg = "black")
Comentarios.grid(row = 5, column = 0, sticky = "e", padx = 50, pady = 10)

#------------------Creacion de cuadro de texto-------------------------
CuadroNombre = Entry(frame, textvariable = MiNombre)# textvariable asocia la variable a el cuadro de texto
CuadroNombre.grid(row = 0, column = 1, padx = 50, pady = 10)
CuadroNombre.config(fg = "blue", justify = "center") 

CuadroApellido = Entry(frame, textvariable = MiApellido)
CuadroApellido.grid(row = 1, column = 1, padx = 50, pady = 10)
CuadroApellido.config(fg = "green", justify = "right")

CuadroEdad = Entry(frame, textvariable = MiEdad)
CuadroEdad.grid(row = 2, column = 1, padx = 50, pady = 10)
CuadroEdad.config(fg = "orange", justify = "left")

CuadroPassword = Entry(frame, textvariable = MiPassword)
CuadroPassword.grid(row = 3, column = 1, padx = 50, pady = 10)
CuadroPassword.config(justify = "center", show = "*")
                                                       
CuadroDireccion = Text(frame, width = 20, height = 5)
CuadroDireccion.grid(row = 4, column = 1, padx = 50, pady = 10)

CuadroComentario = Text(frame, width = 20, height = 5)
CuadroComentario.grid(row = 5, column = 1, padx = 50, pady = 10)
scrollVertical = Scrollbar(frame, command = CuadroComentario.yview)
scrollVertical.grid(row = 5, column = 2, sticky = "nsew")
CuadroComentario.config(yscrollcommand = scrollVertical.set)

#---------------------------Funciones Para Boton-----------------------------
def CodigoBoton():
     
     MiNombre.set("Oscar")  # el .set es para establecer un valor de la variable i mostrarlo en el cuadro de texto
                            # y para obtener informacion del cuadro de texto seria .get

     MiApellido.set("Castro")
     
     MiEdad.set(19)
     
     MiPassword.set(302002)

#-----------------------------------Botones------------------------------------
BotonEnvio = Button(raiz, text = "Envio", command = CodigoBoton) #  Crea un boton -- command-- Permite asignarle una funcion al boton
BotonEnvio.pack() # Metodo --.pack-- Empaquetamos el boton y definir la ubicacion dentro de donde se empaqueto
BotonEnvio.config(fg = "white", bg = "black") # Permite varias configuraciones para el boton

raiz.mainloop()