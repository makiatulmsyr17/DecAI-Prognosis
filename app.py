import streamlit as st
import pandas as pd
from model_utils import load_model, save_input_and_prediction_to_csv, make_prediction
import os

# Load model
model = load_model()

# Streamlit Application
# st.title('DecAI Prognosis: Predicting the 10-Year Risk of Mortality')

# CSS for dark theme
st.markdown(
    """
    <style>
    body {
        background-color: #121212;
        color: #ffffff;
    }
    .stButton>button {
        background-color: #000000;
        color: #FFFFFF;
        border-radius: 5px;
        border: 1px solid #FFFFFF;
    }
    .stButton>button:hover {
        background-color: #333333;
        color: #FFFFFF;
    }
    .stNumberInput>div>input {
        background-color: #1E1E1E;
        color: #FFFFFF;
    }

    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@700&display=swap" rel="stylesheet">
    <h1 style='font-family: Roboto, sans-serif; text-align: center; color: #33AFFF;'>
        🩺DecAI Prognosis🩺
    </h1>
    <p style='text-align: center; color: #ffffff;'>Predicting the 10-Year Risk of Mortality</p>
    """,
    unsafe_allow_html=True
)

# Create ./data folder if it doesn't exist
if not os.path.exists('./data'):
    os.makedirs('./data')

# Function to reset inputs
# Function to reset input values


def reset_input():
    st.session_state['Age'] = 0
    st.session_state['Pulse pressure'] = 0
    st.session_state['Systolic BP'] = 0
    st.session_state['Diastolic BP'] = 0
    st.session_state['Serum Cholesterol'] = 0
    st.session_state['Sedimentation rate'] = 0
    st.session_state['Sex'] = 'Male'  # Set to a valid option
    st.session_state['Serum Albumin'] = 0


# Reset button
if 'reset' not in st.session_state:
    st.session_state['reset'] = False

# Placeholder for reset message
reset_message_placeholder = st.empty()

# Reset button in the right column
col1, col2 = st.columns([9, 1])  # Adjust the proportions as needed
with col2:
    if st.button('🔄', help="Click to reset inputs"):
        reset_input()
        st.session_state['reset'] = True
        reset_message_placeholder.success("Inputs have been reset!")

# Clear reset message after a delay (optional)
if st.session_state['reset']:
    import time
    time.sleep(2)  # Delay in seconds
    st.session_state['reset'] = False
    reset_message_placeholder.empty()

# User inputs with units
Age = st.number_input('Enter value for Age (years):',
                      value=st.session_state.get('Age', 0), key='Age')
Pulse_pressure = st.number_input('Enter value for Pulse pressure (mmHg):',
                                 value=st.session_state.get('Pulse pressure', 0), key='Pulse pressure')
Systolic_BP = st.number_input('Enter value for Systolic BP (mmHg):',
                              value=st.session_state.get('Systolic BP', 0), key='Systolic BP')
Diastolic_BP = st.number_input('Enter value for Diastolic BP (mmHg):',
                               value=st.session_state.get('Diastolic BP', 0), key='Diastolic BP')
Serum_Cholesterol = st.number_input('Enter value for Serum Cholesterol (mg/dL):',
                                    value=st.session_state.get('Serum Cholesterol', 0), key='Serum Cholesterol')
Sedimentation_rate = st.number_input('Enter value for Sedimentation rate (mm/hr):',
                                     value=st.session_state.get('Sedimentation rate', 0), key='Sedimentation rate')

# Gender selection
Sex = st.radio(
    'Select gender:',
    options=['Male', 'Female'],
    index=0 if st.session_state.get('Sex', 'Male') == 'Male' else 1,
    key='Sex'
)
# Map the values for the model
Sex = 1 if Sex == 'Male' else 2

Serum_Albumin = st.number_input('Enter value for Serum Albumin (g/dL):',
                                value=st.session_state.get('Serum Albumin', 0), key='Serum Albumin')


# Predict button
if st.button('Predict'):
    # Create a DataFrame from user inputs matching the feature order during training
    input_data = pd.DataFrame({
        'Age': [Age],
        'Pulse pressure': [Pulse_pressure],
        'Systolic BP': [Systolic_BP],
        'Diastolic BP': [Diastolic_BP],
        'Serum Cholesterol': [Serum_Cholesterol],
        'Sedimentation rate': [Sedimentation_rate],
        'Sex': [Sex],
        'Serum Albumin': [Serum_Albumin],
    })

    # Make prediction using the model
    prediction = make_prediction(model, input_data)

    # Save user inputs and prediction result to CSV file
    save_input_and_prediction_to_csv(input_data, prediction)

    # Display prediction result with a Streamlit alert
    if prediction[0] == 1.0:
        st.success(
            'Prediction Result: **At Risk of Mortality** in the next 10 years')
    elif prediction[0] == 0.0:
        st.success('Prediction Result: **Not at Risk of Mortality**')
    else:
        st.warning('Prediction Result: Invalid prediction value.')

# Footer for copyright
st.markdown(
    """
    <hr style="border: 1px solid #333;">
    <p style="text-align: center; color: #AAAAAA; font-size: 12px;">
        © 2024 Garuda Insight. All rights reserved.
    </p>
    """,
    unsafe_allow_html=True
)
