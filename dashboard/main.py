import streamlit as st
import pandas as pd


pg = st.navigation([
    st.Page("p_one.py", title="Univariate Analysis"),
    st.Page("p_two.py", title="Two Varible ANALYSIS"),
    st.Page("p_three.py", title="Three")
])

pg.run()