import numpy as np
import pandas as pd
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
st.divider()


# Gráficos univariantes

st.header('2. Gráficos univariantes')

columna = st.selectbox("Selecciona la columna numérica", options=df.select_dtypes('number').columns)

tab00, tab01 = st.tabs(['2.1 Histograma', '2.2 Boxplot'])

with tab00:
    fig, ax = plt.subplots(figsize=(6,4))
    sns.kdeplot(df, x=columna)
    sns.rugplot(df, x=columna)
    sns.histplot(df, x=columna, kde=True)
    ax.set_title(f'Análisis univariante de {columna}')
    ax.set_xlabel(f'{columna}')
    ax.set_ylabel('Frecuencia')
    st.pyplot(fig)

with tab01:
    fig, ax = plt.subplots(figsize=(6,4))
    dato = df[columna]
    ax.boxplot(dato, showmeans=True)
    ax.set_title(f'Boxplot de {columna}')
    ax.set_xlabel(f'{columna}')
    ax.set_ylabel('Frecuencia')
    st.pyplot(fig)
st.divider()

st.header('3. Gráficos bivariantes')

#filtros
columna_x = st.selectbox("Selecciona variable X", options=df.columns, key='x')
columna_y = st.selectbox("Selecciona variable Y", options=df.columns, key='y')
fig_scatter = px.scatter(df, x=columna_x, y=columna_y, title=f'Scatter plot de {columna_x} vs {columna_y}')
st.plotly_chart(fig_scatter)

st.divider()

st.header('4. Gráficos multivariantes')

#filtros
columna_x = st.selectbox("Selecciona variable X", options=df.columns, key='o')
columna_y = st.selectbox("Selecciona variable Y", options=df.columns, key='p')
columna_z = st.selectbox("Selecciona variable Z", options=df.columns, key='q')

tab1, tab2, tab3, tab4 = st.tabs(['4.1 Seaborn', '4.2. Plotly', '4.3 Heatmap numéricas', '4.4 Pairplot'])

with tab1:
    st.subheader('4.1 Seaborn')

    fig, ax = plt.subplots(figsize=(6,4))
    sns.scatterplot(df, x=columna_x, y=columna_y, hue=columna_z, palette='autumn', ax=ax)
    ax.set_title(f'Relación entre {columna_x}, {columna_y} y {columna_z} ')
    ax.set_xlabel(f'{columna_x}')
    ax.set_ylabel(f'{columna_y}')
    ax.legend()
    ax.grid()
    st.pyplot(fig)

with tab2:
    st.subheader('4.2. Plotly')

    fig = px.scatter(df, x=columna_x, y=columna_y, color=columna_z, color_continuous_scale='viridis')
    st.plotly_chart(fig)

with tab3:
    st.subheader('4.3 Heatmap numéricas')

    fig, ax = plt.subplots(figsize=(6,4))
    sns.heatmap(df.corr(numeric_only=True).round(2), annot=True)
    ax.set_title('Heatmap de correlación numéricas')
    st.pyplot(fig)
    st.divider()
    
with tab4:
    st.subheader('4.4 Pairplot')
    variables = ['x', 'y', 'z']
    grid = sns.pairplot(df, vars=variables, hue='cut')
    st.pyplot(grid.fig)

st.header('5. Gráficos con todos los filtros globales')

st.subheader('5.1 Filtros')

with st.expander('5.1.a. Filtros categóricos'):

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

with st.expander('5.1.b. Filtros numéricos'):

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



st.write('Gráficos nativos de Streamlit')

with st.expander('Gráfica de barras: st.bar_chart 📊'):
    st.subheader('Gráfica de barras: st.bar_chart 📊')
    df_group_by_cut = df_filtered.groupby('cut', observed=True)['price'].sum()
    st.table(df_group_by_cut)
    st.bar_chart(df_group_by_cut, color=['#00ff00'])
    #st.bar_chart(area_data)

with st.expander('Gráfica de líneas: st.line_chart'):
    
    line_data = df_filtered.sort_values('carat')[['carat', 'price']].set_index('carat')
    st.line_chart(line_data)
    
with st.expander('Gráfico de área: st.area_chart'):
    area_data = df_filtered.groupby('cut')['price'].mean().reset_index()
    area_data.set_index('cut', inplace=True)
    st.area_chart(area_data)

# with st.expander('Gráfico de mapa: st.map'):
#     num_points = df_filtered.shape[0]
#     map_data = pd.DataFrame({
#         'lat': np.random.uniform(37, 38, size=num_points),
#         'lon': np.random.uniform(-122, -121, size=num_points)
#     })
#     st.map(map_data)

with st.expander('Gráfico de scatter: st.scatter_chart'):
    scatter_data = df[['carat', 'price']]
    st.scatter_chart(scatter_data)

st.divider()


#Descargar datos
st.header('6. Descargar datos')
st.html('<p style="text-align:center">Descarga el dataset original o con los filtros actuales</p>')

col1, col2 = st.columns(2, vertical_alignment='center')

with col1:
    st.download_button(
        'Descargar datos originales',
        data=df.to_csv(index=False),
        file_name='diamonds_original.csv',
        mime='text/csv'
    ) 
    
with col2:    
    st.download_button(
        'Descargar datos filtrados',
        data=df_filtered.to_csv(index=False),
        file_name='diamonds_filtered.csv',
        mime='text/csv'
    )
    


