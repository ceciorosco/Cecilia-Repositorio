import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title='1-📊EDAs', page_icon=':bar_chart:')
st.title('Página 1 - EDAs')

col1, col2, col3 = st.columns(3)

with col1:
    if st.button('Volver a inicio'):
        st.switch_page('🏠Home.py')

with col2:
    if st.button('Ir a Regresión'):
        st.switch_page('pages/2-🧩Regresion.py')

with col3:
    if st.button('Ir a Clasificación'):
        st.switch_page('pages/3-🧬Clasificacion.py')

st.header('1. Carga de Datos')

# Cargar datos
df = sns.load_dataset('diamonds').dropna()
st.title('Gráficos de Matplotlib, Seaborn y Plotly en Streamlit')
st.dataframe(df.head(5))

# Gráficos univariantes

st.header('2. Gráficos univariantes')

#filtros
cut_filter= st.multiselect('Introduce corte (cut)', ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'], default=df['cut'].unique())
df_filtrado = df[df['cut'].isin(cut_filter)]

columna = st.selectbox("Selecciona la columna numérica", options=df.select_dtypes('number').columns)
fig, ax = plt.subplots(figsize=(6,4))
sns.kdeplot(df_filtrado, x=columna)
sns.rugplot(df_filtrado, x=columna)
sns.histplot(df_filtrado, x=columna, kde=True)
ax.set_title(f'Análisis univariante de {columna}')
ax.set_xlabel(f'{columna}')
ax.set_ylabel('Frecuencia')
st.pyplot(fig)

fig, ax = plt.subplots(figsize=(6,4))
dato = df_filtrado[columna]
ax.boxplot(dato, showmeans=True)
ax.set_title(f'Boxplot de {columna}')
ax.set_xlabel(f'{columna}')
ax.set_ylabel('Frecuencia')
st.pyplot(fig)

st.header('3. Gráficos bivariantes')

#filtros
columna_x = st.selectbox("Selecciona variable X", options=df.columns, key='x')
columna_y = st.selectbox("Selecciona variable Y", options=df.columns, key='y')
fig_scatter = px.scatter(df_filtrado, x=columna_x, y=columna_y, title=f'Scatter plot de {columna_x} vs {columna_y}')
st.plotly_chart(fig_scatter)

st.header('4. Gráficos multivariantes')

#filtros
columna_x = st.selectbox("Selecciona variable X", options=df.columns, key='o')
columna_y = st.selectbox("Selecciona variable Y", options=df.columns, key='p')
columna_z = st.selectbox("Selecciona variable Z", options=df.columns, key='q')

st.subheader('4.1 Seaborn')

fig, ax = plt.subplots(figsize=(6,4))
sns.scatterplot(df, x=columna_x, y=columna_y, hue=columna_z, palette='autumn', ax=ax)
ax.set_title(f'Relación entre {columna_x}, {columna_y} y {columna_z} ')
ax.set_xlabel(f'{columna_x}')
ax.set_ylabel(f'{columna_y}')
ax.legend()
ax.grid()
st.pyplot(fig)

st.subheader('4.2. Plotly')

fig = px.scatter(df, x=columna_x, y=columna_y, color=columna_z, color_continuous_scale='viridis')
st.plotly_chart(fig)

st.subheader('4.3 Heatmap numéricas')

fig, ax = plt.subplots(figsize=(6,4))
sns.heatmap(df.corr(numeric_only=True).round(2), annot=True)
ax.set_title('Heatmap de correlación numéricas')
st.pyplot(fig)

st.header('5. Gráficos con todos los filtros globales')

st.subheader('5.1 Filtros')



st.subheader('5.2 Gráficos')


