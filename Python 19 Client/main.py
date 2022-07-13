import requests
import json

url = 'http://127.0.0.1:5000/add_record'
data = {'my_column': 'value1 ąčęėįšųūž'}
response = requests.post(url, data=data)
print(type(json.loads(response.text)))

print(response.status_code)
