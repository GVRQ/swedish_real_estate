import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image


# Read data from xlsx files
file_path_bostadsratter = 'data/Bostadsratter_Riket_april2023.xlsx'
file_path_tabell = 'data/Tabell_Riket_april2023.xlsx'
file_path_tabell_riket = 'data/Tabell_Riket.xlsx'
file_path_utbud = 'data/utbud_lagenhet_sverige_23_04_07.xls'


df_bostadsratter_48m = pd.read_excel(file_path_bostadsratter, sheet_name='48 man')
df_bostadsratter_ar = pd.read_excel(file_path_bostadsratter, sheet_name='Arshistorik')
df_bostadsratter_prisrum = pd.read_excel(file_path_bostadsratter, sheet_name='Pris | Rum')

df_tabell_3m = pd.read_excel(file_path_tabell, sheet_name='3 manader')
df_tabell_12m = pd.read_excel(file_path_tabell, sheet_name='12 manader')
df_tabell_riket = pd.read_excel(file_path_tabell_riket, sheet_name='Statistik')

df_tabell_utbud = pd.read_excel(file_path_utbud, sheet_name='Utbud av bostader')

# Create Streamlit app
st.set_page_config(page_title="Swedish Real Estate Market Dashboard", page_icon=":house:", layout="wide")

# Add title and subheader
st.title("Swedish Real Estate Market Dashboard")
st.subheader("A comprehensive overview of the Swedish real estate market (apartments)")
# Add title and subheader
image = Image.open('sweden.jpg')
width, height = image.size
new_width = int(width * 0.5)
new_height = int(height * 0.5)
resized_image = image.resize((new_width, new_height))
st.image(resized_image)
st.markdown("Created by: https://linkedin.com/in/GVRQ/ on April 2023.")
st.markdown("Data used: Svensk Mäklarstatistik, https://www.maklarstatistik.se")


# Display Bostadsrätter i Riket, de senaste 48 månaderna
df_bostadsratter_48m = df_bostadsratter_48m.drop(0) # Drop first row
df_bostadsratter_48m.columns = df_bostadsratter_48m.iloc[0] # Set first row as column names
df_bostadsratter_48m = df_bostadsratter_48m.iloc[1:] # Drop first row (duplicate column names)

fig = px.line(df_bostadsratter_48m, x='Månad', y='kr/kvm', title='Bostadsrätter i Riket, de senaste 48 månaderna')
fig.update_traces(line=dict(width=3, color='#FFA500')) # Customize line width and color
fig.update_layout(
    plot_bgcolor='#FFFFFF',
    xaxis=dict(
        title='Månad',
        showgrid=False,
        showline=True,
        linewidth=2,
        linecolor='#BFBFBF',
        tickfont=dict(family='Arial', size=12),
    ),
    yaxis=dict(
        title='kr/kvm',
        showgrid=False,
        showline=True,
        linewidth=2,
        linecolor='#BFBFBF',
        tickfont=dict(family='Arial', size=12),
    ),
    font=dict(family='Arial', size=12),
    margin=dict(l=50, r=20, t=50, b=50)
)
st.plotly_chart(fig)

# Display Bostadsrätter i Riket, årshistorik
df_bostadsratter_ar = df_bostadsratter_ar.drop(0) # Drop first row
df_bostadsratter_ar.columns = df_bostadsratter_ar.iloc[0] # Set first row as column names
df_bostadsratter_ar = df_bostadsratter_ar.iloc[1:] # Drop first row (duplicate column names)

fig2 = px.line(df_bostadsratter_ar, x='År', y='kr/kvm', title='Bostadsrätter i Riket, årshistorik')
fig2.update_traces(line=dict(width=2.5, color='#FFA500'))
fig2.update_layout(
    plot_bgcolor='#FFFFFF',
    xaxis=dict(
        title='År',
        showgrid=False,
        showline=True,
        linewidth=2,
        linecolor='#BFBFBF',
        tickfont=dict(family='Arial', size=12),
    ),
    yaxis=dict(
        title='Pris per kvadratmeter (kronor)',
        showgrid=False,
        showline=True,
        linewidth=2,
        linecolor='#BFBFBF',
        tickfont=dict(family='Arial', size=12),
    ),
    font=dict(family='Arial', size=12),
    margin=dict(l=50, r=20, t=50, b=50)
)
st.plotly_chart(fig2)

# Display Bostadsrätter Lägenhetsstorlek i Riket, de senaste 48 månaderna
df_bostadsratter_prisrum = df_bostadsratter_prisrum.drop(0) # Drop first row
df_bostadsratter_prisrum.columns = df_bostadsratter_prisrum.iloc[0] # Set first row as column names
df_bostadsratter_prisrum = df_bostadsratter_prisrum[['Månad','1:or','2:or','3:or','4:or+']].reset_index(drop=True) # Select relevant columns and reset index

# Create line chart using Plotly Express

fig3 = px.line(df_bostadsratter_prisrum, x='Månad', y=['1:or','2:or','3:or','4:or+'], title='Bostadsrätter, Lägenhetsstorlek i Riket, de senaste 48 månaderna')
fig3.update_traces(
line=dict(width=2.5) # Increase line width for better visibility
)
fig3.update_layout(
plot_bgcolor='white', # Set plot background color
xaxis_title='Månad', # Set x-axis title
yaxis_title='Pris per kvadratmeter (kronor)', # Set y-axis title
font=dict(family='Arial', size=12), # Set font family and size
margin=dict(l=50, r=20, t=50, b=50) # Set plot margins
)
st.plotly_chart(fig3)
# Display Utbud av bostäder

df_tabell_utbud = df_tabell_utbud.rename(columns={"Period": "Månad"})
fig = px.line(df_tabell_utbud, x='Månad', y=['1:or', '2:or', '3:or', '4:or+'], title='Utbud av bostadsrätter, Lägenhetsstorlek i Riket, de senaste 48 månaderna')
fig.update_traces(line=dict(width=2.5))
fig.update_layout(
plot_bgcolor='white', # Set plot background color
xaxis_title='Månad', # Set x-axis title
yaxis_title='Antal bostadsrätter', # Set y-axis title
font=dict(family='Arial', size=12), # Set font family and size
margin=dict(l=50, r=20, t=50, b=50) # Set plot margins
)
st.plotly_chart(fig)


# Display Statistik, 3 månader
df_tabell_3m = df_tabell_3m.rename(columns={"Områden": "Område"})
if 0 in df_tabell_3m.index:
    df_tabell_3m = df_tabell_3m.drop(0) # Drop first row if it exists

st.subheader('Län i riket, 3 månader')

# Set custom color scheme
colors = ['#FFA500', '#7FDBFF', '#2ECC40', '#FF4136']

# Create grouped bar charts using Plotly Express
fig_kr_kvm = px.bar(df_tabell_3m, x='Område', y='Kr/kvm', title='Kr/kvm per Län', color='Kr/kvm', color_discrete_sequence=colors)
fig_antal_salda = px.bar(df_tabell_3m, x='Område', y='Antal sålda', title='Antal sålda per Län', color='Antal sålda', color_discrete_sequence=colors)
fig_medelpris = px.bar(df_tabell_3m, x='Område', y='Medelpris kr', title='Medelpris per Län', color='Medelpris kr', color_discrete_sequence=colors)
fig_prisutv = px.bar(df_tabell_3m, x='Område', y='Prisutveckling (%)', title='Prisutveckling per Län', color='Prisutveckling (%)', color_discrete_sequence=colors)

# Customize bar charts
for fig in [fig_kr_kvm, fig_antal_salda, fig_medelpris, fig_prisutv]:
    fig.update_traces(marker_line_color='white', marker_line_width=0.5)

# Set background color and font
bgcolor = '#f2f2f2'
font = 'Arial'

# Set layout properties
layout = go.Layout(
    plot_bgcolor=bgcolor,
    paper_bgcolor=bgcolor,
    xaxis=dict(
        showgrid=False,
        showticklabels=True,
        linecolor='#BCCCDC',
        linewidth=2,
        ticks='outside',
        tickfont=dict(family=font, size=12),
        tickangle=-45
    ),
    yaxis=dict(
        showgrid=True,
        gridcolor='#BCCCDC',
        gridwidth=1,
        linecolor='#BCCCDC',
        linewidth=2,
        ticks='outside',
        tickfont=dict(family=font, size=12)
    ),
    font=dict(family=font, size=12),
    margin=dict(l=50, r=20, t=50, b=50),
)

# Update layout for each bar chart
fig_kr_kvm.update_layout(layout)
fig_antal_salda.update_layout(layout)
fig_medelpris.update_layout(layout)
fig_prisutv.update_layout(layout)

# Display bar charts
st.plotly_chart(fig_kr_kvm)
st.plotly_chart(fig_antal_salda)
st.plotly_chart(fig_medelpris)
st.plotly_chart(fig_prisutv)


# Display Statistik, 12 månader
df_tabell_12m = df_tabell_12m.rename(columns={"Områden": "Område"})
df_tabell_12m = df_tabell_12m.drop(0) # Drop first row
st.subheader('Län i riket, 12 månader')

# Set custom color scheme
colors = ['#FFA500', '#7FDBFF', '#2ECC40', '#FF4136']

# Create grouped bar charts using Plotly Express
fig_kr_kvm_12m = px.bar(df_tabell_12m, x='Område', y='Kr/kvm', title='Kr/kvm per Län', color='Kr/kvm', color_discrete_sequence=colors)
fig_antal_salda_12m = px.bar(df_tabell_12m, x='Område', y='Antal sålda', title='Antal sålda per Län', color='Antal sålda', color_discrete_sequence=colors)
fig_medelpris_12m = px.bar(df_tabell_12m, x='Område', y='Medelpris kr', title='Medelpris per Län', color='Medelpris kr', color_discrete_sequence=colors)
fig_prisutv_12m = px.bar(df_tabell_12m, x='Område', y='Prisutveckling (%)', title='Prisutveckling per Län', color='Prisutveckling (%)', color_discrete_sequence=colors)

# Customize bar charts
for fig in [fig_kr_kvm_12m, fig_antal_salda_12m, fig_medelpris_12m, fig_prisutv_12m]:
    fig.update_traces(marker_line_color='white', marker_line_width=0.5)

# Set background color and font
bgcolor = '#f2f2f2'
font = 'Arial'

# Set layout properties
layout = go.Layout(
    plot_bgcolor=bgcolor,
    paper_bgcolor=bgcolor,
    xaxis=dict(
        showgrid=False,
        showticklabels=True,
        linecolor='#BCCCDC',
        linewidth=2,
        ticks='outside',
        tickfont=dict(family=font, size=12),
        tickangle=-45
    ),
    yaxis=dict(
        showgrid=True,
        gridcolor='#BCCCDC',
        gridwidth=1,
        linecolor='#BCCCDC',
        linewidth=2,
        ticks='outside',
        tickfont=dict(family=font, size=12)
    ),
    font=dict(family=font, size=12),
    margin=dict(l=50, r=20, t=50, b=50),
)

# Update layout for each bar chart
fig_kr_kvm_12m.update_layout(layout)
fig_antal_salda_12m.update_layout(layout)
fig_medelpris_12m.update_layout(layout)
fig_prisutv_12m.update_layout(layout)

# Display bar charts
st.plotly_chart(fig_kr_kvm_12m)
st.plotly_chart(fig_antal_salda_12m)
st.plotly_chart(fig_medelpris_12m)
st.plotly_chart(fig_prisutv_12m)
