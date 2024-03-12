# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 11:10:52 2024

@author: Harshal
"""

import pickle
import streamlit as st

pickle_in = open("model_bankruptcy.pkl","rb")
classifier=pickle.load(pickle_in)


st.title('Bankruptcy :bank:')

st.markdown('This model gives the prediction of bankruptcy :money_with_wings:')


def predict_bankruptcy(features):
    prediction = classifier.predict([features])[0]
    result_mapping = {0: 'Bankruptcy', 1: 'Non-Bankruptcy'}
    return result_mapping.get(prediction, 'Unknown')

def main():
    st.title("Bankruptcy Detector")
    st.markdown("""
        <div style="background-color: tomato; padding: 10px">
            <h2 style="color: white; text-align: center;">Streamlit Bankruptcy Detector</h2>
        </div>
    """, unsafe_allow_html=True)

    # Input features
    features = {
        "industrial_risk": st.text_input("Industrial Risk", "Type Here"),
        "management_risk": st.text_input("Management Risk", "Type Here"),
        "financial_flexibility": st.text_input("Financial Flexibility", "Type Here"),
        "credibility": st.text_input("Credibility", "Type Here"),
        "competitiveness": st.text_input("Competitiveness", "Type Here"),
        "operating_risk": st.text_input("Operating Risk", "Type Here"),
    }

    result = ""
    if st.button("Predict"):
        # Convert text inputs to floats and handle invalid inputs
        try:
            features = {key: float(value) for key, value in features.items()}
            result = predict_bankruptcy(list(features.values()))
        except ValueError:
            st.error("Please enter valid numerical values for all input features.")

    st.success(f'The output is {result}')

    if st.button("About"):
        st.text("Let's Learn")
        st.text("Built with Streamlit")

if __name__ == '__main__':
    main()