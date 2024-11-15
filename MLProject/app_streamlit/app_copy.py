# app.py

import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open('../models/train_model_rf.pkl', 'rb') as f:  
    model = pickle.load(f)

# Custom CSS for buttons and input styles
st.markdown("""
<style>
div.stButton > button {
    background-color: #004b8d;
    color: #ffffff;
    border-radius: 10px;
    padding: 10px 20px;
}
div.stNumberInput, div.stSelectbox {
    border: 1px solid #004b8d;
    border-radius: 5px;
    padding: 5px;
}
.stCheckbox input[type=checkbox] {
    margin-right: 10px;
}
</style>
""", unsafe_allow_html=True)

# App title with icon
st.title("🩺 Depression Chronicity Prediction")

# App description with professional tagline
st.write("""
### "Empowering Your Mental Health Decisions"
Discover your risk for chronic depression with our data-driven tool. Gain valuable insights for proactive care and well-being.
""")

# Expander for better organization of input sections
with st.expander("Personal Information"):
    st.write('Enter your age *')
    age = st.number_input('Age', min_value=0, max_value=120, step=1)
    st.write('Select your marital status *')
    marital_status = st.selectbox('Marital Status', ['Single', 'Married', 'Divorced', 'Widowed'])
    st.write('Select your education level *')
    education_level = st.selectbox('Education Level', ['High School', "Bachelor's Degree", "Post-university", 'PhD'])
    st.write('Enter the number of children you have *')
    num_children = st.number_input('Number of Children', min_value=0, max_value=20, step=1)
    st.write('Enter your ANNUAL income *')
    income = st.number_input('Income', min_value=0.0, step=500.0)

with st.expander("Lifestyle & Habits"):
    st.write('Check the box if you are a smoker *')
    smoking_status = st.checkbox('Smoker')
    st.write('Check the box if you are currently employed *')
    employment_status = st.checkbox('Employed')

    st.write('Select your physical activity level *')
    physical_activity = st.radio('Physical Activity Level', ['Sedentary', 'Moderate', 'Active'])

    st.write('Select your alcohol consumption level *')
    alcohol_consumption = st.radio('Alcohol Consumption Level', ['Low', 'Moderate', 'High'])

    st.write('Indicate your dietary habits *')
    diet_level = st.radio('Dietary Habits', ['Unhealthy', 'Moderate', 'Healthy'])

    st.write('Indicate your sleep patterns *')
    sleep_level = st.radio('Sleep Patterns', ['Poor', 'Fair', 'Good'])

with st.expander("Medical History"):
    st.write('Check the boxes corresponding to your history, if any *')
    mental_illness_history = st.checkbox('History of Mental Illness', key='hist_mental')
    substance_abuse_history = st.checkbox('History of Substance Abuse', key='hist_abuse')
    family_depression_history = st.checkbox('Family History of Depression', key='hist_family_depression')

# Map input values to numeric values
marital_status = {'Single': 3, 'Married': 2, 'Divorced': 1, 'Widowed': 0}[marital_status]
education_level = {'High School': 0, "Bachelor's Degree": 2, "Post-university": 3, 'PhD': 1}[education_level]
smoking_status = 1 if smoking_status else 0
employment_status = 1 if employment_status else 0
physical_activity_level = {'Sedentary': 0, 'Moderate': 1, 'Active': 2}[physical_activity]
alcohol_consumption_level = {'Low': 0, 'Moderate': 1, 'High': 2}[alcohol_consumption]
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
    if probability > 0.5:
        st.success(f'Yes, there is a {probability_percentage:.2f}% probability of chronicity.')
    else:
        st.warning(f'No, the probability of chronicity is only {probability_percentage:.2f}%.')

# Footer note
st.markdown("---")
st.markdown("**Note:** This tool is for informational purposes only and should not replace professional medical advice.")