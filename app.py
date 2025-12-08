import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Streamlit Test App", layout="wide")

st.title("🎈 Streamlit Test App")
st.write("Welcome to your Streamlit application!")

# Sidebar
with st.sidebar:
    st.header("Settings")
    name = st.text_input("Enter your name:", "User")
    slider_value = st.slider("Select a value:", 0, 100, 50)

st.write(f"Hello, {name}! You selected: {slider_value}")

# Data visualization
st.header("Data Visualization")

# Generate sample data
data = pd.DataFrame({
    'x': np.arange(0, 100),
    'y': np.random.randn(100).cumsum()
})

st.line_chart(data)

# Columns
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Metric 1", 42, "+5%")

with col2:
    st.metric("Metric 2", 1337, "-8%")

with col3:
    st.metric("Metric 3", 999, "+12%")

# Expander
with st.expander("Click to expand"):
    st.write("This is hidden content that can be revealed!")

# Footer
st.divider()
st.write("Made with ❤️ using Streamlit")
