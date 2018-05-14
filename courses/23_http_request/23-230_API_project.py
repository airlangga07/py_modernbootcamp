from random import choice
import requests
from pyfiglet import figlet_format
from termcolor import colored

header = figlet_format("DAD JOKE 3000!")
header = colored(header, color="magenta")
print(header)

term = input("What would you like to search for? ")
url = "https://icanhazdadjoke.com/search"

response = requests.get(
    url, 
    headers={ "Accept": "application/json" },
    params={ "term": term }
).json()

# get the total number of jokes
num_jokes = response['total_jokes']
# get the results
results = response['results']

if num_jokes > 1:
    print("I found {} jokes about {}. Here's one: ".format(num_jokes, term))
    print(choice(results)['joke'])
elif num_jokes == 1:
    print("I found one joke about {}, here it is: ".format(term))
    print(results[0]['joke'])
else:
    print("Sorry, couldn't find a joke with your term: {}".format(term))
    