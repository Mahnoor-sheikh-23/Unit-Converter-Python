import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(page_title="Unit Converter", page_icon="\U0001F4CF", layout="centered")

# Load an icon image (optional)
st.image("https://cdn-icons-png.flaticon.com/512/2921/2921226.png", width=100)

# Custom styles
st.markdown(
    """
    <style>
        .big-font { font-size:30px !important; color: #4CAF50; text-align: center; }
        .stTextInput, .stSelectbox, .stButton { text-align: center; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<p class="big-font">Unit Converter</p>', unsafe_allow_html=True)

# Define conversion factors
conversions = {
    "meters_kilometers": 0.001,
    "kilometers_meters": 1000,
    "grams_kilograms": 0.001,
    "kilograms_grams": 1000,
    "inches_centimeters": 2.54,
    "centimeters_inches": 0.393701,
    "pounds_kilograms": 0.453592,
    "kilograms_pounds": 2.20462,
}

def convert_units(value, unit_from, unit_to):
    key = f"{unit_from}_{unit_to}"
    return value * conversions.get(key, "Conversion not available")

# User input
value = st.number_input("Enter the value to convert:", min_value=0.0, step=0.1)
unit_from = st.selectbox("Convert from:", list(set(k.split("_")[0] for k in conversions.keys())))
unit_to = st.selectbox("Convert to:", list(set(k.split("_")[1] for k in conversions.keys())))

if st.button("Convert \U0001F680"):
    result = convert_units(value, unit_from, unit_to)
    if isinstance(result, str):
        st.error(result)
    else:
        st.success(f"The converted value is {result:.4f} {unit_to}")

