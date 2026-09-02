
import streamlit as st
import joblib 
from db import MYSQL

# model = joblib.load("/Users/cbitss/Aftab/Cbitss/11_AM_Python/ML/student_performance.joblib")

M1 = 2.85341642
M2 = 1.01908539
M3 = (-0.58000266)
M4 = 0.47114094
M5 = 0.18952435
C = (-33.454137689415)

db = MYSQL("Aftab@786")

name = st.text_input(label = "Student Name", placeholder = "enter your name : ")

class_name = st.text_input(label = "Class Name", placeholder = "enter your class name : ")

Hours_studed = st.text_input(label = "Hour Studied", placeholder = "how many hour you studied : ")

previous_Scores = st.text_input(label = "Previous Score", placeholder = "enter your previous score : ")

Extra_curicular_activities = st.selectbox(label = "ExtraCuricular Activities", options=["Yes", "No"], placeholder = "anything extra you do : ")

Sleep_hour = st.text_input(label = "Sleep Hours", placeholder = "how many hours you sleep : ")

Sample_question = st.text_input(label = "Sample Question Paper", placeholder = "how many sample question paper you solved : ")

extra = {"Yes" : 1, "No" : 0}


if st.button("Check Score"):
    # prediction = model.predict([[int(Hours_studed), int(previous_Scores), int(extra[Extra_curicular_activities]), int(Sleep_hour), int(Sample_question)]])
    # st.write(f"the predicted score == {round(prediction[0])}%")
    db.create_db()
    db.create_table()
    output = M1 * int(Hours_studed) + M2 * int(previous_Scores) + M3 * int(extra[Extra_curicular_activities]) + M4 * int(Sleep_hour) + M5 * int(Sample_question) + C
    db.insert_value(name, class_name, Hours_studed, previous_Scores, Extra_curicular_activities, Sleep_hour, Sample_question, round(output))
    st.success("performance predicted", icon = "✅")
    st.write(f"the predicted score == {round(output)}")
    st.write("data stored in sql")