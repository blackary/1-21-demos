import streamlit as st

line_numbers = st.checkbox("Show line numbers", value=True)

st.code(
    """
import streamlit as st

obj = st.radio("Select an object", ["A", "B", "C"])

st.write(obj)
""",
    language="python",
    line_numbers=line_numbers,
)
