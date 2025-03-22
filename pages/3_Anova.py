import streamlit as st
import scipy.stats as stats
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

st.title("ANOVA Test")

test = st.radio("Select Test Type", ['One-Way ANOVA', 'Two-Way ANOVA'])

if test == 'One-Way ANOVA':
    
    st.text(f"Null Hypothesis : --- ")
    st.text(f"Alternate Hypothesis : --- ")
    
    st.subheader("One-Way ANOVA")
    
    alpha = st.radio("Select a significance level", [0.01, 0.05, 0.1])
    
    x = st.text_area("Enter data of variable X")
    y = st.text_area("Enter data of variable Y")
    
    button = st.button("Run Test")
    
    if button:
        x_arr = np.fromstring(x, sep=',')
        y_arr = np.fromstring(y, sep=',')
        
        df = pd.DataFrame()
        df["x"] = x_arr
        df["y"] = y_arr
        
        model = ols('x ~ y', data=df).fit()

        result = sm.stats.anova_lm(model, typ=2)
        
        p_value = result['PR(>F)'][0]
        
        if p_value < 0.05:
            st.text(f"p-value : {p_value}")
            st.subheader(f"p-value is less than {alpha}, so, we can reject Null hypothesis. ")
        else:
            st.text(f"p-value : {p_value}")
            st.subheader(f"p-value is greater than {alpha}, so we can not reject Null Hypothesis")    
        
if test == 'Two-Way ANOVA':
    
    st.warning("Working on it. Will start this test soon...")