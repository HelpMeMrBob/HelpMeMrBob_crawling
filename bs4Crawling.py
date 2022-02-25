import requests
from bs4 import BeautifulSoup

# 크롤링은 성공. 그러나 kakao map에서 막아둔 부분이 많다.
response = requests.get("https://place.map.kakao.com/2043521087")
html = response.text
soup = BeautifulSoup(html, 'html.parser')
print(soup)
