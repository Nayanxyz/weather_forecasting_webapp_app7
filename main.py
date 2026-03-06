import streamlit as st
import plotly.express as px


st.title("Weather forecasting for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", max_value=5 , min_value=1, help="select number of forecasted days")
option = st.selectbox("select date to view: ", ("Temperature" , "Sky") )

st.subheader(f"{option} for the next {days} days in {place}")

def get_data(days):                                     #temporary dates and temperatures to sync slider with line graph

    dates = ["2026-05-02", "2026-05-03", "2026-05-04"]
    temperatures = [10, 12, 15]
    temperatures = [days*i for i in temperatures ]
    return dates , temperatures
d, t = get_data(days)

figure = px.line(x=d, y=t , labels={"x": "Dates", "y": "Temperature(C)"})                     #plotly data frame for  graphs
st.plotly_chart(figure)