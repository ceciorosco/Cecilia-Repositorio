import streamlit as st

# API reference de elementos de texto en Streamlit

st.title('Elementos de texto en Streamlit')
st.header('Esto es un encabezado')
st.subheader('Esto es un sub-encabezado')

st.write('Esto es un texto normal, con la función write (**admite formateo**)')
st.text('Esto es un texto normal, con la función text (sin formato)')

st.markdown('''
Este párrafo usa **Markdown** con **negrita** y *cursivas* y enlaces como [este](https://streamlit.io).

Con saltos de línea. 

Otro salto de línea. Estamos usando `st.markdown`.

Lista de cosas:
- Cosa 1
- Cosa 2
- Cosa 3

            ''')
st.caption('Lo anterior ha sido una prueba markdown. Esto es un pie de página o nota al pie.')

st.header('Ejemplos de bloques code para código')

st.code('''
def saludar(name):
    print(f'Hola {name}')
        ''', language='python')

st.code('''
public Record(Long id, String email) {}
        ''', language='java')

st.code('''
pip install streamlit
streamlit run app.py
        ''', language='bash')

st.header('Fórmulas matemáticas con Latex')
st.latex(r"""
y = \phi\biggl(\sum_{i=1}^{n} w_i x_i + b\biggr)
""")

st.header('Imprimir help')

# aquí le pasamos cualquier método o clase de la que queramos
# ver la ayuda
st.help(st.write) 
st.write("Hello, *World!* :sunglasses:")

st.header('Imprimir código HTML')

st.html("""
<p><span style='text-decoration: line-through double red;'>Oops</span>!</p>
<p><span style='color:green;'>Oops</span>!</p>
"""
)

st.markdown(
    "<p><span style='text-decoration: line-through double red;'>Oops</span>!</p>",
    unsafe_allow_html=True
)

st.header('Ejemplo de componente echo')

def get_user_name():
    return 'John'

with st.echo():
    # Everything inside this block will be both printed to the screen
    # and executed.

    def get_punctuation():
        return '!!!'

    greeting = "Hi there, "
    value = get_user_name()
    punctuation = get_punctuation()

    st.write(greeting, value, punctuation)

# And now we're back to _not_ printing to the screen
foo = 'bar'
st.write('Done!')

st.header('Conclusión')

st.write('''
Usaremos `st.write` porque es el más flexible y admite tanto
texto normal, fórmulas Latex: $y = mx + b$ y también
texto en **markdown**.

También encabezados:
- ``st.title``
- ``st.header``
- ``st.subheader``
         ''')