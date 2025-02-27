import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Cargar datos
df = sns.load_dataset('penguins').dropna()
st.title('Gráficos de Matplotlib, Seaborn y Plotly en Streamlit')
st.table(df.head())


# Filtros
st.header('Filtros globales')
st.subheader('Filtros categóricos')

# Filtro por species
species = df['species'].unique().tolist()
selected_species = st.multiselect('Selecciona una o varias especies', options=species, default=species)

# Filtro por island
islands = df['island'].unique().tolist()
selected_islands = st.multiselect('Selecciona una o varias islas', options=islands, default=islands)

# Filtro por género
genres = df['sex'].unique().tolist()
selected_genres = st.multiselect('Selecciona uno o varios géneros', options=genres, default=genres)

st.subheader('Filtros numéricos')

# obtenemos mínimo y máximo para usarlo en los filtros de abajo
bill_length_min, bill_length_max = st.slider(
    'Selecciona rango de Bill Length (mm)', 
    min_value=df['bill_length_mm'].min(),
    max_value=df['bill_length_mm'].max(),
    value=(df['bill_length_mm'].min(), df['bill_length_mm'].max())
)

# Aplicar los filtros
df_filtered = df[
    (df['species'].isin(selected_species)) & 
    (df['island'].isin(selected_islands)) &
    (df['sex'].isin(selected_genres)) &
    (df['bill_length_mm'] >= bill_length_min) & (df['bill_length_mm'] <= bill_length_max)
]

st.table(df_filtered.head())
st.write(f'Nº filas antes de filtrar: **{df.shape[0]}**')
st.write(f'Nº filas después de filtrar: **{df_filtered.shape[0]}**')
st.write(f'Nº filas eliminadas por filtro: **{df.shape[0] - df_filtered.shape[0]}**')

# Matplotlib
st.header('1. Gráficos de Matplotlib')
fig, ax = plt.subplots(figsize=(6,4))
ax.hist(df_filtered['flipper_length_mm'], bins=20, color='skyblue', edgecolor='black')
ax.set_title('Histograma de flipper length')
ax.set_xlabel('flipper_length_mm')
ax.set_ylabel('Frecuencia')
st.pyplot(fig)
st.caption('<p style="text-align:center">Figura 1: Gráfica de matplotlib univariante sobre flipper length. Elaboración propia.</p>', unsafe_allow_html=True)

fig, ax = plt.subplots(figsize=(6,4))
ax.boxplot(df_filtered['bill_length_mm'], showmeans=True)
ax.set_title('Boxplot de bill_length_mm')
ax.set_xlabel('bill_length_mm')
ax.set_ylabel('Frecuencia')
st.pyplot(fig)

species_colors = {'Adelie': 'blue', 'Gentoo': 'green', 'Chinstrap': 'red'}
fig, ax = plt.subplots(figsize=(6,4))
for specie, color in species_colors.items():
    df_specie = df_filtered[df_filtered['species'] == specie]
    ax.scatter(x=df_specie['bill_length_mm'], y=df_specie['body_mass_g'], color=color, label=specie)
    
ax.set_title('Relación entre bill_length_mm y body_mass_g')
ax.set_xlabel('bill_length_mm')
ax.set_ylabel('body_mass_g')
ax.legend()
ax.grid()
st.pyplot(fig)

# Seaborn
st.header('2. Gráficos de seaborn')

fig, ax = plt.subplots(figsize=(6,4))
sns.kdeplot(df_filtered, x='body_mass_g')
sns.rugplot(df_filtered, x='body_mass_g')
sns.histplot(df_filtered, x='body_mass_g', kde=True)
ax.set_title('Análisis univariante body_mass_g')
st.pyplot(fig)

fig, ax = plt.subplots(figsize=(6,4))
sns.scatterplot(df_filtered, x='bill_length_mm', y='body_mass_g', hue='species', palette='viridis', ax=ax)
ax.set_title('Relación entre bill_length_mm y body_mass_g')
ax.set_xlabel('bill_length_mm')
ax.set_ylabel('body_mass_g')
ax.legend()
ax.grid()
st.pyplot(fig)
# ax=ax si solo creamos una gráfica y no necesitamos controlar los ejes de manera explícita entonces no hace falta.
# ax=ax si queremos insertar la gráfica en un eje específico, creando varias subplots dentro del mismo gráfico podría hacer falta.


fig, ax = plt.subplots(figsize=(6,4))
sns.heatmap(df_filtered.corr(numeric_only=True).round(2), annot=True, cmap='viridis')
ax.set_title('Correlaciones')
st.pyplot(fig)


# Plotly:
st.header('3. Gráficos de Plotly')
df_grouped = df_filtered.groupby('species', as_index=False)['body_mass_g'].mean()
st.table(df_grouped)
# fig = px.bar(df_grouped)
fig = px.bar(df_grouped, x='species', y='body_mass_g', color='species', title='Peso medio por especie')
st.plotly_chart(fig)


fig = px.scatter(df_filtered, x='bill_length_mm', y='body_mass_g', color='species')
st.plotly_chart(fig)

fig = px.scatter(df_filtered, x='bill_length_mm', y='flipper_length_mm', color='species', size='body_mass_g', width=800, height=700)
st.plotly_chart(fig)

fig = px.scatter(df_filtered, x='bill_length_mm', y='flipper_length_mm', color='species', facet_col='sex')
st.plotly_chart(fig)

st.header('Descargar datos')
st.html('<p style="text-align:center">Descarga el dataset original o con los filtros actuales</p>')

col1, col2 = st.columns(2, vertical_alignment='center')

with col1:
    st.download_button(
        'Descargar datos originales',
        data=df.to_csv(index=False),
        file_name='penguins.csv',
        mime='text/csv'
    ) 
    
with col2:    
    st.download_button(
        'Descargar datos filtrados',
        data=df_filtered.to_csv(index=False),
        file_name='penguins_filtered.csv',
        mime='text/csv'
    )
    
st.write()