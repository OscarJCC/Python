from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

raiz = Tk()

def InfoAdi():
     return messagebox.showinfo("Programa de Oscar", "Programa 2022")

def InfoLi():
     return messagebox.showerror("Licencia", "De 14/09/2021 a 15/09/2022")

def salirapp():
     valor = messagebox.askquestion("Salir","Estas seguro?")
     if valor == "yes":
          raiz.destroy()
     
def cerrardoc():
     valor = messagebox.askretrycancel("Reintentar", "No es posible cerrar")
     if valor == False:
          raiz.destroy

def abreachi():
     archivo = filedialog.askopenfilename(title = "Abrir", initialdir = "/", filetypes = (("Fichero de texto","*.txt"),("Fichero de python","*.py")))
     return print(archivo)
     
raiz.title("Creacion_menu")
raiz.iconbitmap("C:\\Users\\HP\\OneDrive\\Escritorio\\Python\\Interfaz Grafica\\CodePython.ico")
barraMenu = Menu(raiz)
raiz.config(menu = barraMenu, width = 300, height = 300, bg = "black")

archivomenu = Menu(barraMenu, tearoff = 0)
archivomenu.add_command(label = "Nuevo")
archivomenu.add_command(label = "Guardar")
archivomenu.add_command(label = "Guardar como")
archivomenu.add_separator()
archivomenu.add_command(label = "Abrir", command = abreachi)
archivomenu.add_command(label = "Cerrar", command = cerrardoc)
archivomenu.add_command(label = "Salir", command = salirapp)

edicionmenu = Menu(barraMenu, tearoff = 0)
edicionmenu.add_command(label = "Copiar")
edicionmenu.add_command(label = "Cortar")
edicionmenu.add_command(label = "Pegar")

herramientamenu = Menu(barraMenu, tearoff = 0)
herramientamenu.add_command(label = "Reemplazar")

ayudamenu = Menu(barraMenu, tearoff = 0)
ayudamenu.add_command(label = "Licencia", command = InfoLi)
ayudamenu.add_command(label = "Acerca de ......", command = InfoAdi)
barraMenu.add_cascade(label = "Archivo", menu = archivomenu)
barraMenu.add_cascade(label = "Edicion", menu = edicionmenu)
barraMenu.add_cascade(label = "Herramiento", menu = herramientamenu )
barraMenu.add_cascade(label = "Ayuda", menu = ayudamenu)

frame = Frame(raiz, width = 800, height = 400)
frame.pack(fill = "both", expand = "True")
frame.config(bg = "black")

nombre = StringVar()

apellido = StringVar()

edad = IntVar()

dia = IntVar()

contra = StringVar()

def funcionboton1():
     return nombre.set("Oscar")

def funcionboton2():
     return apellido.set("Catro")

def funcionboton3():
     return edad.set(18)

def funcionboton4():
     return dia.set(30)

def funcionboton5():
     return contra.set("contraseña")

cuanombre = Entry(frame, textvariable = nombre)
cuanombre.grid(row = 0, column = 1, padx = 50, pady = 10)
cuanombre.config(fg = "blue", justify = "center")

cuaapellido = Entry(frame, textvariable = apellido)
cuaapellido.grid(row = 1, column = 1, padx = 50, pady = 10)
cuaapellido.config(fg = "blue", justify = "center")

cuaEdad = Entry(frame, textvariable = edad)
cuaEdad.grid(row = 2, column = 1, padx = 50, pady = 10)
cuaEdad.config(fg = "blue", justify = "center")

cuaDia = Entry(frame, textvariable = dia)
cuaDia.grid(row = 3, column = 1, padx = 50, pady = 10)
cuaDia.config(fg = "red", justify = "center")

cuapass = Entry(frame, textvariable = contra)
cuapass.grid(row =4, column = 1, padx = 50, pady = 10)
cuapass.config(fg = "blue", justify = "center", show = "*")

cuacomentario = Text(frame, width = 20, height = 5)
cuacomentario.grid(row = 5, column = 1, padx = 50, pady = 10)
scrollVertical = Scrollbar(frame, command = cuacomentario.yview)
scrollVertical.grid(row = 5, column = 2, sticky = "nsew")
cuacomentario.config(yscrollcommand = scrollVertical.set)

nombrelabel = Label(frame, text = "Nombre: ")
nombrelabel.grid(row = 0, column = 0, sticky = "e", padx = 50, pady = 10)

apellidolabel = Label(frame, text = "Apellido: ")
apellidolabel.grid(row = 1, column = 0, sticky = "e", padx = 50, pady = 10)

Edadlabel = Label(frame, text = "Edad: ")
Edadlabel.grid(row = 2, column = 0, sticky = "e", padx = 50, pady = 10)

Dialabel = Label(frame, text = "Dia: ")
Dialabel.grid(row = 3, column = 0, sticky = "e", padx = 50, pady = 10)

passlabel = Label(frame, text = "Password: ")
passlabel.grid(row = 4, column = 0, sticky = "e", padx = 50, pady = 10)

comenlabel = Label(frame, text = "Comentario: ")
comenlabel.grid(row = 5, column = 0, sticky = "e", padx = 50, pady = 10)

boton1 = Button(raiz, text = "Nombre", command = funcionboton1)
boton1.pack(fill = "both", expand = "True") # Coloca el boton en la raiz

boton2 = Button(raiz, text = "Apellido", command = funcionboton2)
boton2.pack(fill = "both", expand = "True")

boton3 = Button(raiz, text = "Edad", command = funcionboton3)
boton3.pack(fill = "both", expand = "True")

boton4 = Button(raiz, text = "Dia", command = funcionboton4)
boton4.pack(fill = "both", expand = "True")

boton5 = Button(raiz, text = "Password", command = funcionboton5)
boton5.pack(fill = "both", expand = "True")

raiz.mainloop()