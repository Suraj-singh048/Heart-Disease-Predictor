import streamlit as st
import pickle
import pandas as pd
import random
import numpy as np

model = pickle.load(open('gs-log-reg.model', 'rb'))

data_file = '6.1 heart-disease.csv'
df = pd.read_csv(data_file)

# Define the features that predict the target as 1 for heart disease
features = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']

# Function to predict heart disease
def predict_heart_disease(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
    input_data = pd.DataFrame({
        'age': [age],
        'sex': [sex],
        'cp': [cp],
        'trestbps': [trestbps],
        'chol': [chol],
        'fbs': [fbs],
        'restecg': [restecg],
        'thalach': [thalach],
        'exang': [exang],
        'oldpeak': [oldpeak],
        'slope': [slope],
        'ca': [ca],
        'thal': [thal]
    })
    prediction = model.predict(input_data)
    return prediction[0]

# Streamlit app
def main():
    st.markdown('<h1 style="color: red;">Heart Disease Predictor</h1>', unsafe_allow_html=True)
    st.markdown('<span style="color: #219C90; font-size: 26px; font-weight: bold;">Empowering Health Decisions: Predicting Heart Disease with Data Science</span>', unsafe_allow_html=True)
    st.sidebar.markdown('<h2 style="color: Orange; font-weight: bold;">Enter Patient Information</h2>', unsafe_allow_html=True)
    st.markdown(
        """
        <style>
            .stButton>button {
            background-color: #90ee90; /* Set background color of predict button to light green */
            color: #333333; /* Set text color of predict button to dark gray */}

            [data-testid=stAppViewBlockContainer] {
                    width: 100%;
                    padding: 2.5rem;
                    max-width: 100%;
            }
            
            @media (min-width: 576px)  {
                [data-testid=stAppViewBlockContainer] {
                    padding-left: 3rem;
                    padding-right: 3rem;    
                }
            }
            
            .st-emotion-cache-uf99v8 {
                height: 100svh;
            }
            
            [data-testid=stAppViewBlockContainer] {
                height: 100%;
            }
            
            [data-testid=stVerticalBlockBorderWrapper] {
                height: 100%;
            }
            
            .st-emotion-cache-1wmy9hl {
                height: 100%;
            }
            
            [data-testid=stVerticalBlock] {
                height: 100%;
            }
        </style>
        """,
        unsafe_allow_html=True
         )
    
    col1, col2 = st.columns([1, 3])  # Ratio of 1:3 for columns

    with col1:
        st.image(r"C:\Users\suraj\Desktop\projects\heart-disease-project\img.png", use_column_width=True)  # Image
    with col2:
        # Description
        st.markdown("""
        <span style="font-size: 20px;">
            Welcome to our Heart Disease Prediction App! Leveraging the power of data science,
            our app provides accurate predictions about the likelihood of heart disease,
            boasting an impressive accuracy rate of 92%.
        </span><br/><br/>
        <span style="font-size: 17px;"> Addressing the challenge of early detection and risk assessment, 
        our tool simplifies the process by analyzing various patient factors to deliver clear predictions.
        Empowering users to take proactive steps towards better heart health, our user-friendly interface allows for easy input of information
        and instant receipt of personalized predictions. By enabling timely intervention through early detection,
        our app aims to improve health outcomes and save lives.
        <br/><br/>
        Fill in the information on the left sidebar and click <span style="font-weight: bold; color: #219C90"> "Predict" </span> to see the result.</span>
    """, unsafe_allow_html=True)
    
    
    # Collect user input for features
    
    user_input = {}
    mappings = {
    'sex': {
        'Female: 0': 0,
        'Male: 1': 1
    },
    'cp': {
        'No Pain: 0': 0,
        'Typical Angina: 1': 1,
        'Atypical Angina: 2': 2,
        'Non-Anginal Pain: 3': 3,
        'Asymptomatic: 4': 4
    },
    'fbs': {
        'False: 0': 0,
        'True: 1': 1
    },
    'restecg': {
        'Normal: 0': 0,
        'ST-T Wave Abnormality: 1': 1,
        'Probable or Definite Left Ventricular Hypertrophy: 2': 2
    },
    'exang': {
        'No: 0': 0,
        'Yes: 1': 1
    },
    'slope': {
        'Upsloping: 1': 1,
        'Flat: 2': 2,
        'Downsloping: 3': 3
    },
    'thal': {
        'Normal: 3': 3,
        'Fixed Defect: 6': 6,
        'Reversible Defect: 7': 7
    }

    }
    for feature in features:
        if feature == 'age':
            user_input[feature] = st.sidebar.number_input('Age in years', value=0)
        elif feature == 'sex':
            user_input[feature] = st.sidebar.selectbox('Sex', options={'Female: 0', 'Male: 1'}, index=1)
        elif feature == 'cp':
            user_input[feature] = st.sidebar.selectbox('Chest Pain Type', options={'No Pain: 0','Typical Angina: 1', 'Atypical Angina: 2', 'Non-Anginal Pain: 3', 'Asymptomatic: 4'}, index=0)
        elif feature == 'trestbps':
            user_input[feature] = st.sidebar.number_input('Resting Blood Pressure (mm Hg)', value=0)
        elif feature == 'chol':
            user_input[feature] = st.sidebar.number_input('Serum Cholestoral (mg/dl)', value=0)
        elif feature == 'fbs':
            user_input[feature] = st.sidebar.selectbox('Fasting Blood Sugar > 120 mg/dl', options={'False: 0', 'True: 1'}, index=0)
        elif feature == 'restecg':
            user_input[feature] = st.sidebar.selectbox('Resting Electrocardiographic Results', options={'Normal: 0', 'ST-T Wave Abnormality: 1', 'Probable or Definite Left Ventricular Hypertrophy: 2'}, index=0)
        elif feature == 'thalach':
            user_input[feature] = st.sidebar.number_input('Maximum Heart Rate Achieved', value=0)
        elif feature == 'exang':
            user_input[feature] = st.sidebar.selectbox('Exercise Induced Angina', options={'No: 0', 'Yes: 1'}, index=0)
        elif feature == 'oldpeak':
            user_input[feature] = st.sidebar.number_input('ST Depression Induced by Exercise Relative to Rest', value=0.0, step=0.1)
        elif feature == 'slope':
            user_input[feature] = st.sidebar.selectbox('Slope of Peak Exercise ST Segment', options={'Upsloping: 1', 'Flat: 2', 'Downsloping: 3'}, index=0)
        elif feature == 'ca':
            user_input[feature] = st.sidebar.number_input('Number of Major Vessels Colored by Flourosopy (0-3)', min_value=0, max_value=3, value=0)
        elif feature == 'thal':
            user_input[feature] = st.sidebar.selectbox('Thal', options={'Normal: 3', 'Fixed Defect: 6', 'Reversible Defect: 7'}, index=0)

    # Predict heart disease based on user input
    
    if st.sidebar.button('Predict'):
        for feature, value in user_input.items():
            if feature in mappings:
                user_input[feature] = mappings[feature][value]
        #st.write(user_input)
        prediction = predict_heart_disease(**user_input)
        if prediction == 1:
            st.markdown('<p style="text-align: center; font-size: 26px; color: red;"><b>The model predicts that the patient has heart disease.</b></p>', unsafe_allow_html=True)
        else:
            st.markdown('<p style="text-align: center; font-size: 26px; color: green;"><b>The model predicts that the patient does not have heart disease.</b></p>', unsafe_allow_html=True)
    # Footer at the bottom
    st.markdown('<hr style="border: 2px solid orange;">', unsafe_allow_html=True)  # Horizontal line
    st.markdown('''
                <footer style="color: orange; display: flex; justify-content: space-between; align-items: center;">
                    <span>Contact: surajpratapsingh9798@gmail.com</span>
                    <span>Developed by: Suraj Singh</span>
                </footer>''', unsafe_allow_html=True)  # Contact information
            
if __name__ == '__main__':
    main()
    