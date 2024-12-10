import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

def f(x,A,F):
     y = A*np.sin(F*2*np.pi*x)
     return y

x = np.linspace(0,1,1000)

A = 10
F = 1

plt.style.use("dark_background")
fig, ax1 = plt.subplots(dpi = 110, figsize = (12.3,6.1), facecolor = "blue")
ax1.set_xlabel(r"$t(s)$")
ax1.set_ylabel("$v_x(t)$")
ax1.grid(color = "turquoise")
ax1.axhline(color = "red")
ax1.axvline(color = "red")
lv, =  ax1.plot(x,f(x,A,F), color = "yellow", lw = 2)


def Actualiza(val):
     lv.set_ydata(f(x,Amplitud.val,Frecuencia.val))
     fig.canvas.draw_idle()
     
# Grafica para colocar el slider
ax2 = plt.axes([.92,.225,.02,.65]) #[Posicion desde izquierda, Posicion desde abajo, Ancho del eje en porcentaje, Alto del eje]

Amplitud = Slider(
     ax = ax2, #En que axes se va ubicar el slider
     label = "A", #Nombre del slider
     valmin = 1, # Valor minimo del slider
     valmax = 10, # Valor maximo del slider
     valinit = 10, # Valor inicial del slider
     valstep = 1, # Tamaño de paso con el que van a cambiar los valores
     orientation = "vertical", # Orientacion del slider
     color = "yellow"
     )

def ActualizaA(valor):
     A = Amplitud.val # Toma el valor que tiene el slider

ax3 = plt.axes([.95,.225,.02,.65]) #[Posicion desde izquierda, Posicion desde abajo, Ancho del eje en porcentaje, Alto del eje]

Frecuencia = Slider(
     ax = ax3, #En que axes se va ubicar el slider
     label = "F", #Nombre del slider
     valmin = 1, # Valor minimo del slider
     valmax = 60, # Valor maximo del slider
     valinit = 1, # Valor inicial del slider
     valstep = 1, # Tamaño de paso con el que van a cambiar los valores
     orientation = "vertical", # Orientacion del slider
     color = "yellow"
     )

def ActualizaF(valor):
     F = Frecuencia.val # Toma el valor que tiene el slider

Amplitud.on_changed(Actualiza) # Si movemos el slider A0 esto nos ayuda a cambiar dentro de una funcion el valor de A0
Frecuencia.on_changed(Actualiza) # Si movemos el slider A0 esto nos ayuda a cambiar dentro de una funcion el valor de A0

#Grafica para colocar el boton
ax4 = plt.axes([.92,.125,.05,.05])

B0 = Button(
     ax = ax4, #En que axes se va ubicar el boton
     label = "Reset", #Nombre del boton
     color = "black"
)
def reset(accion):
     Amplitud.reset() # Reinicia el valor del slider
     Frecuencia.reset()

B0.on_clicked(reset) # Si pulsamos el boton B0 esto nos ayuda a entrar en una funcion

plt.show()