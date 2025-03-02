import streamlit as st
import joblib
import seaborn as sns
import pandas as pd

st.set_page_config(page_title='3-🧬Clasificación', page_icon=':dna:')
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
        value=df['carat'].mean(),
        min_value=0.20,
        max_value=5.01,
        step=0.01
    )
    color = st.selectbox('Introduce color (color)', df['color'].unique().tolist())
    
    clarity = st.selectbox('Introduce claridad (clarity)', df['clarity'].unique().tolist())
    
    depth = st.number_input(
        'Introduce profundidad (depth):',
        value=df['depth'].mean(),
        min_value=df['depth'].min(), 
        max_value=df['depth'].max(),
        step=0.05
    )
        
    table = st.number_input(
        'Introduce mesa (table):',
        value=df['table'].mean(),
        min_value=df['table'].min(), 
        max_value=df['table'].max(),
        step=0.01
    )
    
    price = st.number_input(
        'Introduce precio (price):',
        value=int(df['price'].mode()),
        min_value=df['price'].min(), 
        max_value=df['price'].max(),
        step=1
    )
    
    x = st.number_input(
        'Introduce largo mm (x):',
        value=df['x'].mean(),
        min_value=df['x'].min(), 
        max_value=df['x'].max(),
        step=0.01
    )
    
    y = st.number_input(
        'Introduce ancho mm (y):',
        value=df['y'].mean(),
        min_value=df['y'].min(), 
        max_value=df['y'].max(),
        step=0.01
    )
    
    z = st.number_input(
        'Introduce profundidad mm (z):',
        value=df['z'].mean(),
        min_value=df['z'].min(),
        max_value=df['z'].max(),
        step=0.01
    )
     
    boton_enviar = st.form_submit_button('Generar predicción')

    if boton_enviar:
        X_new = pd.DataFrame({
            'carat': [carat],
            'color': [color],
            'clarity': [clarity],
            'depth': [depth],
            'table': [table],
            'price': [price],
            'x':[x],
            'y':[z],
            'z':[z],
        })
        prediccion = model.predict(X_new)
        proba = model.predict_proba(X_new).max() * 100

        # Convertir el valor numérico a etiqueta usando el diccionario
        cut_dic = {0: 'Fair',
           1: 'Good',
           2: 'Ideal',
           3: 'Premium',
           4: 'Very good'}
        
        corte_estimado = cut_dic[prediccion[0]]

        col1, col2 = st.columns(2)
        col1.metric('Corte estimado (prediccion): ', value=corte_estimado)
        col2.metric('Corte promedio: ', value=f'{proba:.2f} %')

