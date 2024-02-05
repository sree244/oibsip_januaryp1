# This code is for checking the weather conditions like humidity, temperature, and description of weather in a city.

import requests
import json

API_key='6c17906d3117425660ac059320d3ada1'
city_name=input("Enter city name:")
url=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'

response=requests.get(url)

if response.status_code == 200:
    data=response.json()
    print("weather is: ",data['weather'][0]['description'])
    print("current temperature is: ",data['main']['temp'])
    print("current temperature feels like: ",data['main']['feels_like'])
    print("current Humidity is: ",data['main']['humidity'])
