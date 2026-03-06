import streamlit as st
import plotly.express as px
from backend import get_data


st.title("Weather forecasting for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", max_value=5 , min_value=1, help="select number of forecasted days")
option = st.selectbox("select date to view: ", ("Temperature" , "Sky") )

st.subheader(f"{option} for the next {days} days in {place}")

if place:
    try:

        filtered_data = get_data(place, days)

        if option == "Temperature":

            temperatures = [dict["main"]["temp"] / 10 for dict in filtered_data ]    # from dictionary we get main dictionary, and
                                                                                # from main dictionary we get temp key
            dates = [dict["dt_txt"] for dict in filtered_data ]

            figure = px.line(x=dates, y=temperatures , labels={"x": "Dates", "y": "Temperature(C)"})

            st.plotly_chart(figure)                                             #plotly data frame for  graphs

        if option == "Sky":

            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}

            sky_conditions = filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
                                                                                # dict weather has a list main ,
                                                                                # that is why we have [0] to select list
                                                                                # and then select main key
            image_paths = [images[condition] for condition in sky_conditions]

            st.image(image_paths , width=115)                                   #to add images
    except KeyError:
        st.write("This place does not exist")