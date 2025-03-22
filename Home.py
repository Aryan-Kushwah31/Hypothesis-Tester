import streamlit as st
import pandas as pd
import numpy as np
import scipy.stats as stats

st.set_page_config(
    page_title="Hypothesis Testing",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.title("Hypothesis Tester")
st.header("Welcome!")

st.write("In today's data-rich environment, making informed decisions is crucial. However, traditional hypothesis testing can be time-consuming and complex. That's why I developed a streamlined tool to simplify this process, empowering you to extract meaningful insights from your data quickly and efficiently.")

st.subheader("How to Use")
st.write("1. Enter the data in the text area.\n2. Choose the appropriate test and significance level.\n3. Click on the 'Run Test' button to generate results.")

st.subheader("With this tool, you can:")
st.write("1. Quickly validate hypotheses and gain confidence in your data.\n2. Reduce the risk of making decisions based on faulty assumptions.\n3. Save valuable time and resources.")


st.subheader("Note : This tool currently supports the following tests:")
st.write("1. T-Test\n2. Chi-Square Test\n3. ANOVA Test\n4. Post-Hoc Test")

st.subheader('Disclaimer')

st.text(f"Please note that this hypothesis testing tool is currently in its testing phase and is provided as a work-in-progress. While every effort has been made to ensure accuracy, the results generated should be interpreted with caution. As with any statistical tool, errors can occur, and the output may not always be perfectly aligned with real-world scenarios.")
st.text("I am actively working on enhancing this project by adding more user-friendly features and expanding its capabilities. Your feedback is invaluable in this process.")
st.text("This tool is intended for personal projects and experimentation. If you have specific needs or require assistance with your own data analysis, please feel free to reach out to me directly on LinkedIn or Instagram. I am also open to collaboration and welcome insightful feedback to improve the tool's functionality and accuracy.")
st.text("By using this tool, you acknowledge that you understand its current developmental stage and agree to use it responsibly. Please verify results with other methods when making critical decisions. Thank you for your understanding and support!")
