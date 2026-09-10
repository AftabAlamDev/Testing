


import streamlit as st
import joblib 

model = joblib.load("plr.joblib")
poly = joblib.load("poly.joblib")

st.title("Icream Sale Unit Predicter")

temp = st.text_input("Temperature", placeholder = "write your temperature : ")


if st.button("predict"):
    new_temp = poly.fit_transform([[float(temp)]])
    prediction = model.predict(new_temp)
    st.write(f"The predicted sale will be == {round(prediction[0])}")

