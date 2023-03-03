import streamlit as st
import pandas as pd
import numpy as np

st.title('게임 순위')
multi_select = st.multiselect('Please select somethings in multi selectbox!',
                                ['A', 'B', 'C', 'D'])
st.write('You selected:', multi_select)
