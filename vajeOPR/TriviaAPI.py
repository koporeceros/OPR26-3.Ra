import requests
import pprint
urlTrivia = "https://opentdb.com/api.php?amount=10&type=multiple"


kt = requests.get(urlTrivia).json()

rez = kt["results"]

print(len(rez))
pprint.pprint(kt["results"][0])