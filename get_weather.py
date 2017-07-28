from influxdb import InfluxDBClient
from influxdb.client import InfluxDBClientError
import time
import requests
client = InfluxDBClient('localhost', 8086, 'ws_db', 'ws_db', 'ws_db')
client.switch_database('ws_db')
while (1):
    response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Wiesloch,de&APPID=e8accc4a17c161eabbb49a2061e8972c")
    jsonobj = response.json()
    #print (jsonobj)
    t_city = jsonobj['name']
    t_country = jsonobj['sys']['country']
    t_type = jsonobj["weather"][0]
    t_type = t_type['main']
    t_temp = jsonobj['main']['temp'] - 273.15
    t_temp = round (t_temp)
    t_humidity = jsonobj['main']['humidity']
    t_wind = jsonobj['wind']['speed']
    t_wind = round (t_wind)
    timenow = time.asctime (time.localtime(time.time()));
    bjson_body = [
        {
            "measurement": "weather",
            "tags": {
                "city": t_city,
                "country": t_country
            },
            "fields": {
                "type": t_type,
                "temp": t_temp,
                "humidity": t_humidity,
                "wind": t_wind
            }
        }
    ]
    #print (timenow)
    client.write_points(bjson_body)
    #print(bjson_body)
    response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Frankfurt,de&APPID=99174197b1cc56b0e044f0180b76ad92")
    jsonobj = response.json()
    #print (jsonobj)
    t_city = jsonobj['name']
    t_country = jsonobj['sys']['country']
    t_type = jsonobj["weather"][0]
    t_type = t_type['main']
    t_temp = jsonobj['main']['temp'] - 273.15
    t_temp = round (t_temp)
    t_humidity = jsonobj['main']['humidity']
    t_wind = jsonobj['wind']['speed']
    t_wind = round (t_wind)
    timenow = time.asctime (time.localtime(time.time()));
    bjson_body = [
        {
            "measurement": "weather",
            "tags": {
                "city": t_city,
                "country": t_country
            },
            "fields": {
                "type": t_type,
                "temp": t_temp,
                "humidity": t_humidity,
                "wind": t_wind
            }
        }
    ]
    #print (timenow)
    client.write_points(bjson_body)
    #print(bjson_body)
    #print("Write done")
    time.sleep(600)
