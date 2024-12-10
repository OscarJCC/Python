
import numpy as np
import math 
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#tener una funcion
def f(x):
     return 20+80*np.exp(-7.3e-3*x)

ecuacion = "20+80*exp(-7.3e-3*x)"

x = np.linspace(0,600,61)

#plt.style.use("dark_background")
#Crear una figura con figure()
fig = plt.figure()
#Creamos ejes con gca()
ax = fig.gca()

#Crear funcion que obtenga imagen por imagen, con un interador
def update(i):
     #limpia los ejes cadaves que se coloca una imagen
     ax.clear()
     k = np.linspace(-10,1000,100001)
     g = [0]*100001
     ax.plot(k,g,color="red")
     ax.plot(g,k,color="red")
     #Graficamos x (desde el inicio hasta i) =x[:i] y f(x[:i])
     ax.plot(x[:i],f(x[:i]),"o",color="blue")
     ax.set_title(f"{ecuacion},  t={i*10}s")
     ax.set_xlabel(r"$Tiempo \quad (s)$")
     ax.set_ylabel(r"$Temperatura  \quad (°C)$")
     ax.set_xlim(min(x-10),max(x+10))
     ax.set_ylim(min(f(x)-26),max(f(x-10)))
     ax.grid()

#Creamos la animacion y llamamos el modulo animation y 
#la funcion FuncAnimation(figura de la animacion, funcion que genera los fotogramas, numero de fotogramas a generar, tiempo e el que se muestran los de fotogramas)
ani = animation.FuncAnimation(fig, update,range(len(x)),interval=100)
#Grada la animacion (nombre de la animacion.mp4 o .gif,numero de fotogramas)
ani.save("AnimacionLeyDeEnfriamientoDeNewton.gif", fps = 60)
plt.show()