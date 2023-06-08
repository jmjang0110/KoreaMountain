import requests
import json
from Data.DataManager import *

class WEATHER_DATA_TYPE:
    NAME            = 'name'
    WEATHER_DESC    = 'weather'
    TEMP            = 'temp'
    FEELS_LIKE      = 'feels_like'
    TEMP_MIN        = 'temp_min'
    TEMP_MAX        = 'temp_max'
    HUMIDITY        = 'humidity'
    PRESSURE        = 'pressure'
    WIND_DEG        = 'deg'
    WIND_SPEED      = 'speed'


class OpenWeatherAPI:
    def __init__(self):

        #city = "Seoul"
        #api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}"

        self.lat = ''
        self.lon = ''
        self.Url = f"http://api.openweathermap.org/data/2.5/weather?&units=metric&lat={self.lat}&lon={self.lon}&appid={self.apikey}"

        self.result = requests.get(self.Url)
        # json 타입으로 변환
        self.data = json.loads(self.result.text)


    def UpdateData(self, lat, lon):
        self.lat    = lat
        self.lon    = lon
        self.Url    = f"http://api.openweathermap.org/data/2.5/weather?&units=metric&lat={self.lat}&lon={self.lon}&appid={self.apikey}"
        self.result = requests.get(self.Url)
        self.data   = json.loads(self.result.text)

    def GetData(self, WeatherDataType):
        if WeatherDataType == WEATHER_DATA_TYPE.NAME:
            return self.data[WeatherDataType] 
        if WeatherDataType == WEATHER_DATA_TYPE.WEATHER_DESC:
            return self.data[WeatherDataType][0]['description']
        if WeatherDataType == WEATHER_DATA_TYPE.TEMP:
            return self.data['main'][WeatherDataType] 
        if WeatherDataType == WEATHER_DATA_TYPE.FEELS_LIKE:
            return self.data['main'][WeatherDataType] 
        if WeatherDataType == WEATHER_DATA_TYPE.TEMP_MIN:
            return self.data['main'][WeatherDataType]  
        if WeatherDataType == WEATHER_DATA_TYPE.TEMP_MAX:
            return self.data['main'][WeatherDataType]  
        
        if WeatherDataType == WEATHER_DATA_TYPE.HUMIDITY:
            return self.data['main'][WeatherDataType]  
        if WeatherDataType == WEATHER_DATA_TYPE.PRESSURE:
            return self.data['main'][WeatherDataType]  
       
        if WeatherDataType == WEATHER_DATA_TYPE.WIND_DEG:
            return self.data['wind'][WeatherDataType]  
        if WeatherDataType == WEATHER_DATA_TYPE.WIND_SPEED:
            return self.data['wind'][WeatherDataType]  
        
    def ShowData(self):
        print(self.data["name"],"의 날씨입니다.")
        print("날씨는 ",self.data["weather"][0]["description"],"입니다.")
        print("현재 온도는 ",self.data["main"]["temp"],"입니다.")
        print("하지만 체감 ",self.data["main"]["feels_like"],"일 거에요.")
        print("최저 기온은 ",self.data["main"]["temp_min"],"입니다.")
        print("최고 기온은 ",self.data["main"]["temp_max"],"입니다.")
        print("습도는 ",self.data["main"]["humidity"],"입니다.")
        print("기압은 ",self.data["main"]["pressure"],"입니다.")
        print("풍향은 ",self.data["wind"]["deg"],"입니다.")
        print("풍속은 ", self.data["wind"]["speed"],"입니다.")
            