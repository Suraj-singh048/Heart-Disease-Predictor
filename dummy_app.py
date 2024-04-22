import streamlit as st
import pickle
import pandas as pd

# Customizing Streamlit appearance
st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="💓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load the trained model
model = pickle.load(open('gs-log-reg.model', 'rb'))

# Load the dataset
data_file = '6.1 heart-disease.csv'
df = pd.read_csv(data_file)

# Define the features used in the model
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
    #st.markdown('<h1 style="color: red;">Heart Disease Prediction</h1>', unsafe_allow_html=True)
    # Title and subheading at the top
    st.markdown('<h1 style="color: red; text-align: center;">Heart Disease Prediction</h1>', unsafe_allow_html=True)
    st.subheader('Empowering Health Decisions: Predicting Heart Disease with Data Science')
    
    # Main content area with image and description
    col1, col2 = st.columns([1, 3])  # Ratio of 1:3 for columns

    with col1:
        st.image(r"C:\Users\suraj\Desktop\projects\heart-disease-project\img.jpg", use_column_width=True)  # Image
    with col2:
        # Description
        st.markdown("""
            Welcome to our Heart Disease Prediction App! Leveraging the power of data science,
            our app provides accurate predictions about the likelihood of heart disease,
            boasting an impressive accuracy rate of 92%. 
            Addressing the challenge of early detection and risk assessment, 
            our tool simplifies the process by analyzing various patient factors to deliver clear predictions.
            Empowering users to take proactive steps towards better heart health, our user-friendly interface allows for easy input of information
            and instant receipt of personalized predictions. By enabling timely intervention through early detection,
            our app aims to improve health outcomes and save lives.
             
            Fill in the information on the left sidebar and click "Predict" to see the result.
        """)
    
     # Developer's name

    # Collect user input for features
    st.sidebar.subheader('Enter Patient Information')
    user_input = {}
    mappings = {
        'sex': {'Female': 0, 'Male': 1},
        'cp': {'No Pain': 0, 'Typical Angina': 1, 'Atypical Angina': 2, 'Non-Anginal Pain': 3, 'Asymptomatic': 4},
        'fbs': {'False': 0, 'True': 1},
        'restecg': {'Normal': 0, 'ST-T Wave Abnormality': 1, 'Probable or Definite Left Ventricular Hypertrophy': 2},
        'exang': {'No': 0, 'Yes': 1},
        'slope': {'Upsloping': 1, 'Flat': 2, 'Downsloping': 3},
        'thal': {'Normal': 3, 'Fixed Defect': 6, 'Reversible Defect': 7}
    }

    for feature in features:
        if feature == 'age':
            user_input[feature] = st.sidebar.number_input('Age in years', value=0)
        elif feature == 'sex':
            user_input[feature] = st.sidebar.selectbox('Sex', options=['Female', 'Male'])
        elif feature == 'cp':
            user_input[feature] = st.sidebar.selectbox('Chest Pain Type', options=['No Pain', 'Typical Angina', 'Atypical Angina', 'Non-Anginal Pain', 'Asymptomatic'])
        elif feature == 'trestbps':
            user_input[feature] = st.sidebar.number_input('Resting Blood Pressure (mm Hg)', value=0)
        elif feature == 'chol':
            user_input[feature] = st.sidebar.number_input('Serum Cholesterol (mg/dl)', value=0)
        elif feature == 'fbs':
            user_input[feature] = st.sidebar.selectbox('Fasting Blood Sugar > 120 mg/dl', options=['False', 'True'])
        elif feature == 'restecg':
            user_input[feature] = st.sidebar.selectbox('Resting Electrocardiographic Results', options=['Normal', 'ST-T Wave Abnormality', 'Probable or Definite Left Ventricular Hypertrophy'])
        elif feature == 'thalach':
            user_input[feature] = st.sidebar.number_input('Maximum Heart Rate Achieved', value=0)
        elif feature == 'exang':
            user_input[feature] = st.sidebar.selectbox('Exercise Induced Angina', options=['No', 'Yes'])
        elif feature == 'oldpeak':
            user_input[feature] = st.sidebar.number_input('ST Depression Induced by Exercise Relative to Rest', value=0.0, step=0.1)
        elif feature == 'slope':
            user_input[feature] = st.sidebar.selectbox('Slope of Peak Exercise ST Segment', options=['Upsloping', 'Flat', 'Downsloping'])
        elif feature == 'ca':
            user_input[feature] = st.sidebar.number_input('Number of Major Vessels Colored by Fluoroscopy (0-3)', min_value=0, max_value=3, value=0)
        elif feature == 'thal':
            user_input[feature] = st.sidebar.selectbox('Thal', options=['Normal', 'Fixed Defect', 'Reversible Defect'])

    # Predict heart disease based on user input
    if st.sidebar.button('Predict'):
        for feature, value in user_input.items():
            if feature in mappings:
                user_input[feature] = mappings[feature][value]

        prediction = predict_heart_disease(**user_input)
        if prediction == 1:
            st.markdown('<p style="color: red; text-align: center;"><b>The model predicts that the patient has heart disease.</b></p>', unsafe_allow_html=True)
        else:
            st.markdown('<p style="color: green; text-align: center;"><b>The model predicts that the patient does not have heart disease.</b></p>', unsafe_allow_html=True)
    

    # Footer at the bottom
    st.markdown('<hr style="border: 2px solid #add8e6;">', unsafe_allow_html=True)  # Horizontal line
    st.markdown('''
                <div style="color: #add8e6; display: flex; justify-content: space-between; align-items: center;">
                    <span>Contact: your_email@example.com</span>
                    <span>Developed by: Your Name</span>
                </div>''', unsafe_allow_html=True)  # Contact information

if __name__ == '__main__':
    main()


