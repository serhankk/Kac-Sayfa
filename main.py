
from bs4 import BeautifulSoup
import requests
import lxml


headersparam = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}

USER_INPUT = str(input("Yazar ve Kitap Adı: ")).replace(" ", "+")
SEARCH = "https://www.google.com/search?q=" + USER_INPUT + "+kac+sayfa"
print("Sorgu\t\t  : " + SEARCH)

r = requests.get(SEARCH, headers=headersparam)
soup = BeautifulSoup(r.content, "lxml", from_encoding="utf-8")

BOOK_INFORMATION_FLAG = False
PAPER_FLAG = False

try:
    book_name = soup.find("div", attrs={"class": "iKJnec"}).text
    KITAP_FLAG = True
    print("Kitap Bilgisi\t  : " + book_name)
except AttributeError:
    book_name = None
    print("Kitap Bilgisi\t  :", book_name)

book_information = soup.find_all("div", attrs={"class": "Crs1tb"})

for i in range(len(book_information)):
    tds = book_information[i].find_all("td")
    for j in range(len(tds)):
        if tds[j].text ==  "Sayfa Sayısı:":
            book_paper = tds[j + 1].text
            PAPER_FLAG = True
            print("Sayfa Sayısı\t  : %s" % book_paper)

if BOOK_INFORMATION_FLAG == False and PAPER_FLAG == False:
    print('Kitap bilgisi bulunamadı..')








