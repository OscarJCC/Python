# PRIMERAS GRAFICAS
# Graficas 2D

import plotly.graph_objects as go
import numpy as np

#Definimos un diccionario para la grafica
Datos = {
     "data" : [{"type" : "scatter", "x" : [1,2,3], "y" : [4,5,6]}],
     "layout" : {"title" : "MI PRIMERA GRAFICA CON PLOTLY"}
}
#Definimos una figura
#go.figure(Diccionario creado) permite crear una figura
#con el diccionario anterior
fig = go.Figure(Datos)
fig.show()

del fig #Borra lo que ya esta guardado en fig

x = np.linspace(-2*np.pi,2*np.pi,1001)

fig = go.Figure()
#Agrega un traso a la figura y solo se deve usar de un tipo de traso
#go.Scatter(lista de x, lista de y, nombre de la linea) traso de linea
fig.add_trace(go.Scatter(x = x, y = np.sin(x), name = "Sin(x)"))
fig.add_trace(go.Scatter(x = x, y = np.cos(x), name = "Cos(x)"))

fig.show()

#del fig #Borra lo que ya esta guardado en fig

#O podemos crear una lista con todos los trasos que queremos y agragarlos a la figura guntos
#trasos = [go.Scatter(x = x, y = np.sin(x), name = "Sin(x)"),go.Scatter(x = x, y = np.cos(x), name = "Cos(x)")]
#fig.add_traces(trasos)

#fig.show()

#con esto se pueden agregar muchas cosas como
#El titulo de la grafica con title = "---"
#Delimitar los ejes con yaxis_range o xaxis_range = [limite inferior, limite superior]
#Titulo a la etiquetas con legend_title = "---"
#Titulo de los ejes con xaxis_title o yaxis_title = "---"
fig.update_layout(title = "FUNCIONES TRIGONOMETRICAS", yaxis_range = [-1,1],
                  legend_title = "Etiquetas", xaxis_title = "Eje x",
                  yaxis_title = "Eje y",)
fig.show()