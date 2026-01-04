import streamlit as st          # Import Streamlit for building the web app
import pandas as pd             # Import Pandas for data handling
import joblib                   # Import Joblib to load the pre-trained model


# Load the trained fraud detection model/pipeline
model = joblib.load('fraud_detection_pipeline.pkl')


# Title of the web app
st.title('Fraud Detection Prediction App 👮🏽')


# A short description to guide the user
st.markdown('Please enter the transaction details and use the predict button')


# A visual divider for better UI separation
st.divider()


# Dropdown for selecting type of transaction
transaction_type = st.selectbox(
    'Transaction Type', 
    ['PAYMENT', 'TRANSFER', 'CASH_OUT', 'CASH_IN', 'DEBIT']
)


# Input field to enter transaction amount (default = 1000)
amount = st.number_input('Amount', min_value=0.0, value=1000.0)


# Sender's old balance input (default = 10000)
oldbalanceOrg = st.number_input('Old Balance (Sender)', min_value=0.0, value=10000.0)


# Sender's new balance input after transaction (default = 9000)
newbalanceOrig = st.number_input('New Balance (Sender)', min_value=0.0, value=9000.0)


# Receiver's old balance (default = 0)
oldbalanceDest = st.number_input('Old Balance (Receiver)', min_value=0.0, value=0.0)


# Receiver's new balance (default = 0)
newbalanceDest = st.number_input('New Balance (Receiver)', min_value=0.0, value=0.0)


# Run this block when the user clicks the Predict button
if st.button('Predict'):
    
    # Create a dataframe with a single row of the provided input values
    input_data = pd.DataFrame([{
        'type' : transaction_type,
        'amount' : amount,
        'oldbalanceOrg' : oldbalanceOrg,
        'newbalanceOrig' : newbalanceOrig,
        'oldbalanceDest' : oldbalanceDest,
        'newbalanceDest' : newbalanceDest
    }])
    
    # Use the loaded model to predict fraud (0 = not fraud, 1 = fraud)
    prediction = model.predict(input_data)[0]
    
    # Show raw numeric prediction result
    st.subheader(f"Prediction: '{int(prediction)}'")
    
    # Interpret the result: Fraud or Not Fraud
    if prediction == 1:
        st.error('This Transaction can be fraud')     # Red-colored warning message
    else: 
        st.success('This transaction looks like it is not a fraud')  # Green success message
