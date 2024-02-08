import streamlit as st

st.title("Streamlit Application")
html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Wine quality ML App </h2>
    </div>
    """

st.markdown(html_temp,unsafe_allow_html=True)

st.text_input("fixed_acidity","Type Here")

st.button("Predict")

