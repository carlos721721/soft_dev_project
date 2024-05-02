import streamlit as st
import pandas as pd
import plotly.express as px

# Read the dataset into a Pandas DataFrame
@st.cache_data  # This decorator will cache the data, making it faster to load
def load_data():
    url = "https://practicum-content.s3.us-west-1.amazonaws.com/datasets/vehicles_us.csv"
    df = pd.read_csv(url)
    return df

df = load_data()

# Title/Header
st.header("Vehicle Advertisement Dashboard")

# Checkbox to toggle behavior
show_histogram = st.checkbox("Show Histogram")

# Plotly Express histogram
if show_histogram:
    st.write("## Distribution of Vehicle Prices")
    fig_hist = px.histogram(df, x='price', title='Distribution of Vehicle Prices')
    st.plotly_chart(fig_hist)

# Checkbox to toggle behavior
show_scatterplot = st.checkbox("Show Scatter Plot")

# Plotly Express scatter plot
if show_scatterplot:
    st.write("## Vehicle Price vs. Mileage")
    fig_scatter = px.scatter(df, x='odometer', y='price', title='Vehicle Price vs. Mileage')
    st.plotly_chart(fig_scatter)
