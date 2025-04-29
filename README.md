# Statistical Hypothesis Testing Suite

## Overview
An interactive Streamlit web application that performs hypothesis testing (t-test, z-test, χ²-test, ANOVA) with automated result interpretation. Users input their sample data and receive clear conclusions about null hypothesis rejection.

## Features
- **Intuitive Interface**: Input data via CSV upload or manual entry
- **Supported Tests**:
  - Parametric: t-test (one/two-sample), z-test, one-way ANOVA
  - Non-parametric: Chi-square test
- **Automated Analysis**:
  - Checks test assumptions (normality, equal variance)
  - Calculates p-values and effect sizes
  - Provides visual diagnostics (distribution plots, Q-Q plots)
- **Clear Output**: Plain English conclusion about rejecting/failing to reject H₀

## Technical Implementation
- **Frontend**: Streamlit
- **Statistical Backend**: SciPy, StatsModels
- **Data Processing**: Pandas, NumPy

## How to Use
1. Clone the repository
2. Install requirements: `pip install -r requirements.txt`
3. Run the app: `streamlit run app.py`

## Professional Note
This project demonstrates core statistical understanding through a practical implementation. While intentionally kept simple for educational purposes, it reflects my ability to:
- Translate statistical concepts into usable tools
- Design intuitive data science interfaces
- Make technical outputs accessible to non-experts

In a production environment, I would extend this with:
- Advanced error handling
- Bayesian testing options
- Power analysis capabilities
- Comprehensive logging

The current implementation focuses on core functionality while maintaining clean, maintainable code - ask me about how I would adapt this for specific use cases like clinical trials or A/B testing scenarios.
