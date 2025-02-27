import streamlit as st
import seaborn as sns
import requests

# Decorador para cachear el resultado de la función, es decir, cachear el dataframe para evitar recargarlo todo el rato
@st.cache_data
def load_tips_data():
    return sns.load_dataset('tips')

# @st.cache_data
def load_json_data():
    url = 'https://fakestoreapi.com/products/1'
    return requests.get(url).json()

st.title('Streamlit API reference Data elements')

#
# 1. MOSTRAR DATAFRAME
#
st.header('1. DataFrame NO editable de Pandas con st.dataframe')
df = load_tips_data()
st.dataframe(df, use_container_width=True)


#
# 2. DATAFRAME EDITABLE
#
st.header('2. DataFrame editable de Pandas con st.data_editor')
df_edited = st.data_editor(df, use_container_width=True)


#
# 3. COMPROBAR MODIFICACIONES SOBRE DATASET EDITADO
# 
st.header('3. DataFrame NO editable de Pandas con st.dataframe para comprobar datos editados.')
st.write('''
Este método ``st.data_editor`` permite modificar celdas, podemos guardar el dataframe resultante. 
Ejemplo de **dataframe editado** resultante:
''')
st.dataframe(df_edited, use_container_width=True)

#
# 4. TABLAS ESTÁTICAS
#
st.header('4. Tabla estática con st.table')
st.write('Tabla estática sin funcionalidades interactivas.')
st.table(df.head())

#
# 5. JSON
#
st.header('5. Mostrar datos JSON')
st.json(load_json_data())

#
# 6. Metrics
# 
st.header('Métricas')
st.metric('tu rendimiento', value=10, delta=2)
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")