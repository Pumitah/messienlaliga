import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Definir la función para cargar y procesar datos
def cargar_y_procesar_datos():
    # Cargar datos desde CSV (asumiendo que está en el mismo directorio)
    data = pd.read_csv('la_liga_data.csv')

    # Agrupar por equipo y sumar goles
    goles_por_equipo = data.groupby('Equipo')['Goles'].sum()

    # Ordenar por goles de mayor a menor
    goles_por_equipo = goles_por_equipo.sort_values(ascending=False)

    # Devolver el DataFrame ordenado
    return goles_por_equipo

# Establecer el título de la aplicación
st.title('Goles por Equipo en La Liga 2023-2024')

# Cargar y procesar datos
datos_goles = cargar_y_procesar_datos()

# Mostrar la tabla de datos
st.subheader('Datos de Goles por Equipo')
st.dataframe(datos_goles)

# Crear gráfico de barras
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(datos_goles.index, datos_goles.values, color='skyblue')

# Personalizar el gráfico
ax.set_xlabel('Equipo')
ax.set_ylabel('Goles Marcados')
ax.set_title('Goles por Equipo en La Liga 2023-2024')
ax.xticks(rotation=45, ha='right')  # Rotar etiquetas del eje X si hay muchos equipos
plt.tight_layout()

# Mostrar el gráfico en Streamlit
st.subheader('Gráfico de Goles por Equipo')
st.pyplot(fig)

# Nota: Reemplaza 'la_liga_data.csv' con el nombre real de tu archivo CSV
