
import requests

url = 'http://0.0.0.0:8000/v1/sentiment'

response = requests.get(url)

print(response)

# link = "https://ousadia-api.herokuapp.com/v1/sentiment"

# print(link.get)