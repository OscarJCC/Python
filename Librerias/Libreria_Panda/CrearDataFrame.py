import pandas as pd

# Metodo 1: Lista de listas
print("Metodo 1: Lista de listas")

c = ["Marca","Precio","Disponibilidad"]

carA = ["Mercedez","10e3",True]
carB = ["BMW","20e3",False]

df1 = pd.DataFrame([carA,carB],columns = c)

print(df1)

# Metodo 2: Usando zip
print("\nMetodo 2: Usando zip")

marcas = ["Audi","Mercedez","BMW","Mercedez"]
precio = [20e3,30e3,40e3,25e3]
disponibilidad = [True,False,False,True]

df2 = pd.DataFrame(list(zip(marcas,precio,disponibilidad)), columns = c)

print(df2)

# Metodo 3: Usando un diccionario
print("\nMetodo 3: Usando un diccionario")

diccionario = {
     "marcas": marcas,
     "precios": precio,
     "disponibilidad": disponibilidad
}

df3 = pd.DataFrame(diccionario)

print(df3)