"""
Girilen yazar ve kitap adına göre
kitabın kaç sayfa olduğunu döndürür.
"""
import requests
import sys
from bs4 import BeautifulSoup

headers_param = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}

print("Kaç-Sayfa".center(50, '-'))
print("""Hoşgeldiniz. Lütfen kaç sayfa olduğunu
öğrenmek istediğiniz kitabın adını ve daha tutarlı
bilgi gelmesi için yazar adını da giriniz. 
Ardından program sizin için arama yapacaktır.

Programdan çıkmak için 0 yazmanız yeterlidir.""")
print("-" * 50)

while True:
    USER_INPUT = str(input("Yazar ve Kitap Adı: ")).replace(" ", "+")
    if USER_INPUT == "0":
        print("Hoşçakalın!")
        sys.exit("-" * 50)

    SEARCH = "https://www.google.com/search?q=" + USER_INPUT + "+kac+sayfa"
    print("Sorgu\t\t  : " + SEARCH)

    response = requests.get(SEARCH, headers=headers_param)
    soup = BeautifulSoup(response.content, "lxml", from_encoding="utf-8")

    BOOK_INFORMATION_FLAG = False
    PAPER_FLAG = False

    try:
        book_name = soup.find("div", attrs={"class": "iKJnec"}).text
        KITAP_FLAG = True
        print("Kitap Bilgisi\t  : " + book_name)
    except AttributeError:
        print("Kitap Bilgisi\t  :", None)

    book_information = soup.find_all("div", attrs={"class": "Crs1tb"})

    for i, _ in enumerate(book_information):
        tds = book_information[i].find_all("td")
        for j, _ in enumerate(tds):
            if tds[j].text in  ("Sayfa Sayısı:", "Sayfa", "Sayfa Sayısı"):
                book_paper = tds[j + 1].text
                PAPER_FLAG = True
                print("Sayfa Sayısı\t  : " + book_paper)

    if BOOK_INFORMATION_FLAG is False and PAPER_FLAG is False:
        print('Kitap bilgisi bulunamadı..')
    print("-" * 50)
