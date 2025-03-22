import streamlit as st
import scipy.stats as stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.stats.multicomp import pairwise_tukeyhsd



st.title("Post-Hoc Test")

test = st.radio("Select a Test", ["Tukey's HSD Test", "Bonferroni Test"])
sig_level = st.radio("Select a significance level", [0.01, 0.05, 0.1])

if test == "Tukey's HSD Test":
    st.subheader("Tukey's HSD")
    
    x = st.text_area("Enter variable X")
    y = st.text_area("Enter variable Y")
    
    x_arr = np.fromstring(x, sep=',')
    y_arr = np.fromstring(x, sep=',')
    
    button = st.button("Run Test")
    
    if button:
        
        df = pd.DataFrame()
        df['x'] = x_arr
        df['y'] = y_arr
        
        tukey = pairwise_tukeyhsd(endog=df['x'], groups=df['y'], alpha=sig_level)
        tukey_df = tukey.summary()
        
        st.subheader("Results")
        st.dataframe(tukey_df)
        
if test == "Bonferroni Test":
    st.subheader("Bonferroni Test")
    st.warning("Working on it, will start this test soon...")