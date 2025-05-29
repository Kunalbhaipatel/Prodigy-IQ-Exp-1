
import streamlit as st
import pandas as pd
from dual_filter_panel import render_dual_filter_panel
from shaker_image_map import get_shaker_image

st.set_page_config(layout="wide", page_title="Prodigy IQ Flowline Shaker Dashboard")

# Load Data
@st.cache_data
def load_data():
    return pd.read_csv("Refine Sample.csv")

df = load_data()

# Sidebar Header
st.sidebar.image("images/Hyperpool 1.jpg", use_column_width=True)
st.sidebar.title("🔎 Filter Options")

# Global filter by shaker
shakers = df["flowline_Shakers"].dropna().unique().tolist()
selected_shaker = st.sidebar.selectbox("Select Flowline Shaker", shakers)

# Show shaker image
shaker_img = get_shaker_image(selected_shaker)
if shaker_img:
    st.image(shaker_img, caption=selected_shaker, width=400)

# Filter dataframe based on selected shaker
filtered_df = df[df["flowline_Shakers"] == selected_shaker]

# Render the dual filter panels with optional config toggles
render_dual_filter_panel(filtered_df)

st.markdown("---")
st.caption("Prodigy IQ Flowline Cost Comparison App © 2025")
