import matplotlib.pyplot as plt
import numpy as np

# Datos de ejemplo
x = np.linspace(0, 10, 100)
y1, y2, y3 = np.sin(x), np.cos(x), np.tan(x)
y4, y5, y6 = np.exp(-x), np.log1p(x), np.sqrt(x)

# Crear subplots (2 filas, 3 columnas)
fig, axes = plt.subplots(2, 3, figsize=(12, 6))  # Figura con 2x3 subplots

# Graficar en cada subplot
axes[0, 0].plot(x, y1, label='sin(x)', color='blue')
axes[0, 0].set_title('Seno')

axes[0, 1].plot(x, y2, label='cos(x)', color='green')
axes[0, 1].set_title('Coseno')

axes[0, 2].plot(x, y3, label='tan(x)', color='red')
axes[0, 2].set_title('Tangente')

axes[1, 0].plot(x, y4, label='exp(-x)', color='purple')
axes[1, 0].set_title('Exponencial')

axes[1, 1].plot(x, y5, label='log1p(x)', color='orange')
axes[1, 1].set_title('Logaritmo')

axes[1, 2].plot(x, y6, label='sqrt(x)', color='cyan')
axes[1, 2].set_title('Raíz Cuadrada')

# Agregar leyendas y ajustar diseño
for ax in axes.flat:
    ax.legend()
    ax.grid()

plt.tight_layout()  # Ajustar espaciado automáticamente
plt.show()