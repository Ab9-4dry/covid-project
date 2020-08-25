import requests

link = 'https://api.covidindiatracker.com/total.json'

response = requests.get(link)

res_json = response.json()

print(res_json['active'])