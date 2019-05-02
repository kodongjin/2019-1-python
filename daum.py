import requests

from bs4 import BeautifulSoup

req = requests.get("https://www.daum.net/")

soup=BeautifulSoup(req.text, 'html.parser')

b=soup.find_all("span", {'class', 'txt_issue' } )

idx = 1
for i in b:
    print(str(idx) + '위  ' + i.text)
    idx += 0.5
