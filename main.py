import streamlit as st 
import pandas as pd 

st.set_page_config(layout="centered",
                   page_title="Weather Forecast Web App",
                   page_icon=":sun:")


st.title("Weather Forecast For The Next Days")
place=st.text_input("PLACE :-")
days=st.slider('FORECAST DAYS :-', 0, 10 ,key="slider",help="Select the number of days to forcast")
view_type=st.selectbox('Select Data To View', ['Temperature', 'Sky'] , key="view")


st.subheader(f"{view_type} for the next {days} days in {place}")
