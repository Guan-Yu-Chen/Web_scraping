import requests as req
import json
from bs4 import BeautifulSoup as bs

author_code = ""

url_tainan_1week = f"https://opendata.cwa.gov.tw/fileapi/v1/opendataapi/F-D0047-079?Authorization={author_code}&downloadType=WEB&format=JSON"

res = req.get(url_tainan_1week)

obj = json.loads(res.text)

WeatherInfo = obj["cwaopendata"]["dataset"]["locations"]

time = obj["cwaopendata"]["sent"][0:10]

for area in WeatherInfo["location"]:
    if area["geocode"] == "6703200":
        district = WeatherInfo["locationsName"] + area["locationName"]
        MaxT = area["weatherElement"][3]["time"][0]["elementValue"]["value"]
        MinT = area["weatherElement"][4]["time"][0]["elementValue"]["value"]
        ProbOfRain = area["weatherElement"][9]["time"][0]["elementValue"]["value"]
        weather = area["weatherElement"][12]["time"][0]["elementValue"][0]["value"]


print(f"地區 : {district}")
print(f"時間 : {time}")
print(f"溫度 : {MinT}°C - {MaxT}°C") #最高最低
print(f"天氣 : {weather}")
print(f"降雨機率 : {ProbOfRain} %")
