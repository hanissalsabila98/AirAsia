import streamlit as st
import numpy as np
import pandas as pd

st.header("My first Streamlit App")

option = st.sidebar.selectbox(
    'Select a mini project',
     ['line chart','map','T n C'])

if option=='line chart':
    chart_data = pd.DataFrame(
      np.random.randn(20, 3),
      columns=['a', 'b', 'c'])
    st.line_chart(chart_data)

st.write('Before you continue, please read the [terms and conditions](https://www.gnu.org/licenses/gpl-3.0.en.html)')
show = st.checkbox('I agree the terms and conditions')
if show:
    st.write(pd.DataFrame({
        'Students': ['John', 'Lofa', 'Siti', 'Amy'],
        'Attendance Status': ['yes', 'yes', 'yes', 'no']
    }))
