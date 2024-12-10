# FUNDAMENTOS
# Creacion de figuras

import plotly.express as px
import numpy as np

#se define una figura
#funcion px.line crea una grafica con una linea
#px.line(x = lista en x, y = lista en y, titulo de la grafica)
#"x" y "y" puede ser una lista de caracteres y numeros
fig = px.line(x= ["b","c","d"],y =[1,2,3],title = "Figura simple")

#imprimimos la figura, trabaja con diccionarios
print(fig)

#tipo figura
print(type(fig))

#Manda a llamar a la grafica y la muestra
fig.show()

x = np.linspace(-2*np.pi, 2*np.pi, 1001)

fig1 = px.line(x = x, y = np.sin(x), title = "Sin(x)")

fig1.show()