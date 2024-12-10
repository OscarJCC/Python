import pandas as pd

file = "http://luis2501.github.io/files/Taller_Python_Avanzado/radiacion.xls"

df = pd.read_excel(file)

print(df)