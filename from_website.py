from bs4 import BeautifulSoup
import requests

class Veri:
    def __init__(self,url) -> None:
        self.url=url
        self.html=requests.get(self.url).content
        self.soup=BeautifulSoup(self.html,"html.parser")
        Veri.veriGetir(self)

    def veriGetir(self):
        getir=self.soup.select("div.day-detail >ul>li>div")
        isim=self.soup.select("div.day-detail >ul>li>div>span:nth-child(2)")
        for a,b in zip(getir,isim):
            tarih=(a.span.text)
            derece=(b.text)
            print(f"İsimler > {tarih} Derece > {derece}")

    
Veri("https://www.haberturk.com/havadurumu/Turkiye-TR/Istanbul/LTSI")