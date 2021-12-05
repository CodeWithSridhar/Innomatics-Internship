import streamlit as st
import pandas as pd

st.title("Basic Streamlit application")

st.header("Hello")

st.subheader("Hello World....!")

st.markdown("Good to go :sunglasses: ")

df = pd.read_csv('E:\Innomatics Internship\Streamlit_appli\irisdata\Iris.csv')

st.button("Click here!")

st.dataframe(df)