import streamlit as st

line_numbers = st.checkbox("Show line numbers", value=True)

st.code(
    """
import streamlit as st

st.code("Insert your python code here!", language="python", line_number = True)

""",
    language="python",
    line_numbers=line_numbers,
)
