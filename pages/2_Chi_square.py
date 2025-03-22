import streamlit as st
import scipy.stats as stats
import numpy as np
import pandas as pd

st.title("Chi-Square Test")

test = st.radio("Select type of test to perform ", ['Test for independence'])
alpha = st.radio("Select significance level ", [0.01, 0.05, 0.1])

if test == 'Test for independence':
    
    st.text(f"Null Hypothesis : --- ")
    st.text(f"Alternate Hypothesis : --- ")
    
    freq_1 = st.text_area("Enter Frequency of variable 1")
    freq_2 = st.text_area("Enter Frequency of variable 2")
    col_1 = np.fromstring(freq_1, sep=',')
    col_2 = np.fromstring(freq_2, sep=',')
    df = pd.DataFrame()
    
    button = st.button("Run Test")
    
    if button:
        df["col-1"] = col_1
        df["col-2"] = col_2
            
        observed_data = pd.crosstab(df["col-1"], df["col-2"] , margins=True)
        chi_stat, p, dof, expected = stats.chi2_contingency(observed_data)
        
        if p < alpha:
            st.text(f"Chi-Square Statistic : {chi_stat}")
            st.text(f"p-value : {p}")
            st.text(f"Degree of Freedom : {dof}")
            st.subheader("p-value is less than choosen Significance level, so, we can reject Null hypothesis. ")
        else:
            st.text(f"Chi-Square Statistic : {chi_stat}")
            st.text(f"p-value : {p}")
            st.text(f"Degree of Freedom : {dof}")
            st.subheader("p-value is greater than choosen significance level, so we can not reject Null Hypothesis")