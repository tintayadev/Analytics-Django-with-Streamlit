import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import altair as alt
import pandas as pd
import requests

swapi_endpoint = 'https://swapi.dev/api/people/1/'
api_url = 'http://127.0.0.1:8000/api/customers/'

# functions
def fetch_data(endpoint):
    respponse = requests.get(endpoint)
    data = respponse.json()
    return data

def send_data(name, gender, age, favorite_number):
    gender_value = "0" if gender == "Female" else "1"
    data = {
        "name": name,
        "gender": gender_value,
        "age": age,
        "favorite_number": favorite_number
    }
    response = requests.post(api_url, json=data)
    return response


st.title("Dashboard de analisis")
# st.write("v.0.01")

# Layout customization
col1, col2 = st.columns(2)

with col1:
    st.header('Columna 1')
    st.write('algun contenido')

    with st.expander('Escoge una opcion'):
        st.write('opcion 1')
        st.write('otra opcion')

with col2:
    # Test chart
    categories = ['A', 'B', 'C', 'D']
    values = np.random.randint(10, 100, size=(4,))

    fig, ax = plt.subplots()

    ax.bar(categories, values, color='blue')
    ax.set_xlabel('categorias')
    ax.set_ylabel('valores')
    ax.set_title('First bar char')

    st.pyplot(fig)

# Session state

if 'counter' not in st.session_state:
    st.session_state.counter = 0

# increment btn
if st.button('increment'):
    st.session_state.counter += 1

st.write(f"Valor del contador: {st.session_state.counter}")

# data from SWAPI API


swapi_data = fetch_data(swapi_endpoint)

st.write('Data del SWAPI API')
st.json(swapi_data)


# Fetch data from our API

data = fetch_data(api_url)

if data:
    df = pd.DataFrame(data)
    st.dataframe(df)

    scatter_chart = alt.Chart(df).mark_circle().encode(
        x = 'age',
        y = 'favorite_number'
    )
    st.altair_chart(scatter_chart, use_container_width=True)

# Form to collect customer data
name = st.text_input("Tu nombre")
gender = st.radio("Selecciona tu genero", ["Male", "Female"] )
age = st.slider("Selecciona tu edad", 1, 100, 18)
fav_number = st.number_input("Ingresa tu nro favorito", step=1)

if st.button("Submit"):
    response = send_data(name, gender, age, fav_number)
    if response.status_code == 201:
        st.success("Nuevo Customer creado")
        st.rerun()
    else:
        st.error("Algo salio mal")
