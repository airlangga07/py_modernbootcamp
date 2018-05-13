import requests

url = "http://www.google.com"

response = requests.get(url)
print(response)
print(response.ok)

# print the headers
print(response.headers)