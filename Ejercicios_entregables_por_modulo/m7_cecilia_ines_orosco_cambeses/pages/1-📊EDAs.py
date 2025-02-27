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
st.dataframe(df)

# Gráficos univariantes
st.header('2. Gráficos univariantes')

fig, ax = plt.subplots(figsize=(6,4))
ax.hist(df['price'], bins=20, color='skyblue', edgecolor='black')
ax.set_title('Histograma de precios')
ax.set_xlabel('Precio')
ax.set_ylabel('Frecuencia')
st.pyplot(fig)

fig, ax = plt.subplots(figsize=(6,4))
sns.kdeplot(df, x='price')
sns.rugplot(df, x='price')
sns.histplot(df, x='price', kde=True)
ax.set_title('Análisis univariante Precio')
st.pyplot(fig)


fig, ax = plt.subplots(figsize=(6,4))
ax.boxplot(df['price'], showmeans=True)
ax.set_title('Boxplot de Precios')
ax.set_xlabel('Precio')
ax.set_ylabel('Frecuencia')
st.pyplot(fig)

fig, ax = plt.subplots(figsize=(6,4))
sns.histplot(df, x='table', bins=30, kde=True)
ax.set_title('Distribución de la proporción de la mesa en los diamantes')
ax.set_xlabel('Table (%)')
ax.set_ylabel('Frecuencia')
st.pyplot()

# categorical_features = df.dtypes[df.dtypes == object].index
# for feature in categorical_features:
#     fig, ax = plt.subplots(figsize=(6,4)) 
#     sns.countplot(y=feature, data=df, ax=ax)
#     ax.set_title(f"Distribución de {feature}")
#     st.pyplot(fig)

st.header('2. Gráficos bivariantes')
cut_colors = {'Ideal': 'orange', 'Premium': 'yellow', 'Good': 'pink', 'Very Good': 'red', 'Fair': 'green'}
fig, ax = plt.subplots(figsize=(6,4))
for cut, color in cut_colors.items():
    df_color = df[df['cut'] == color]
    ax.scatter(x=df_color['cut'], y=df_color['price'], color=color, label=cut)
    
ax.set_title('Relación entre corte y el precio')
ax.set_xlabel('Corte')
ax.set_ylabel('Precio')
ax.legend()
ax.grid()
st.pyplot(fig)

# Seaborn
st.header('2. Gráficos de Seaborn')

st.header('2. Gráficos multivariantes')
fig, ax = plt.subplots(figsize=(6,4))
sns.scatterplot(df, x='cut', y='price', hue='color', palette='autumn', ax=ax)
ax.set_title('Relación entre corte, precio y color ')
ax.set_xlabel('corte')
ax.set_ylabel('precio')
ax.legend()
ax.grid()
st.pyplot(fig)

fig, ax = plt.subplots(figsize=(6,4))
sns.heatmap(df.corr(numeric_only=True).round(2), annot=True)
ax.set_title('Heatmap de correlación numéricas')
st.pyplot(fig)

# Plotly
st.header('3. Gráficos de Plotly')
df_grouped = df.groupby(['cut', 'color'], as_index=False)['price'].mean()
st.table(df_grouped)
fig = px.bar(df_grouped, x='cut', y='price', color='color', title='Precio medio por corte')
st.plotly_chart(fig)

fig = px.scatter(df, x='cut', y='price', color='color')
st.plotly_chart(fig)


fig = px.scatter(df, x='cut', y='price', color='color', size='clarity')
st.plotly_chart(fig)

fig = px.scatter(df, x='cut', y='price', color='color', facet_col='clarity')
st.plotly_chart(fig)




df_tips = px.data.tips() 
