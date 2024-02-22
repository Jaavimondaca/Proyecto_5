import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Anuncios de ventas de coches')
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
            fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)

# Botón para construir un gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

# Verificar si se hizo clic en el botón de gráfico de dispersión
if scatter_button:
    # Escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    # Crear un gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="year", y="price", color="fuelType", size="mileage",
                             hover_name="make", title="Gráfico de Dispersión")
    
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)