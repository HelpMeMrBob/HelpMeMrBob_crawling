import requests
from bs4 import BeautifulSoup

response = requests.get("https://place.map.kakao.com/2043521087")
html = response.text
soup = BeautifulSoup(html, 'html.parser')
print(soup)
