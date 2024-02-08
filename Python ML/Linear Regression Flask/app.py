"""
Created on Fri Nov 14 2019

@author: Omkar Nallagoni
"""


import numpy as np
import pickle
import pandas as pd
from flask import Flask, request

#model.pkl is used to get the predictions on new data
# in this page np pd pickle we did not used it is masked
# yellow error 


app=Flask(__name__)

pickle_in = open("linear_wine_model.pkl","rb")
classifier=pickle.load(pickle_in)


@app.route('/')      # decorator
def welcome():
    return "Welcome All"


@app.route('/predict',methods=["Get"])
def predict_note_authentication():

    """
    ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
     'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
     'pH', 'sulphates', 'alcohol']
   """
    input_cols=['fixed acidity', 'volatile acidity', 'citric acid', 
                'residual sugar','chlorides', 'free sulfur dioxide', 
                'total sulfur dioxide', 'density',
                'pH', 'sulphates', 'alcohol']
    list1=[]
    for i in input_cols:
        val=request.args.get(i)
        list1.append(eval(val))


    prediction=classifier.predict([list1])

    #prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return "Hello The answer is"+str(prediction)



@app.route('/predict_file',methods=["POST"])
def predict_note_file():
    df_test=pd.read_csv(request.files.get("file"))  # whatever name you written here the same name will provide in Post man
    prediction=classifier.predict(df_test)
    return str(list(prediction))

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000)