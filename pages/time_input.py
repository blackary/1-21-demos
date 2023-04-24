from datetime import time, timedelta

import streamlit as st

minutes = st.radio("Time step (minutes)", [1, 5, 10, 15, 30, 60])

with st.echo():
    st.time_input(
        "Set an alarm for",
        value=time(8, 0),
        step=timedelta(minutes=minutes),
    )
