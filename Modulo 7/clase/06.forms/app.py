import streamlit as st
import seaborn as sns 

st.title("Ejemplo de formulario de Streamlit")

df = sns.load_dataset('tips')

st.header('Ejemplo de botón interactivo')
st.write('Si no se hace clic entonces muestra una tabla con 5 filas, si hace clic muestra todo el dataFrame.')
clicked = st.button('Mostrar dataframe completo', type='primary')
if not clicked:
    st.table(df.head())
else:
    st.dataframe(df, use_container_width=True)

st.header('Formularios')
# Creamos un formulario llamado "mi_formulario"
with st.form("mi_formulario"):
    st.write("Por favor, completa los siguientes campos:")
    
    # Texto de una sola línea
    nombre = st.text_input("Nombre", placeholder='Juancito')
    
    # Texto de varias líneas
    descripcion = st.text_area("Descripción", placeholder='Descripción texto algo largo pero tampoco mucho no te pases.')
    
    # Número (con límites y paso específico)
    edad = st.number_input("Edad", min_value=0, max_value=120, value=25, step=1)
    
    # Control deslizable (slider)
    peso = st.slider("Peso (kg)", 0, 150, 70) # se puede hacer rango y que permita seleccionar minimo y maximo
    
    # Selección de una opción entre varias (selectbox)
    genero = st.selectbox("Género", ["Masculino", "Femenino", "Otro"])
    
    # Selección múltiple (multiselect)
    intereses = st.multiselect("Intereses", 
                               ["Avistamiento de aves", "Fotografía", "Programación", "Arte", "Lectura"])
    
    # Selección de radio
    nivel_experiencia = st.radio("Nivel de experiencia en Python", 
                                 ["Principiante", "Intermedio", "Avanzado"])
    
    # Casilla de verificación (checkbox)
    aceptar_terminos = st.checkbox("Acepto los términos y condiciones")
    
    # Selección de fecha
    fecha_nacimiento = st.date_input("Fecha de nacimiento")
    
    # Selección de hora
    hora_cita = st.time_input("Hora de cita")
    
    # Selector de color
    color_favorito = st.color_picker("Elige tu color favorito", "#FFFFFF")
    
    # Subida de archivos
    archivo_subido = st.file_uploader("Sube un archivo", type=["png", "jpg", "pdf"])

    # Botón para enviar el formulario
    boton_enviar = st.form_submit_button("Enviar")

    # Si el usuario hace clic en el botón "Enviar", mostramos los datos introducidos
    if boton_enviar:
        st.write("## Datos introducidos:")
        st.write(f"- **Nombre:** {nombre}")
        st.write(f"- **Descripción:** {descripcion}")
        st.write(f"- **Edad:** {edad}")
        st.write(f"- **Peso:** {peso} kg")
        st.write(f"- **Género:** {genero}")
        st.write(f"- **Intereses:** {intereses}")
        st.write(f"- **Nivel de experiencia:** {nivel_experiencia}")
        st.write(f"- **Acepta términos:** {aceptar_terminos}")
        st.write(f"- **Fecha de nacimiento:** {fecha_nacimiento}")
        st.write(f"- **Hora de cita:** {hora_cita}")
        st.write(f"- **Color favorito:** {color_favorito}")

        # Validamos si hay un archivo subido
        if archivo_subido is not None:
            st.write("Archivo subido con éxito:")
            st.write(f"- Nombre del archivo: {archivo_subido.name}")
        else:
            st.write("No se subió ningún archivo.")
            
        # Para persistir estos datos hay multiples opciones:
        # opcion 1: utilizar mysql connector y hacer un insert a una base de datos
        # opcion 2: pasar los datos a un dataframe y moverlos con to_sql de Pandas a base de datos
        # opcion 3: pasarlos a un archivo csv o json utilizando los módulos csv o json de python o pickle
        # opción 4: utilizar la librería requests de python para enviarlos por HTTP POST a otro backend API REST