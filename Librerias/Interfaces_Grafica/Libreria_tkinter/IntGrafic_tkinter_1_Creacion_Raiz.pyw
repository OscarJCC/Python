from tkinter import *

def imprimir_informacion(r):
    altura = r.winfo_reqheight()
    anchura = r.winfo_reqwidth()
    altura_pantalla = r.winfo_screenheight()
    anchura_pantalla = r.winfo_screenwidth()
    print(f"Altura: {altura}\nAnchura: {anchura}\nAltura de pantalla: {altura_pantalla}\nAnchura de pantalla: {anchura_pantalla}")

#---------------------Creacion de ventana--------------------------
raiz = Tk() # Crea la ventana
raiz.title("IntGrafic_1_Creacion_Raiz") # Le da un nombre a la ventana
#raiz.resizable(False,False) # Bloque o permite con False y True el agrandamiento de la ventana (ancho, largo)
#raiz.iconbitmap("C:\\Users\\HP\\OneDrive\\Documentos\\Programacion\\Python\\Interfaces Grafica\\CodePython.ico") # Coloca el icono a la ventana escribiendo la direccion del icono

wtotal = raiz.winfo_screenwidth()  # Obtencion del ancho de la pantalla laptop
htotal = raiz.winfo_screenheight() # Obtencion del alto de la pantalla laptop

raiz.geometry(str(wtotal)+"x"+str(htotal)) # Define el tamaño de la ventana ("Ancho x Largo")
raiz.config(bg = "blue") # Permite manipular diferentes cosas de la ventana
                         # bg = "color en ingles" -- cambia color del fondo

imprimir_informacion(raiz)

raiz.mainloop() # Abre o ejecuta la ventana