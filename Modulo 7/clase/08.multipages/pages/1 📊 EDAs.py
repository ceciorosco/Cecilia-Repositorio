
import streamlit as st

st.set_page_config(
    page_title='EDAs', 
    page_icon=':bar_chart:'
)

st.title('Página 1 - EDAs')

if st.button('Volver a inicio'): # opcional poder volver a inicio
    st.switch_page('Home.py')
        
st.header('1. Carga de datos')

st.header('2. Gráficos univariantes')

st.header('3. Gráficos bivariantes')

st.header('4. Gráficos multivariantes')