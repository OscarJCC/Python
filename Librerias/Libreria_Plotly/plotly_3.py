import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

x = np.linspace(-2,2,1001)

#Subgraficas
#make_subplots(numero de filas, numero de columnas)
#Agregar titulo a cada grafica
#subplot_titles = tupla con los nombre de cada grafica
fig = make_subplots(rows = 1, cols = 2, subplot_titles=("Grafica 1","Grafica 2"))

#mode = "lines" forma de unir los puntos de la funcion
#line_color = "green" darle color a la linea
fig.add_trace(go.Scatter(x = x, y = x**2, name="Funcion cuadratica",
                         mode="lines", line_color="purple"),
              row=1,col=1)

fig.add_trace(go.Bar(x=["Peras","Manzanas","Fresas"], y=[1,2,3], name="Grafica de barras"),
              row=1,col=2)
#Estilos de graficas template = "---"
#plotly
#plotly_white
#plotly_dark
#ggplot2
fig.update_layout(title="Subplots",template="plotly_dark",)

#para agregar titulo a los ejes
fig.update_xaxes(title_text="Eje x", row = 1, col = 1)
fig.update_xaxes(title_text="Eje x", row = 1, col = 2)
fig.update_yaxes(title_text="Eje y", row = 1, col = 1)
fig.update_yaxes(title_text="Eje y", row = 1, col = 2)

fig.show()

#Guarda las grafica en modo html para abrir en navegador
fig.write_html("Prueba.html")
