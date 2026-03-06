import requests


API_KEY = "422daebb066f79393c16f0423f3467bn8"

def get_data(place, forecast_day, kind):
    """ we have ["list"] key from debugger that has all the keys and dictionaries .
        we have 5 days of forecast with 3 hour difference , that means we have 8 temperatures in one day .


    """

    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"

    response = requests.get(url)

    data = response.json()

    filtered_data = data["list"]

    number_values = 8 * forecast_day                                      # 8* forecast day will give us temps or sky

    filtered_data = filtered_data[:number_values]                          #from 0 day to no. of forecast days

    if kind == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]          # from dictionary we get main dictionary, and
                                                                                  # from main dictionary we get temp key

    if kind == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]     # dict weather has a list main , that is why we have [0] to select list
                                                                                   # and then select main key

    return filtered_data

if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_day=2, kind="Temperature"))