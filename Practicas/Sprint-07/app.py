import pandas as pd
import plotly.graph_objects as go
import streamlit as st


# Título de la app
st.header('Análisis de anuncios de vehículos')

# Cargar datos
car_data = pd.read_csv('DB/vehicles_us.csv')

# Checkboxes
show_hist = st.checkbox('Mostrar histograma del odómetro')
show_scatter = st.checkbox('Mostrar diagrama de dispersión (precio vs odómetro)')

# Histograma
if show_hist:
    st.write('Distribución del kilometraje de los vehículos')

    fig_hist = go.Figure(
        data=[go.Histogram(x=car_data['odometer'])]
    )

    fig_hist.update_layout(
        title='Distribución del Odómetro',
        xaxis_title='Kilometraje',
        yaxis_title='Frecuencia'
    )

    st.plotly_chart(fig_hist, use_container_width=True)

# Diagrama de dispersión
if show_scatter:
    st.write('Relación entre precio y kilometraje')

    fig_scatter = go.Figure(
        data=[
            go.Scatter(
                x=car_data['odometer'],
                y=car_data['price'],
                mode='markers'
            )
        ]
    )

    fig_scatter.update_layout(
        title='Precio vs Odómetro',
        xaxis_title='Kilometraje',
        yaxis_title='Precio'
    )

    st.plotly_chart(fig_scatter, use_container_width=True)