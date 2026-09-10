


import streamlit as st
import joblib 

model = joblib.load("/Users/cbitss/Aftab/Cbitss/6_PM_Agentic_AI/ML/plr.joblib")
poly = joblib.load("/Users/cbitss/Aftab/Cbitss/6_PM_Agentic_AI/ML/poly.joblib")

st.title("Icream Sale Unit Predicter")

temp = st.text_input("Temperature", placeholder = "write your temperature : ")


if st.button("predict"):
    new_temp = poly.fit_transform([[float(temp)]])
    prediction = model.predict(new_temp)
    st.write(f"The predicted sale will be == {round(prediction[0])}")

