
import streamlit as st

st.set_page_config(
    page_title='Home', 
    page_icon=':house:'
)

st.title('Página home')
st.write('Ejemplo de aplicación de Streamlit para EDA, regresión y clasificación.')

col1, col2, col3 = st.columns(3)

with col1:
    if st.button('Ir a EDAs'):
        st.switch_page('pages/1 📊 EDAs.py')
        
with col2:
    if st.button('Ir a Regresión'):
        st.switch_page('pages/2 🤖 Regresión.py')
        
with col3:
    if st.button('Ir a Clasificación'):
        st.switch_page('pages/3 🤖 Clasificación.py')