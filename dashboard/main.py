import streamlit as st
import pandas as pd


pg = st.navigation([
    st.Page("p_one.py", title="Introduction"),
    st.Page("p_two.py", title="Search by Topic"),
    st.Page("p_three.py", title="Search by Task"),
    st.Page("p_four.py", title="Search by Keyword"),
    st.Page("p_five.py", title="Search by Difficulty"),
    st.Page("p_six.py", title="Search by Paper"),
    st.Page("p_seven.py", title="Exam Papers"),
    st.Page("p_eight.py", title="Exam Papers Solutions"),
    st.Page("p_nine.py", title="Exam Papers Statistics"),
    st.Page("p_ten.py", title="Predict my Grade")
])

pg.run()