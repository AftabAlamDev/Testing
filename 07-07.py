

# run command
# streamlit run filename.py
# python -m run filename.py


# pip install streamlit

# python -m pip install streamlit

import streamlit as st
from db import MYSQL, host, user, password

db = MYSQL(host=host, user=user, password=password)


st.title("REGISTRATION FORM")


name = st.text_input(label = "Name" ,placeholder = "Enter your name : ")
age = st.text_input(label = "Age" ,placeholder = "Enter your age : ")
gender = st.text_input(label = "Gender" ,placeholder = "Enter your gender : ")
city = st.text_input(label = "City" ,placeholder = "Enter your city : ")
email = st.text_input(label = "Email" ,placeholder = "Enter your email : ")



if st.button("submit"):
    db.create_db(db_name="R_FORM")
    st.write(db.create_tb(db_name = "R_FORM", tb_name = "STUDENT"))
    db.insert_value(db_name = "R_FORM", tb_name = "STUDENT", name=name, age=age, gender=gender, city=city, email=email)
    st.success("form submitted successful", icon = "✅")