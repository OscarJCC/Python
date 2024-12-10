import pandas as pd
from matplotlib import pyplot as plt
df = pd.read_csv("C:\\Users\\HP\\Documents\\Programacion\\Python\\Librerias\\Libreria Panda\\Data\\avocado.csv", index_col = 0)

#print(df.head(5)) # Permite ver las primeras 5 filas de los datos

#print(df["region"][:5]) # Permite ver solo una columna de los datos con [:5] vemos solo las 5 primeras filas

chicago = df[df["region"] == "Chicago"] #De los datos estamos eliguiendo solo los que estan en la region de chicago

chicago = chicago.set_index("Date") # Permite cambiar el indice de los datos por alguna columna deseada

chicago = chicago.sort_values(by="Date") # Estamos ordenando los datos por la fecha

print(chicago.head(5))

max_samples = 100

precio = chicago["AveragePrice"][:max_samples]
cantidad = chicago["Total Volume"][:max_samples]

plt.plot(precio,label = "Precio Medio")
#plt.plot(cantidad,label = "Volumen Total")
plt.title("Precio de los aguacates vs tiempo")
plt.xlabel("Fecha")
plt.xticks(rotation=90)
plt.ylabel("Precio en $")
plt.legend()
plt.show()