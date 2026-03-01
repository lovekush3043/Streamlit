import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Adidas Retail Store Analysis 🏬")

# Load dataset (replace with your actual CSV file name)
df = pd.read_csv("Adidas_Sales.csv")

# Show raw data
st.subheader("Raw Data Preview")
st.write(df.head())

# Example chart: Sales by Region
fig = px.bar(df, x="Region", y="Sales", color="Retailer", title="Sales by Region")
st.plotly_chart(fig)
