from urllib import response
import requests

API_KEY = "1b227106b49687b6d35bfbd5bc16293e"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()

    weather = data['weather'][0]['description']
    print("Weather is: ", weather)

    temperature = round(data['main']['temp']-273.15, 2)  #Kelvin to celcius
    print("Temperature is: ", temperature)

else:
    print("An Error occured")


