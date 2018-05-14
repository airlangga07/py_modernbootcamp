# query string is a way to pass data to the server as part of a GET request method
import requests 

url = "https://icanhazdadjoke.com/search"

response = requests.get(
    url, 
    headers={ "Accept": "application/json" }, 
    params={ "term": "cat", "limit": 1 }
)

data = response.json()
print(data['results'])

# print(data['joke'])
# print('status: {}'.format(data['status']))