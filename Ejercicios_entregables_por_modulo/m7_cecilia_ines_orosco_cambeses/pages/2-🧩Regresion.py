import streamlit as st
import joblib
import seaborn as sns
import pandas as pd

st.set_page_config(page_title='2-🧩Regresión', page_icon=':jigsaw:')
st.title('Página 2 - Regresión')

col1, col2, col3 = st.columns(3)

with col1:
    if st.button('Ir a EDAs'):
        st.switch_page('pages/1-📊EDAs.py')    
with col2:
    if st.button('Volver a inicio'):
        st.switch_page('🏠Home.py')

with col3:
    if st.button('Ir a Clasificación'):
        st.switch_page('pages/3-🧬Clasificacion.py')

@st.cache_resource
def load_scikit_model():
    return joblib.load('models/pipeline_regresion.joblib')

model = load_scikit_model()


#1. mostrar datos
st.write('Carga de datos (diamonds)')
df = sns.load_dataset('diamonds')
st.table(df.head())

price_mean = df['price'].mean()
#2.Formulario para la prediccion
st.header('Introduce los siguientes datos para la predicción:')

with st.form('mi_formulario'):
    size = st.number_input(
        'Introduce profundidad (depth):',
        min_value=1,
        max_value=10,
        value=df['depth'].mode()[0],
        step=1
    )
    cut = st.selectbox('Introduce corte (cut)', ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'])
    smoker = st.selectbox('Introduce si es fumador (smoker)', ['Yes', 'No'])
    day = st.selectbox('Introduce día semana (date)', ['Thur', 'Fri', 'Sat', 'Sun'])
    time = st.selectbox('Introduce horario (time)', ['Lunch', 'Dinner'])
    
    boton_enviar = st.form_submit_button('Generar predicción')

    if boton_enviar:
        X_new = pd.DataFrame({
            'total_bill': [total_bill],
            'sex': [sex],
            'smoker': [smoker],
            'day': [day],
            'time': [time],
            'size': [size]
        })
        prediccion = model.predict(X_new)[0]
        delta_value = prediccion - tip_mean
        col1, col2 = st.columns(2)
        col1.metric('Propina estimada (prediccion): ', value=f'{prediccion:.2f} €', delta=f'{delta_value:.2f} €')
        col2.metric('Propina media: ', value=f'{tip_mean:.2f} €')







