import requests
from bs4 import BeautifulSoup
import pprint

adres_strony = 'https://wallpaperlist.com'
zrodlo_strony = requests.get(adres_strony).content

parser = BeautifulSoup(zrodlo_strony, "html.parser")

obrazki = parser.find_all("img")

for obraz in obrazki:
    adres_obrazka = adres_strony + obraz["src"]
    print(adres_obrazka)
    dane_obrazka = requests.get(adres_strony).content
