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

# Check for duplicates
duplicates = df.duplicated()

# Count the number of duplicates
num_duplicates = duplicates.sum()
print("Number of duplicates:", num_duplicates)

# Remove duplicates
df = df[~duplicates]

# Reset index
df.reset_index(drop=True, inplace=True)

# Display the shape of the cleaned dataset
print("Shape of the cleaned dataset:", df.shape)



# Group by 'model' and fill missing 'model_year' values with the median year for each group
df['model_year'] = df.groupby('model')['model_year'].transform(lambda x: x.fillna(x.median()))

# Group by 'model' and fill missing 'cylinders' values with the median cylinders for each group
df['cylinders'] = df.groupby('model')['cylinders'].transform(lambda x: x.fillna(x.median()))

# Group by 'model_year' (or 'model' and 'year' combined) and fill missing 'odometer' values with the median or mean odometer reading for each group
df['odometer'] = df.groupby('model_year')['odometer'].transform(lambda x: x.fillna(x.median()))

# If you prefer to use 'model' and 'year' combined, you can use the following code:
# df['odometer'] = df.groupby(['model', 'model_year'])['odometer'].transform(lambda x: x.fillna(x.median()))

# Display the number of missing values after filling
print("Number of missing values after filling:")
print(df.isnull().sum())
