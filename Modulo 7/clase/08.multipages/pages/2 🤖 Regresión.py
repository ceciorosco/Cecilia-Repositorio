import streamlit as st
import joblib
import seaborn as sns
import pandas as pd 

@st.cache_resource
def load_scikit_model():
    return joblib.load('models/pipeline.joblib')

st.set_page_config(
    page_title='Regresión', 
    page_icon=':robot_face:'
)

st.title('Página 2 - Regresión')

model = load_scikit_model()

st.write('Ejemplo de los datos')
df = sns.load_dataset('tips')
tip_mean = df['tip'].mean() # propina media de todo el dataset

st.table(df.head())

# 2. Formulario para predicción
st.header('Introduce datos para la predicción')

with st.form("tips_form"):
    total_bill = st.number_input(
                    'Introduce total cuenta (total_bill)', 
                    min_value=0.0, max_value=100.0, 
                    value=df['total_bill'].mean(), 
                    step=0.1
    )
    size = st.number_input(
        'Introduce número comensales (size)',
        min_value=1, 
        value=df['size'].mode()[0], # opcional poner el valor más habitual
        max_value=10,
        step=1
    )
    sex = st.selectbox('Introduce género (sex)', ['Male', 'Female'])
    smoker = st.selectbox('Introduce si es fumador (smoker)', ['Yes', 'No'])
    day = st.selectbox('Introduce día semana (day)', ['Thur', 'Fri', 'Sat', 'Sun'])
    time = st.selectbox('Introduce horario (time)', ['Lunch', 'Dinner'])

    boton_enviar = st.form_submit_button("Generar predicción")

    if boton_enviar:
        X_new = pd.DataFrame({
            'total_bill': [total_bill],
            'sex': [sex],
            'smoker': [smoker],
            'day': [day],
            'time': [time],
            'size': [size]                        
        })
        prediccion = model.predict(X_new)[0] # esta prediccion se podría guardar en base de datos junto a los datos introducidos
        # st.write(prediccion)
        delta_value = prediccion - tip_mean
        col1, col2 = st.columns(2)
        col1.metric('Propina estimada (predicción)', value=f'{prediccion:.2f} $', delta=f'{delta_value:.2f} $')
        col2.metric('Propina media', value=f'{tip_mean:.2f} $')

    
    
    