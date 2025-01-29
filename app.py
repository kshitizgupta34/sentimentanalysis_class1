import streamlit as st
import pickle
import pandas as pd

st.title('California Hosing Price Prediction')
st.write('Trial 1')

model = pickle.load(open('model_lr.pkl','rb'))

med_inc = st.number_input('Median Income')

if st.button('Predict'):
    st.write('Hello')