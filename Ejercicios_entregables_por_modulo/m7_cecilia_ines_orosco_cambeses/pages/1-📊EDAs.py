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

st.write('5.1.a. Filtros categóricos')

col1, col2, col3 = st.columns(3)

color = df['color'].unique().tolist()
with col1:
    selected_color = st.multiselect('Selecciona uno o varios colores', options=color, default=color)

clarity = df['clarity'].unique().tolist()
with col2:
    selected_clarity = st.multiselect('Selecciona una o varias claridades', options=clarity, default=clarity)

cut = df['cut'].unique().tolist()
with col3:
    selected_cut = st.multiselect('Selecciona uno o varios cortes', options=cut, default=cut)

st.write('5.1.b. Filtros numéricos')

# obtenemos mínimo y máximo para usarlo en los filtros de abajo
col4, col5, col6 = st.columns(3)

with col4:
    carat_min, carat_max = st.slider(
        'Selecciona rango de peso (carat)', 
        min_value=df['carat'].min(),
        max_value=df['carat'].max(),
        value=(df['carat'].min(), df['carat'].max())
    )

with col5:
    depth_min, depth_max = st.slider(
        'Selecciona rango de densidad (depth)', 
        min_value=df['depth'].min(),
        max_value=df['depth'].max(),
        value=(df['depth'].min(), df['depth'].max())
    )

with col6:
    table_min, table_max = st.slider(
        'Selecciona rango de mesa (table)', 
        min_value=df['table'].min(),
        max_value=df['table'].max(),
        value=(df['table'].min(), df['table'].max())
    )

price_min, price_max = st.slider(
    'Selecciona rango de precio (price)', 
    min_value=df['price'].min(),
    max_value=df['price'].max(),
    value=(df['price'].min(), df['price'].max())
)

col7, col8, col9 = st.columns(3)

with col7:
    x_min, x_max = st.slider(
        'Selecciona rango de alto (x)', 
        min_value=df['x'].min(),
        max_value=df['x'].max(),
        value=(df['x'].min(), df['x'].max())
    )

with col8:
    y_min, y_max = st.slider(
        'Selecciona rango de ancho (y)', 
        min_value=df['y'].min(),
        max_value=df['y'].max(),
        value=(df['y'].min(), df['y'].max())
    )

with col9:
    z_min, z_max = st.slider(
        'Selecciona rango de profundidad (z)', 
        min_value=df['z'].min(),
        max_value=df['z'].max(),
        value=(df['z'].min(), df['z'].max())
    )

# Aplicar los filtros
df_filtered = df[
    (df['cut'].isin(selected_cut)) & 
    (df['color'].isin(selected_color)) &
    (df['clarity'].isin(selected_clarity)) &
    (df['carat'] >= carat_min) & (df['carat'] <= carat_max) &
    (df['depth'] >= depth_min) & (df['depth'] <= depth_max) &
    (df['table'] >= table_min) & (df['table'] <= table_max) &
    (df['price'] >= price_min) & (df['price'] <= price_max) &
    (df['x'] >= x_min) & (df['x'] <= x_max) &
    (df['y'] >= y_min) & (df['y'] <= y_max) &
    (df['z'] >= z_min) & (df['z'] <= z_max)
]

st.table(df_filtered.head())
st.write(f'Nº filas antes de filtrar: **{df.shape[0]}**')
st.write(f'Nº filas después de filtrar: **{df_filtered.shape[0]}**')
st.write(f'Nº filas eliminadas por filtro: **{df.shape[0] - df_filtered.shape[0]}**')



st.subheader('5.2 Gráficos')


