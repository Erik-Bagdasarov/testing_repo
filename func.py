import requests
from apikey import API_TOKEN
import json
import pandas as pd

params = {'q': 'Moscow', 'appid': API_TOKEN, 'units': 'metric'}

response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params)
print(response.status_code)

data = response.json()

json_data = json.dumps(data, indent=4)

df = pd.DataFrame({
    'name': data['name'],
    'temp': data['main']['temp'],
    'feels_like': data['main']['feels_like'],
    'min_temp': data['main']['temp_min'],
    'max_temp': data['main']['temp_max']
}, index=[0])

print(df)
df.to_csv('/Users/erikbagdasarov/PycharmProjects/traning/de_stepik/data.csv', index=False)
