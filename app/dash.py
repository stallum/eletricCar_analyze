import streamlit as st
import pandas as pd
import plotly.express as px

# Instruções do aplicativo
# 1. visão geral do mercado de veículos elétricos
# 2. Desempenho de baterias e eficiência
# 3. Velocidade e Aceleração
# 4. Carracterísticas fisiscas dos veículos
# 5. Detalhes de carregamento

st.set_page_config(page_title="Electric Vehicles Dashboard", layout="wide")
st.title("Electric Vehicles Dashboard")

df = pd.read_csv('./data/electric_vehicles_spec_2025.csv', index_col=False)



# Informações gerais: Numero total de veículos, marcas e numeros ausentes nas colunas: range_km, battery_capacity_kWh, fast_charging_power_kw_dc, acceleration_0_100_s, top_speed_kmh
st.sidebar.header("General Information")
st.sidebar.write(f"Total number of vehicles: {df.shape[0]}")
st.sidebar.write(f"Total number of brands: {df['brand'].nunique()}")

st.sidebar.write(f"Missing values in 'range_km': {df['range_km'].isnull().sum()}")
st.sidebar.write(f"Missing values in 'battery_capacity_kWh': {df['battery_capacity_kWh'].isnull().sum()}")
st.sidebar.write(f"Missing values in 'fast_charging_power_kw_dc': {df['fast_charging_power_kw_dc'].isnull().sum()}")
st.sidebar.write(f"Missing values in 'acceleration_0_100_s': {df['acceleration_0_100_s'].isnull().sum()}")
st.sidebar.write(f"Missing values in 'top_speed_kmh': {df['top_speed_kmh'].isnull().sum()}")



col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)
col6, col7, col8 = st.columns(3)

# visão geral do mercado de veículos elétricos
brand_counts = df['brand'].value_counts().reset_index()
brand_counts.columns = ['brand', 'num_models']
fig_brand = px.bar(
    brand_counts,
    x='brand',
    y='num_models',
    color='brand',
    title='Number of Electric Vehicle Models by Brand',
)
fig_brand.update_layout(xaxis={'categoryorder':'total descending'})
col1.plotly_chart(fig_brand, use_container_width=True)

# Desempenho de baterias e eficiência
fig_battery = px.scatter(
    df,
    x='battery_capacity_kWh',
    y='range_km',
    color='brand',
    hover_name='model',
    title='Battery Capacity vs Efficiency of Electric Vehicles',
)
col2.plotly_chart(fig_battery, use_container_width=True)

fig_eficiency = px.histogram(
    df,
    x='efficiency_wh_per_km',
    color='brand',
    title='Distribution of Efficiency of Electric Vehicles',
    nbins=20,
)
col3.plotly_chart(fig_eficiency, use_container_width=True)

fig_body = px.box(
    df,
    x='car_body_type',
    y='seats',
    color='brand',
    title='Seats and Body Type of Electric Vehicles',
    points='all'
)
col4.plotly_chart(fig_body, use_container_width=True)

fig_bodyPerc = px.bar(
    df['car_body_type'].value_counts().reset_index(),
    x='count',
    y='car_body_type',
    color='count',
    title='Distribution of Body Types of Electric Vehicles'
)
col5.plotly_chart(fig_bodyPerc, use_container_width=True)


fig_charginPower = px.histogram(
    df,
    x='fast_charging_power_kw_dc',
    color='brand',
    title='Fast Charging Power and Port Type of Electric Vehicles',
)
col6.plotly_chart(fig_charginPower, use_container_width=True)

fig_charginPort = px.pie(
    df,
    names='fast_charge_port',
    title='Fast Charging Port Type of Electric Vehicles',
    color_discrete_sequence=px.colors.qualitative.Set3,
)
col7.plotly_chart(fig_charginPort, use_container_width=True)

fig_acceleration = px.scatter(
    df,
    x='acceleration_0_100_s',
    y='top_speed_kmh',
    color='brand',
    hover_name='model',
    title='Acceleration vs Top Speed of Electric Vehicles',
)
col8.plotly_chart(fig_acceleration, use_container_width=True)