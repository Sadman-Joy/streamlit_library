# streamlit_app.py

# ===========================
# 📌 1. Import required libraries
# ===========================
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# ===========================
# 📌 2. Page configuration
# ===========================
st.set_page_config(
    page_title="Streamlit Demo App",
    page_icon="🌐",
    layout="centered",
)

# ===========================
# 📌 3. Title and description
# ===========================
st.title("🌟 Welcome to Streamlit!")
st.write("This is a simple demo app to teach you the basics of Streamlit.")

# ===========================
# 📌 4. Show static data
# ===========================
st.header("1️⃣ Displaying a DataFrame")
data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 30, 22],
    'Score': [85, 90, 95]
})
st.dataframe(data)  # You can also use st.table() for static tables

# ===========================
# 📌 5. Chart/Graph display
# ===========================
st.header("2️⃣ Plotting a Chart")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)
st.line_chart(chart_data)

# ===========================
# 📌 6. User input widgets
# ===========================
st.header("3️⃣ Using Widgets")
name = st.text_input("What's your name?")
age = st.slider("Select your age", 0, 100, 25)

if st.button("Submit"):
    st.success(f"Hello {name}, you're {age} years old!")

# ===========================
# 📌 7. Image display
# ===========================
st.header("4️⃣ Displaying Images")
# You can replace 'your_image.jpg' with any local image path
try:
    image = Image.open("your_image.jpg")
    st.image(image, caption='Sample Image', use_column_width=True)
except FileNotFoundError:
    st.warning("Image not found. Please place 'your_image.jpg' in the same folder.")

# ===========================
# 📌 8. Sidebar usage
# ===========================
st.sidebar.title("🔧 Settings")
show_df = st.sidebar.checkbox("Show DataFrame")
if show_df:
    st.sidebar.write(data)

# ===========================
# 📌 9. Columns layout
# ===========================
st.header("5️⃣ Layout with Columns")
col1, col2 = st.columns(2)

with col1:
    st.info("This is column 1")

with col2:
    st.success("This is column 2")

# ===========================
# 📌 10. Ending note
# ===========================
st.markdown("---")
st.write("🎉 You've just built your first interactive Streamlit app!")

