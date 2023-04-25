import streamlit as st

def space(num_lines: int = 1):
    """Adds empty lines to the Streamlit app."""
    for _ in range(num_lines):
        st.write("")
st.title("Hello, world!", help="This is a help message")

st.header("This is a header", help="This is a help message")

st.text(
    """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua.
    """,
    help="This is a help message",
)

space(5)

st.header("""Spice your text element with a tooltip :laughing:""", help="This is a help message",)


