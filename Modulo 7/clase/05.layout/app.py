
import streamlit as st

st.set_page_config(
    page_title="Título aplicación Layout",
    page_icon="🧊", # favicon
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

# Se puede agregar archivos statics de css externos
# with open('styles.css') as f:
#     st.html(f'<style>{f.read()}</style>')

st.title('Elementos para layout y estructura')

st.header('1. Columnas')
# se puede cambiar la alineación del contenido:
# col1, col2, col3 = st.columns(3, vertical_alignment='bottom')
# col1, col2, col3 = st.columns(3, vertical_alignment='top')
col1, col2, col3 = st.columns(3, vertical_alignment='center')

with col1:
    # st.write('Contenido de la primera columna')
    st.image('https://placehold.co/100x250', caption='Imagen 100x200')

with col2:
    # st.write('Contenido de la segunda columna')
    st.image('https://placehold.co/100x300', caption='Imagen 100x200')
    
with col3:
    # st.write('Contenido de la tercera columna')
    st.image('https://placehold.co/100x200', caption='Imagen 100x200')
    

# tabs
st.header('2. tabs')
tab1, tab2, tab3 = st.tabs(['EDA', 'Regresión', 'Clasificación'])

with tab1:
    # si lo ponemos como imagen directa no será responsive a menos que la hagamos en CSS ni tendría border-radius
    # st.html('<img src="https://placehold.co/600x250" style="text-align:center;">')
    # st.write('Contenido de la primera columna')
    st.image('https://placehold.co/600x250', caption='Imagen 600x250')

with tab2:
    # st.write('Contenido de la segunda columna')
    st.image('https://placehold.co/600x300', caption='Imagen 600x300')
    
with tab3:
    # st.write('Contenido de la tercera columna')
    st.image('https://placehold.co/600x200', caption='Imagen 600x200')
    


# expander
st.header('3. expander (acordeón)')

with st.expander('Contenido desplegable'):
    st.write('Esto es un párrafo.')
    st.image('https://placehold.co/600x200', caption='Imagen 600x200')
    
with st.expander('¿Puedo pagar con Bizum?'):
    st.write('Puedes pagar con PayPal, tarjeta, Bizum en euros o rupias.')
    st.write('Puedes pagar con PayPal, tarjeta, Bizum en euros o rupias.')
    
with st.expander('Pregunta 3'):
    st.write('Puedes pagar con PayPal, tarjeta, Bizum en euros o rupias.')
    st.write('Puedes pagar con PayPal, tarjeta, Bizum en euros o rupias.')
    
# container
st.header('4. container')

container1 = st.container(border=True)
container1.write('Esto es un texto')
container1.image('https://placehold.co/600x200', caption='Imagen 600x200')
container1.write('Esto es otro texto')

container2 = st.container(border=True)
container2.write('Esto es un texto')
container2.image('https://placehold.co/600x200', caption='Imagen 600x200')
container2.write('Esto es otro texto')


# sidebar
st.header('5. sidebar')
# nombre = st.sidebar.text_input('Introduce tu nombre')

# if nombre:
#     st.sidebar.success(f'Tu nombre es {nombre}')

menu = ['Pagina 1', 'Pagina 2', 'Pagina 3']
pagina = st.sidebar.selectbox('Seleccionar una página', options=menu)

if pagina == 'Pagina 1':
    st.write('Has seleccionado la página 1')
    
elif pagina == 'Pagina 2':
    st.write('Has seleccionado la página 2')
    
elif pagina == 'Pagina 3':
    st.write('Has seleccionado la página 3')