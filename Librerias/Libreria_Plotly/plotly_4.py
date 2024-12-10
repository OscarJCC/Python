# Graficas 3D

import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

#Creamos los valores asignados a "x" y a "y"
x,y = np.linspace(np.pi, np.pi, 101), np.linspace(np.pi, np.pi, 101)

X, Y = np.meshgrid(x,y) #Crea matriz relacionando "x" y "y"

Z = np.sqrt(3 + 2*np.cos(np.sqrt(3)*Y) + 4*np.cos(np.sqrt(3)*Y/2)*np.cos(3*X/2))

fig = go.Figure(data=[go.Surface(z=Z), go.Surface(z=-Z)])

fig.update_layout(title="Estructura de bandas del grafeno", autosize=False,
                  width=500, height=500,
                  margin=dict(l=65, r=50, b=65, t=90))

fig.show()