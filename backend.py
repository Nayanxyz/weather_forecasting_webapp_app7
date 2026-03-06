import requests


API_KEY = "422daebb066f79393c16f0423f3467bn8"

def get_data(place, forecast_day=None):
    """ we have ["list"] key from debugger that has all the keys and dictionaries .
        we have 5 days of forecast with 3 hour difference , that means we have 8 temperatures in one day .
    """

    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"

    response = requests.get(url)

    data = response.json()

    filtered_data = data["list"]

    number_values = 8 * forecast_day                                      # 8* forecast day will give us temps or sky

    filtered_data = filtered_data[:number_values]                          #from 0 day to no. of forecast days

    return filtered_data

if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_day=2, kind="Temperature"))