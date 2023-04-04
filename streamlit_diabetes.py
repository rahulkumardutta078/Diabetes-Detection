import streamlit as st
import numpy as np
import pandas as pd
import pickle
diabetes_predictor_model=pickle.load(open('diabetes_predictor.pickle','rb'))

def predict(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age):
    prediction=diabetes_predictor_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])

    if prediction==0:
        result_var="not suffering from diabetes"
        return result_var
        
    elif prediction==1:
        result_var="suffering from diabetes"
        return result_var



def main():
    st.title("Diabetes Prediction System")

    Pregnancies=st.text_input("Pregnancies")
    Glucose=st.text_input("Glucose")
    BloodPressure=st.text_input("BloodPressure")
    SkinThickness=st.text_input("SkinThickness")
    Insulin=st.text_input("Insulin")
    BMI=st.text_input("BMI")
    DiabetesPedigreeFunction=st.text_input('DiabetesPedigreeFunction')
    Age=st.text_input("Age")

    result=""
    if st.button("Predict"):
        result=predict(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)

        st.success("You are {}".format(result))
        
        st.write("Click This [ To book doctor appointment online](https://www.practo.com/doctors)")

if __name__=='__main__':
    main()
