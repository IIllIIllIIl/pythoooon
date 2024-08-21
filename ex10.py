import requests #pip install requests
city_name = '울산'
API_key = '4838c172caac1cab38c75284fc1fcd68'
limit = 5
url = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit={limit}&appid={API_key}'
res=requests.get(url)
data = res.json()
print(len(data))
lat= data[0]['lat']
lon= data[0]['lon']
print(lat, lon)
url=f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}'
weather = requests.get(url)
weather_data = weather.json()
temp = weather_data['main'][0]['temp']
print(temp)



