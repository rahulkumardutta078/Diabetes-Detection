import streamlit as st
import numpy as np
import pandas as pd
import pickle
diabetes_predictor_model=pickle.load(open('diabetes_predictor.sav','rb'))

def predict(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    prediction=diabetes_predictor_model.predict(input_data_reshaped)
    
    if prediction[0]==0:
        
        return "You are not suffering from diabetes"
        
    else:
        
        return "You are suffering from diabetes"



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
        result=predict([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])

        st.success(result)
        
        st.write("Click This [ To book doctor appointment online](https://www.practo.com/doctors)")

if __name__=='__main__':
    main()
