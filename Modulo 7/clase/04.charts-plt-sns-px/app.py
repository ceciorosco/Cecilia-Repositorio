import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Cargar datos
df = sns.load_dataset('penguins').dropna()
st.title('Gráficos de Matplotlib, Seaborn y Plotly en Streamlit')
st.table(df.head())

# Matplotlib
st.header('1. Gráficos de Matplotlib')
fig, ax = plt.subplots(figsize=(6,4))
ax.hist(df['flipper_length_mm'], bins=20, color='skyblue', edgecolor='black')
ax.set_title('Histograma de flipper length')
ax.set_xlabel('flipper_length_mm')
ax.set_ylabel('Frecuencia')
st.pyplot(fig)

fig, ax = plt.subplots(figsize=(6,4))
ax.boxplot(df['bill_length_mm'], showmeans=True)
ax.set_title('Boxplot de bill_length_mm')
ax.set_xlabel('bill_length_mm')
ax.set_ylabel('Frecuencia')
st.pyplot(fig)

species_colors = {'Adelie': 'blue', 'Gentoo': 'green', 'Chinstrap': 'red'}
fig, ax = plt.subplots(figsize=(6,4))
for specie, color in species_colors.items():
    df_specie = df[df['species'] == specie]
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
sns.kdeplot(df, x='body_mass_g')
sns.rugplot(df, x='body_mass_g')
sns.histplot(df, x='body_mass_g', kde=True)
ax.set_title('Análisis univariante body_mass_g')
st.pyplot(fig)

fig, ax = plt.subplots(figsize=(6,4))
sns.scatterplot(df, x='bill_length_mm', y='body_mass_g', hue='species', palette='viridis', ax=ax)
ax.set_title('Relación entre bill_length_mm y body_mass_g')
ax.set_xlabel('bill_length_mm')
ax.set_ylabel('body_mass_g')
ax.legend()
ax.grid()
st.pyplot(fig)
# ax=ax si solo creamos una gráfica y no necesitamos controlar los ejes de manera explícita entonces no hace falta.
# ax=ax si queremos insertar la gráfica en un eje específico, creando varias subplots dentro del mismo gráfico podría hacer falta.


fig, ax = plt.subplots(figsize=(6,4))
sns.heatmap(df.corr(numeric_only=True).round(2), annot=True, cmap='viridis')
ax.set_title('Correlaciones')
st.pyplot(fig)


# Plotly:
st.header('3. Gráficos de Plotly')
df_grouped = df.groupby('species', as_index=False)['body_mass_g'].mean()
st.table(df_grouped)
# fig = px.bar(df_grouped)
fig = px.bar(df_grouped, x='species', y='body_mass_g', color='species', title='Peso medio por especie')
st.plotly_chart(fig)


fig = px.scatter(df, x='bill_length_mm', y='body_mass_g', color='species')
st.plotly_chart(fig)

fig = px.scatter(df, x='bill_length_mm', y='flipper_length_mm', color='species', size='body_mass_g', width=800, height=700)
st.plotly_chart(fig)

fig = px.scatter(df, x='bill_length_mm', y='flipper_length_mm', color='species', facet_col='sex')
st.plotly_chart(fig)

# alternativa, cargar datos demo directamente con plotly.
df_tips = px.data.tips()