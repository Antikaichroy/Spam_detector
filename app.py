import streamlit as st
import pickle

# Load your pre-trained model
with open('C:\\Users\\HP\\spam_model.pkl', 'rb') as file:
    model = pickle.load(file)


# Define the Streamlit app
st.title('Spam Email Classifier')

st.write("""
This app predicts whether an email is spam or not.
""")

# Input text box for the email
user_input = st.text_area('Enter the email content')

# Prediction
if st.button('Predict'):
    input_data = [user_input]
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.write("It is a spam")
    else:
        st.write("It is not a spam, the mail is fine.")
