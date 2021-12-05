import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Basic Streamlit application")

st.header("Pcactice using Iris Dataset")

st.markdown("Good to go :sunglasses: ")

df = pd.read_csv('E:\Innomatics Internship\Streamlit_appli\irisdata\Iris.csv')

click = st.button("Click here to expand!")
if click == True:
    st.dataframe(df)

check = st.checkbox("click this cheakbox to see the data!!")
if check == True:
    st.dataframe(df)


columns = df.columns
col_name = st.selectbox("Choose a column", columns)
if st.checkbox("Display the plot"):
    st.pyplot(sns.displot(df[col_name], kind='hist'))