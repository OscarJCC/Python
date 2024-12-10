
import numpy as np
import matplotlib.pyplot as plt

print("""
| x | y |
|---|---|
| 1 | 1 |
| 2 | 4 |
| 3 | 2 |
| 4 | 3 |
""")

#Creamos una figura que contenga ejes
fig, ax = plt.subplots(facecolor = "blue")
#Crea la regilla dentro de la grafica
ax.grid(color = "blue")
#Marcan los ejes x y y en la  grafica
ax.axhline(color = "red")
ax.axvline(color = "red")
#Coloca un titulo a la grafica
ax.set_title("Mi primer grafico")
#Manda a llama a los ejes y colocamos listas para crear la grafica
ax.plot([1,2,3,4],[1,4,2,3])
#Coloca un nombre al eje x
ax.set_xlabel("Eje x")
#Coloca un nombre al eje x
ax.set_ylabel("Eje y")
#Abre la grafica
plt.show()

x = np.linspace(0,4,1001)
print(x)
fig, ax = plt.subplots()
ax.grid()
ax.axhline(color = "red")
ax.axvline(color = "red")
ax.set_title(r"$Grafica simple f(x), g(x), h(x)$")
#El -label = "---"- le crea una etiqueta a cada funcion graficada
#si queremos que se escriba como en latex colocamos -label = r"$---$"-
ax.plot(x,x,label=r"$f(x) = x$")
ax.plot(x,x**2,label=r"$f(x) = x^2$")
ax.plot(x,x**3,label=r"$f(x) = x^3$")
ax.set_xlabel("Eje x")
ax.set_ylabel("Eje y")
#Permite colocar texto dentro de la grafica en una posicion en espesifico
#el fontsize nos permite agrandar el texto que se coloca deltro de la grafica
ax.text(2,30,r"$\int_{a} ^{b}$",fontsize = 20)
#Permite colocar la etiquetas de las funciones en la
#el edgecolor marca el margen y fonsize modifica el tamaño de la letra
ax.legend(edgecolor = "red", fontsize = 15)
plt.show()


x = np.linspace(-2*np.pi,2*np.pi,1001)
f = np.sin(x)
g = np.cos(x)
print(x)
fig, ax = plt.subplots()
ax.grid()
ax.axhline(color = "red")
ax.axvline(color = "red")
ax.set_title("Funciones trigonometricas")
ax.plot(x,f,color="purple",label=r"$\sin(x)$")
ax.plot(x,g,color="blue",label=r"$\cos(x)$")
ax.set_xlabel("Eje x")
ax.set_ylabel("Eje y")
#Crea un limite a los ejes desde tales puntos
ax.set_xlim(-2*np.pi,2*np.pi) #ax.set_xlim(min(x),max(x))
ax.set_ylim(-1,1)
ax.legend()
plt.show()