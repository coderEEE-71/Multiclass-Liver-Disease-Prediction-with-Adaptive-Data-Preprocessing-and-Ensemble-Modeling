import streamlit as st
import pickle
from sklearn.preprocessing import StandardScaler
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler
# Load the scaler from the file
ss = joblib.load('scaler.pkl')
liver_model = pickle.load(open('D:/user interface/liver_model2.sav', 'rb'), encoding='latin1')

# Page title
st.title('Liver Disease Prediction using ML')

# Getting the input data from the user
col1, col2, col3 = st.columns(3)

with col1:
    Age = st.text_input('Age of the Person')

with col2:
    Sex = st.selectbox('Sex', ['Male', 'Female'])
with col3:
    ALB = st.text_input('ALB Level')

with col1:
    ALP = st.text_input('ALP Level')

with col2:
    ALT = st.text_input('ALT level')

with col3:
    AST = st.text_input('AST Level')

with col1:
    BIL = st.text_input('BIL value')

with col2:
    CHE = st.text_input('CHE value')

with col3:
    CHOL = st.text_input('CHOL level')

with col1:
   CREA = st.text_input('CREA level')

with col2:
    GGT = st.text_input('GGT level')

with col3:
    PROT = st.text_input('PROT level')

# Prepare for prediction
liver_diagnosis = ''

# Creating a button for prediction
if st.button('Liver Test Result'):
    user_input = [[Age, ALB, ALP, ALT, AST, BIL, CHE, CHOL, GGT, PROT]]

    user_input_scaled = ss.transform(user_input)  # use transform() instead of fit_transform()
    liver_prediction = liver_model.predict(user_input_scaled)

    #st.write('The prediction result is: ', liver_prediction)  # Show the liver_prediction variable
    #st.write(f'Input Features: {user_input_scaled}')
    if liver_prediction[0] == 0:
        liver_diagnosis = 'The person is normal'
    elif liver_prediction[0] == 1:
        liver_diagnosis = 'The person is suspected of liver disease'
    elif liver_prediction[0] == 2:
        liver_diagnosis = 'The person has hepatitis'
    elif liver_prediction[0] == 3:
        liver_diagnosis = 'The person has fibrosis'
    elif liver_prediction[0] == 4:
        liver_diagnosis = 'The person has cirrhosis'

    st.success(liver_diagnosis)

