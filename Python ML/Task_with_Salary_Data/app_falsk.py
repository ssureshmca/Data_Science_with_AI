import pickle
from flask import Flask, request

app=Flask(__name__)

pickle_in = open("linear_salary_model.pkl","rb")
classifier=pickle.load(pickle_in)


@app.route('/')      # decorator
def welcome():
    return "Welcome All"


@app.route('/predict',methods=["Get"])
def predict_note_authentication():
    val=request.args.get("YearsExperience")
    list1=[]
    list1.append(eval(val))
    prediction=classifier.predict([list1])
    print(prediction)
    return "The Salary Prediction is : "+str(prediction)

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000)