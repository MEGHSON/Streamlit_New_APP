import streamlit as st
import pandas as pd

uploaded = st.file_uploader("Upload the CSV", type="csv")

if uploaded is not None :
    df = pd.read_csv(uploaded)

    number_students = df.shape[0]
    average_age = df["age"].mean()

    col1, col2, col3 = st.columns(3) 

    with col1:
        st.metric("Avergage Age", round(average_age,2), delta= 20)


    with col2:
        st.metric("Number of Students", number_students)
    
    # st.metric("Number of Students", number_students)
    
   
    st.dataframe(df)

else:
    st.info("Please upload a csv filr to display it's contents.")

