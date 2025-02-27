import streamlit as st
import joblib
import seaborn as sns
import pandas as pd

st.set_page_config(page_title='2-🧬Clasificación', page_icon=':dna:')
st.title('Página 3 - Clasificación')

col1, col2, col3 = st.columns(3)

with col1:
    if st.button('Ir a EDAs'):
        st.switch_page('pages/1.📊EDAs.py')

with col2:
    if st.button('Ir a Regresión'):
        st.switch_page('pages/2-🧩Regresion.py')

with col3:
    if st.button('Volver a inicio'):
        st.switch_page('🏠Home.py')

@st.cache_resource
def load_scikit_model():
    return joblib.load('models/pipeline_clasificacion.joblib')

model = load_scikit_model()


#1. mostrar datos
st.write('Carga de datos (diamonds)')
df = sns.load_dataset('diamonds')
st.table(df.head())

cut_mode = df['cut'].mode()
#2.Formulario para la prediccion
st.header('Introduce los siguientes datos para la predicción:')

with st.form('mi_formulario'):
    carat = st.number_input(
        'Introduce peso (carat):',
        min_value=0.20,
        max_value=5.01,
        value=df['depth'].mode()[0],
        step=0.01
    )
    depth = st.number_input(
        'Introduce profundidad (depth):',
        min_value=43,
        max_value=79,
        value=df['depth'].mode()[0],
        step=0.1
    )
    price = st.number_input(
        'Introduce precio (price):',
        min_value=326.00,
        max_value=18823.00,
        value=df['price'].mode()[0],
        step=1
    )
    table = st.number_input(
        'Introduce mesa (table):',
        min_value=43,
        max_value=95,
        value=df['table'].mode()[0],
        step=1
    )
    x = st.number_input(
        'Introduce largo mm (x):',
        min_value=0.01,
        max_value=10.70,
        value=df['x'].mode()[0],
        step=0.01
    )
    y = st.number_input(
        'Introduce ancho mm (y):',
        min_value=0.01,
        max_value=58.90,
        value=df['y'].mode()[0],
        step=0.01
    )
    z = st.number_input(
        'Introduce profundidad mm (z):',
        min_value=0.01,
        max_value=31.80,
        value=df['z'].mode()[0],
        step=0.01
    )
    color = st.selectbox('Introduce color (color)', ['D', 'E', 'F', 'G', 'H', 'I', 'J'])
    clarity = st.selectbox('Introduce claridad (clarity)', ['SI2', 'SI1', 'VS1', 'VS2', 'VVS2', 'VVS1', 'I1', 'IF'])
    
    boton_enviar = st.form_submit_button('Generar predicción')

    if boton_enviar:
        X_new = pd.DataFrame({
            'carat': [carat],
            'color': [color],
            'clarity': [clarity],
            'depth': [depth],
            'table': [table],
            'price': [price],
            'x':['x'],
            'y':['z'],
            'z':['z']
        })
        prediccion = model.predict(X_new)[0]
        col1, col2 = st.columns(2)
        col1.metric('Corte estimado (prediccion): ', value=f'{prediccion}', delta=f'{cut_mode}')
        col2.metric('Corte promedio: ', value=f'{cut_mode} €')







