import requests

from bs4 import BeautifulSoup

req = requests.get("https://www.naver.com/")

soup=BeautifulSoup(req.text, 'html.parser')

b=soup.find_all("span", {'class', 'ah_k' } )

idx = 1
for i in b:
    print(str(idx) + '위' + i.text)
    idx += 1