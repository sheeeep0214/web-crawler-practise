import requests
from bs4 import BeautifulSoup
yt=requests.get("https://www.books.com.tw/web/books/?loc=menu_1_001p")
print(yt)
soup=BeautifulSoup(yt.text,"html.parser")
s=soup.findAll("h4")
for i in s:
    print(i.a.string)