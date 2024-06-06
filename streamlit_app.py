import pandas as pd
import matplotlib.pyplot as plt

# Suponiendo que tu conjunto de datos de La Liga se llama 'la_liga_data.csv'
# Cargar los datos en un DataFrame de Pandas
df_la_liga = pd.read_csv('la_liga_data.csv')

# Agrupar datos por 'Equipo' y sumar goles
goles_por_equipo = df_la_liga.groupby('Equipo')['Goles'].sum()

# Crear el gráfico de barras
plt.figure(figsize=(10, 6))  # Ajustar el tamaño del gráfico si es necesario
plt.bar(goles_por_equipo.index, goles_por_equipo.values, color='skyblue')

# Personalizar el gráfico
plt.xlabel('Equipo')
plt.ylabel('Goles Marcados')
plt.title('Goles por Equipo en La Liga 2023-2024')
plt.xticks(rotation=45, ha='right')  # Rotar etiquetas del eje X si hay muchos equipos
plt.tight_layout()

# Mostrar el gráfico
plt.show()

