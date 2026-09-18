import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Gurgaon Real Estate Home", layout="wide")

st.title("🏘️ Gurgaon Real Estate Analytics Dashboard")

st.markdown("""
Welcome to the **Gurgaon Real Estate Analytics Dashboard** — an interactive web app designed to help users explore, analyze, and predict real estate prices across different sectors of Gurgaon.

---
### 🔍 Project Objective

- Analyze real estate trends in Gurgaon using data visualizations
- Understand pricing patterns based on features like location, area, number of bedrooms, and amenities
- Predict property prices using machine learning models

---
### 📊 Application Sections

1. **🏠 Home** — Overview of the app and purpose
2. **📈 Analysis App** — Interactive data visualizations (e.g., price maps, area vs price, pie charts)
3. **💰 Price Predictor** — Predict property prices using a trained ML model
""")

# load sample dataset
df = pd.read_csv("data_viz1.csv")

# chart: Average price per sqft by sector
st.subheader("📍 Sample Chart: Average Price per Sqft by Sector")
group_df = df.groupby("sector")["price_per_sqft"].mean().reset_index().sort_values(by="price_per_sqft", ascending=False)
fig = px.bar(group_df.head(10), x="sector", y="price_per_sqft", color="price_per_sqft",
             title="Top 10 Sectors by Average Price per Sqft",
             labels={"price_per_sqft": "Price per Sqft", "sector": "Sector"},
             height=500)

st.plotly_chart(fig, use_container_width=True)


