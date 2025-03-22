import streamlit as st
import scipy.stats as stats
import numpy as np
import pandas as pd

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

st.title("T-Test")


test = st.radio("Select Test type ", ["Independent Two-Sample Test" ])
alpha = st.radio("Select significance level ", [0.01, 0.05, 0.1])

if test == "Independent Two-Sample Test":
    
    st.text(f"Null Hypothesis : --- ")
    st.text(f"Alternate Hypothesis : --- ")
    
    st.subheader("Two sample test")
    
    data1 = st.text_area(label="Sample of independent variable (X)")
    arr1 = np.fromstring(data1, sep=',')
    
    data2 = st.text_area(label="Sample of dependent variable (Y)")
    arr2 = np.fromstring(data2, sep=',')
    
    button = st.button("Run Test")
    
    if button:
        
        t_stat, p_val = stats.ttest_ind(arr1, arr2)
        
        if p_val < alpha:
            st.text(f"alpha = {alpha}")
            st.text(f"p-value = {p_val}")
            
            st.subheader("Conclusion : p-value is less than choosen significance level, we can reject null Hypothesis.")
        
        else:
            st.text(f"alpha = {alpha}")
            st.text(f"p-value = {p_val}")
            
            st.subheader("p-value is greater than choosen significance level, we can not reject significance level")
    