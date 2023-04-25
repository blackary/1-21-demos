import streamlit as st

line_numbers = st.checkbox("Show line numbers", value=True)

width = st.slider("Code width", min_value=1, max_value=20, value=10)

_, col, _ = st.columns([1, width, 1])

col.code(
    f"""
import streamlit as st

st.write("Hello, world!")

st.code(
    "Insert your python code here!",
    language="python",
    line_numbers={line_numbers},
)
""",
    language="python",
    line_numbers=line_numbers,
)
