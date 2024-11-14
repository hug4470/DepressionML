# app.py

import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open('../models/train_model_rf.pkl', 'rb') as f:  
    model = pickle.load(f)

# App title
st.title('Depression Chronicity Prediction')

# App description
st.write('Based on this data, we will try to predict if you are at risk of your depression becoming chronic, in case you develop it.')

# Create input forms for each variable
st.write('Enter your age')
age = st.number_input('Age', min_value=0, max_value=120, step=1)
st.write('Select your marital status')
marital_status = st.selectbox('Marital Status', ['Single', 'Married', 'Divorced', 'Widowed'])
st.write('Select your education level')
education_level = st.selectbox('Education Level', ['High School', "Bachelor's Degree", "Post-university", 'PhD'])
st.write('Enter the number of children you have')
num_children = st.number_input('Number of Children', min_value=0, max_value=20, step=1)
st.write('Enter your ANNUAL income')
income = st.number_input('Income', min_value=0.0, step=500.0)  # Added income input
st.write('Check the box if you are a smoker')
smoking_status = st.checkbox('Smoker')
st.write('Check the box if you are currently employed')
employment_status = st.checkbox('Employed')

# Physical activity, alcohol, diet, and sleep options with checkboxes and unique keys
st.write('Select your physical activity level:')
physical_activity = {
    'Sedentary': st.checkbox('Sedentary', key='act_sedentary'),
    'Moderate': st.checkbox('Moderate', key='act_moderate'),
    'Active': st.checkbox('Active', key='act_active')
}
physical_activity_level = max(physical_activity, key=physical_activity.get)

st.write('Select your alcohol consumption level:')
alcohol_consumption = {
    'Low': st.checkbox('None', key='alc_low'),
    'Moderate': st.checkbox('Occasional', key='alc_moderate'),
    'High': st.checkbox('Habitual', key='alc_high')
}
alcohol_consumption_level = max(alcohol_consumption, key=alcohol_consumption.get)

st.write('Indicate your dietary habits:')
diet_habits = {
    'Unhealthy': st.checkbox('Unhealthy', key='diet_unhealthy'),
    'Moderate': st.checkbox('Regular', key='diet_moderate'),
    'Healthy': st.checkbox('Adequate', key='diet_healthy')
}
diet_level = max(diet_habits, key=diet_habits.get)

st.write('Indicate your sleep patterns:')
sleep_patterns = {
    'Poor': st.checkbox('Poor', key='sleep_poor'),
    'Fair': st.checkbox('Regular', key='sleep_fair'),
    'Good': st.checkbox('Good', key='sleep_good')
}
sleep_level = max(sleep_patterns, key=sleep_patterns.get)

st.write('Check the boxes corresponding to your history, if any.')

# Medical histories as checkboxes with unique keys
mental_illness_history = st.checkbox('History of Mental Illness', key='hist_mental')
substance_abuse_history = st.checkbox('History of Substance Abuse', key='hist_abuse')
family_depression_history = st.checkbox('Family History of Depression', key='hist_family_depression')

# Map input values to numeric values
marital_status = {'Single': 3, 'Married': 2, 'Divorced': 1, 'Widowed': 0}[marital_status]
education_level = {'High School': 0, "Bachelor's Degree": 2, "Master's Degree": 3, 'PhD': 1}[education_level]
smoking_status = 1 if smoking_status else 0
employment_status = 1 if employment_status else 0
physical_activity_level = {'Sedentary': 0, 'Moderate': 1, 'Active': 2}[physical_activity_level]
alcohol_consumption_level = {'Low': 0, 'Moderate': 1, 'High': 2}[alcohol_consumption_level]
diet_level = {'Unhealthy': 0, 'Moderate': 1, 'Healthy': 2}[diet_level]
sleep_level = {'Poor': 0, 'Fair': 1, 'Good': 2}[sleep_level]
mental_illness_history = 1 if mental_illness_history else 0
substance_abuse_history = 1 if substance_abuse_history else 0
family_depression_history = 1 if family_depression_history else 0

# Button to make prediction
if st.button('Predict'):
    # Create a DataFrame with the entered data
    user_data = pd.DataFrame({
        'Age': [age],
        'Marital Status': [marital_status],
        'Education Level': [education_level],
        'Number of Children': [num_children],
        'Smoking Status': [smoking_status],
        'Physical Activity Level': [physical_activity_level],
        'Employment Status': [employment_status],
        'Income': [income],
        'Alcohol Consumption': [alcohol_consumption_level],
        'Dietary Habits': [diet_level],
        'Sleep Patterns': [sleep_level],
        'History of Mental Illness': [mental_illness_history],
        'History of Substance Abuse': [substance_abuse_history],
        'Family History of Depression': [family_depression_history]
    })

    # Make prediction
    prediction = model.predict(user_data)
    probability = model.predict_proba(user_data)[0][1]  # Get chronicity probability

    # Convert probability to percentage
    probability_percentage = probability * 100

    # Display simplified result
    result = "Yes" if probability > 0.5 else "No"
    st.write(f'Chronicity Probability: {result} ({probability_percentage:.2f}%)')
