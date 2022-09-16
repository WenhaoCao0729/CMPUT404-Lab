
import requests

x = requests.get('http://www.google.com')

print(x.text)