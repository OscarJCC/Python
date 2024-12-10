import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi,2*np.pi,1001)

f = np.sin(x)
g = np.cos(x)

#fig, (ax1,ax2,ax3,ax4)
#Se pueden crear mas de una grafica en la misma figura
#plt.subplots(filas,columas,tamaño de la figura figsize = (ancho,largo))
#y despues indicamos como las que remos colocar 
fig, (ax1,ax2,ax3,ax4,ax5) = plt.subplots(1,5)#, figsize = (15,7.5))

ax1.set_title("Grafica 1")
ax1.plot(x,f)
ax1.grid()

ax2.plot(x,g)
ax2.grid()

ax3.plot(x,x**2)
ax3.grid()

ax4.plot(x,x**3-5)
ax4.grid()

ax5.plot(x,x**4-5)
ax5.grid()


t = np.linspace(-1,1,11)

#Cambia el estilo de la grafica
plt.style.use("dark_background") 
fid, ax =plt.subplots()
#lo que va en comillas es el diseño de linea que se desea
#"b--", "b^", "r--", "bs",marker ="o"
ax.plot(t,np.sin(t),"r--")
ax.grid()
plt.show()

