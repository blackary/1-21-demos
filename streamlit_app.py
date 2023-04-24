import datetime
import random

import streamlit as st

options = {
    "st": st,
    "st.line_chart": st.line_chart,
    "random": random,
    "datetime": datetime,
}

option = st.radio("Pick an option", options.keys())

obj = options[option]

st.code(
    f"""
st.help({option})
""",
    language="python",
)
st.help(obj)
