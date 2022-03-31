
from bs4 import BeautifulSoup
import pandas as pd
import requests
import lxml


headersparam = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}

USER_INPUT = str(input("Yazar ve kitap adı: ")).replace(" ", "+")
SEARCH = "https://www.google.com/search?q=" + USER_INPUT + "+kac+sayfa"
print("Sorgu: ", SEARCH)

r = requests.get(SEARCH, headers=headersparam)
soup = BeautifulSoup(r.content, "lxml", from_encoding="utf-8")

try:
    kitap_adi = soup.find("div", attrs={"class": "iKJnec"}).text
    print("Kitap Bilgisi: ", kitap_adi)
except AttributeError:
    kitap_adi = ''
kunye = soup.find_all("div", attrs={"class": "Crs1tb"})


td_dict = dict()
for i in range(len(kunye)):
    tds = kunye[i].find_all("td")
    for j in range(len(tds)):
        if tds[j].text ==  "Sayfa Sayısı:":
            print("Sayfa sayısı: %s" % tds[j + 1].text)







