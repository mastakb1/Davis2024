import streamlit as st
import pandas as pd
import plotly.express as px

# Menambahkan judul besar
st.title('Analisis Data Ketersediaan dan Pelatihan Pasca Perang')

# Membaca data dari CSV
df = pd.read_csv('war_survival_data.csv')

# Membuat scatter plot interaktif
fig = px.scatter(df, x='Food Supply (Days)', y='Water per Day (Liters)', color='Training Level',
           size='Weapons Available', hover_name='Name',
           labels={'Food Supply (Days)': 'Masa Persediaan Makanan (Hari)',
                   'Water per Day (Liters)': 'Konsumsi Air per Hari (Liter)',
                   'Training Level': 'Tingkat Pelatihan',
                   'Weapons Available': 'Senjata Tersedia'},
           title='Data Supplies and Training Level')

# Menambahkan informasi tambahan pada hover
fig.update_traces(hovertemplate='<b>%{hovertext}</b><br><br>' +
                                 'Masa Persediaan Makanan: %{x} hari<br>' +
                                 'Konsumsi Air per Hari: %{y} liter<br>' +
                                 'Senjata Tersedia: %{marker.size}<br>' +
                                 'Tingkat Pelatihan: %{marker.color}')

# Menampilkan plot utama
st.plotly_chart(fig)

# Visualisasi tambahan
st.write('## Visualisasi Tambahan')

fig_age = px.histogram(df, x='Age', title='Distribusi Umur')
st.plotly_chart(fig_age)

fig_food = px.bar(df, x='Name', y='Food Supply (Days)', title='Persediaan Makanan (Hari) Berdasarkan Nama')
st.plotly_chart(fig_food)

fig_training = px.pie(df, names='Training Level', title='Distribusi Tingkat Pelatihan')
st.plotly_chart(fig_training)

fig_supply = px.scatter_matrix(df, dimensions=['Food Supply (Days)', 'Water per Day (Liters)', 'First Aid Kits'],
                     title='Scatter Matrix untuk Data Supply')
st.plotly_chart(fig_supply)
