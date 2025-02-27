import streamlit as st

st.set_page_config(page_title='🏠Inicio', page_icon=':house:')
st.title('Pagina INICIO')
st.write('Aplicación de Streamlit para EDA, Regresión y Clasificación: Diamonds')


col1, col2, col3 = st.columns(3)

with col1:
    if st.button('Ir a EDAs'):
        st.switch_page('pages/1-📊EDAs.py')

with col2:
    if st.button('Ir a Regresión'):
        st.switch_page('pages/2-🧩Regresion.py')

with col3:
    if st.button('Ir a Clasificación'):
        st.switch_page('pages/3-🧬Clasificacion.py')
        
