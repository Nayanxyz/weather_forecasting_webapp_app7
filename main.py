import streamlit as st


st.title("Weather forecasting for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", max_value=5 , min_value=1, help="select number of forecasted days")
option = st.selectbox("select date to view: ", ("Temperature" , "Sky") )

st.subheader(f"{option} for the next {days} days in {place}")