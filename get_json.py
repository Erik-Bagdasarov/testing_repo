import json
import requests
import pandas as pd

response = requests.get('https://jsonplaceholder.typicode.com/posts')

data = response.json()

json_data = json.dumps(data, indent=4)
# print(json_data)

print(json.dumps(data, indent=4))
# df = pd.DataFrame(data)
# print(df)

# df.to_csv('data_2.csv', index=False)