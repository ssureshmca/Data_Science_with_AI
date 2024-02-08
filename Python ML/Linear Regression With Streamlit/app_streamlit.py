# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 11:40:32 2019

@author: Omkar Nallagoni
"""




import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("linear_wine_model.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(fixed_acidity, volatile_acidity, citric_acid, 
                                residual_sugar,chlorides, free_sulfur_dioxide, 
                                total_sulfur_dioxide, density,
                                pH, sulphates, alcohol):
   
    prediction=classifier.predict([[fixed_acidity, volatile_acidity, citric_acid, 
                                residual_sugar,chlorides, free_sulfur_dioxide, 
                                total_sulfur_dioxide, density,
                                pH, sulphates, alcohol]])
    print(prediction)
    return prediction



def main():
    st.title("Wine quality")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Wine quality ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    fixed_acidity = st.text_input("fixed_acidity","Type Here")
    volatile_acidity = st.text_input("volatile_acidity","Type Here")
    citric_acid = st.text_input("citric_acid","Type Here")
    residual_sugar = st.text_input("residual_sugar","Type Here")
    chlorides = st.text_input("chlorides","Type Here")
    free_sulfur_dioxide = st.text_input("free_sulfur_dioxide","Type Here")
    total_sulfur_dioxide = st.text_input("total_sulfur_dioxide","Type Here")
    density = st.text_input("density","Type Here")
    pH = st.text_input("pH","Type Here")
    sulphates = st.text_input("sulphates","Type Here")
    alcohol = st.text_input("alcohol","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(eval(fixed_acidity), eval(volatile_acidity), eval(citric_acid), 
                                           eval(residual_sugar),eval(chlorides), eval(free_sulfur_dioxide), 
                                           eval(total_sulfur_dioxide), eval(density),
                                           eval(pH), eval(sulphates), eval(alcohol))
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("This is about wine qulaity")

if __name__=='__main__':
    main()
    
    
    