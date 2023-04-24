import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

# Set numpy random state
np.random.seed(42)

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

use_container_width = st.checkbox("Use container width?", value=True)

with st.echo():
    st.pyplot(fig, use_container_width=use_container_width)
