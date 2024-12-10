
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#tener una funcion
def f(x):
     return np.sqrt(x**2)

x = np.linspace(-10,10,101)

plt.style.use("dark_background")
#Crear una figura con figure()
fig = plt.figure()
#Creamos ejes con gca()
ax = fig.gca()

#Crear funcion que obtenga imagen por imagen, con un interador
def update(i):
     #limpia los ejes cadaves que se coloca una imagen
     ax.clear()
     #Graficamos x (desde el inicio hasta i) =x[:i] y f(x[:i])
     ax.plot(x[:i],f(x[:i]),".")
     ax.set_title(f"Fotograma = {i}")
     ax.set_xlim(min(x),max(x))
     ax.set_ylim(min(f(x)),max(f(x)))
     ax.grid()

#Creamos la animacion y llamamos el modulo animation y 
#la funcion FuncAnimation(figura de la animacion, funcion que genera los fotogramas, numero de fotogramas a generar, tiempo e el que se muestran los de fotogramas)
ani = animation.FuncAnimation(fig, update,range(len(x)),interval=0)
#Grada la animacion (nombre de la animacion.mp4 o .gif,numero de fotogramas)
#ani.save("Animacion.mp4", fps = 20)
plt.show()