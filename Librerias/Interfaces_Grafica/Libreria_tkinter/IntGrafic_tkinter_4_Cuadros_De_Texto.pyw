from tkinter import *

#---------------------Creacion de ventana--------------------------
raiz = Tk()
#raiz.iconbitmap("C:\\Users\\HP\\OneDrive\\Documentos\\Programacion\\Python\\Interfaces Grafica\\CodePython.ico")
raiz.title("IntGrafic_4_Cuadros_de_Texto")

#---------------Creacion del cuadro de la ventana o widget------------------
frame = Frame(raiz, width = 1200, height = 600)
frame.pack(fill = "none", expand = "True")
frame.config(bg = "black")

#--------------------------Introduccion de texto------------------
Nombre = Label(frame, text = "Nombre:", fg = "white", bg = "black")
Nombre.grid(row = 0, column = 0, sticky = "e", padx = 50, pady = 10) #Trabaja el texto como tabla junto con el cuadro de texto
                               # sticky = ("n";"s";"w";"e") ayuda a alinear el texto dentro del --.grip--
                               # --padx-- y --pady-- es la distancia entre un cuadro y lo que tiene dentro por los cuatro lados y esto lo permite controlar por pixeles

Apellido = Label(frame, text = "Apellido:", fg = "white", bg = "black")
Apellido.grid(row = 1, column = 0, sticky = "e", padx = 50, pady = 10)

Edad = Label(frame, text = "Edad:", fg = "white", bg = "black")
Edad.grid(row = 2, column = 0, sticky = "e", padx = 50, pady = 10)

Password = Label(frame, text = "Password:", fg = "white", bg = "black")
Password.grid(row = 3, column = 0, sticky = "e", padx = 50, pady = 10)

Direccion = Label(frame, text = "Direccion:", fg = "white", bg = "black")
Direccion.grid(row = 4, column = 0, sticky = "e", padx = 50, pady = 10)

#------------------Creacion de cuadro de texto-------------------------
CuadroNombre = Entry(frame) # Crea un cuadro donde ingresar texto y lo vincula con el cuadro de la ventana
#CuadroNombre.place(x = 100, y = 100) # define la posicion del cuadro
CuadroNombre.grid(row = 0, column = 1, padx = 50, pady = 10) # lo trabaja como tablas igual que con el texto
CuadroNombre.config(fg = "blue", justify = "center") 
                    # fg = "color" permite cambiar el color de las letras que se escribem
                    # justify = ("left";"right";"center") permite acomodar el cursor

CuadroApellido = Entry(frame)
CuadroApellido.grid(row = 1, column = 1, padx = 50, pady = 10)
CuadroApellido.config(fg = "green", justify = "right")

CuadroEdad = Entry(frame)
CuadroEdad.grid(row = 2, column = 1, padx = 50, pady = 10)
CuadroEdad.config(fg = "yellow", justify = "left")

CuadroPassword = Entry(frame)
CuadroPassword.grid(row = 3, column = 1, padx = 50, pady = 10)
CuadroPassword.config(justify = "center", show = "/") 
                                                       # --show = "/" o "*"-- Pemite ocultar lo que se escribe con cualquier caracter
                                                       
CuadroDireccion = Text(frame, width = 20, height = 5) # Crea el cuadro tipo texto y lo vincula con la cuadro de la ventana
CuadroDireccion.grid(row = 4, column = 1, padx = 50, pady = 10) # Modifica posicion
scrollVertical = Scrollbar(frame, command = CuadroDireccion.yview) # Crea una barra para poder vajar y con 
                                                            # .yview se pone vertical y 
                                                            # .xview se pone horizontal
scrollVertical.grid(row = 4, column = 2, sticky = "nsew") # Modifica donde se coloca la barra y deva estar una columna despues del cuadro de texto
CuadroDireccion.config(yscrollcommand = scrollVertical.set) # Arregla el erro que tiene al posicionar la barra

raiz.mainloop()