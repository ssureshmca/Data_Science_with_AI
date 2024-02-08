import pickle
import streamlit as st 

pickle_in = open("linear_salary_model.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(YearsExperience):   
    prediction=classifier.predict([[YearsExperience]])
    print(prediction)
    return prediction

def main():
    st.title("Salary")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Wine Salary ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Years_Experience = st.text_input("Years_Experience","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(eval(Years_Experience))
    st.success('The output is : {}'.format(result))

if __name__=='__main__':
    main()
