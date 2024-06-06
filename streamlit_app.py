pip install matplotlib
pip install -r requirements.txt

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Define a function to load and process data
def cargar_y_procesar_datos():
    # Load data from CSV (assuming it's in the same directory)
    data = pd.read_csv('la_liga_data.csv')

    # Group by team and sum goals
    goles_por_equipo = data.groupby('Equipo')['Goles'].sum()

    # Sort by goals from highest to lowest
    goles_por_equipo = goles_por_equipo.sort_values(ascending=False)

    # Return the sorted DataFrame
    return goles_por_equipo
# Set the app title
st.title('Goles por Equipo en La Liga 2023-2024')

# Load and process data
datos_goles = cargar_y_procesar_datos()
# Display data table
st.subheader('Datos de Goles por Equipo')
st.dataframe(datos_goles)

# Create bar chart
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(datos_goles.index, datos_goles.values, color='skyblue')

# Customize the chart
ax.set_xlabel('Equipo')
ax.set_ylabel('Goles Marcados')
ax.set_title('Goles por Equipo en La Liga 2023-2024')
ax.xticks(rotation=45, ha='right')  # Rotate x-axis labels if many teams
plt.tight_layout()

# Display the chart in Streamlit
st.subheader('Gráfico de Goles por Equipo')
st.pyplot(fig)

streamlit run streamlit_app.py

