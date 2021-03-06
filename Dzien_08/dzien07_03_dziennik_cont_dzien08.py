# 1. Menu
# 2. Przeglądanie - otwieranie pliku, odczytywanie pliku, zamknięcie
# 3. Dodawanie - otwieranie pliku z uprawnieniami, zapytanie o dane, zapis pliku, zamknięcie
# 4. Usuwanie - otworzyć plik , odnalezienie wpisu do usunięcia, zamknięcie
# 5. WYszukiwanie - otworzyć plik, zapytanie o kryterium, odnalezienie wpisu, wyświetlenie wpisu, zamknięcie
# 6. Wyjście - exit()
#
# Powtarzają się rzeczy, które warto ofunkcjonować: otwarcie, zamknięcie, odnalezienie wpisu.
# Ja nie było piku .dz, to go sobie utowrzył
# W głównym scopie powinno być jak najmniej "logiki biznesowej" (ifów, elsów itd) To wszystko raczej do funckji

import pickle #zaletą pickle'a jest to, że jeżeli ładujemy tam listę, to dostajemy czytając listę, jeżeli słownik to slownik itd.
import smtplib
import pprint #ładnie wyświetla zawartość listy
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def otworz_dziennik(plik_dziennika):
    dziennik = open(plik_dziennika,"rb+") #handler otwartego pliku
    return dziennik # zwrot, żeby inne funkcje mogły korzystać

def zamknij_dziennik(plik_dz):
    plik_dz.close()

def dodaj_wpis(plik_dz): #co chcemy dodać do dziennika?
    data = input("Podaj datę: ")
    tresc = input("Wpisz tresc: ")
    nowy_wpis = {"data":data, "tresc":tresc}
    stare_wpisy = przeczytaj_plik(plik_dz)
    nowe_wpisy = stare_wpisy
    # lista=[]
    # lista.append(stare_wpisy)
    # for i,wpisy in enumerate(stare_wpisy):
    #     lista.append(stare_wpisy[i])
    # lista.append(nowy_wpis)
    # if stare_wpisy == None:
    #     nowe_wpisy = []
    try:
        nowe_wpisy.append(nowy_wpis)
    except:
        print("Nie było żadnego wpisu. Dodaję pierwszy wpis...")
        nowe_wpisy = []
        nowe_wpisy.append(nowy_wpis)
    plik_dz.seek(0)
    pickle.dump(nowe_wpisy,plik_dz) #NADPISUJE NAM PLIKI, TEGO NIE CHCEMY, TZN. CHCEMY ALE Z UZUPEŁNIONĄ O WPIS LISTĄ
    print("Wpis dodany poprawnie.")

def wyslij_mail(temat,tresc):
    # temat = "Ktoś unsunął wpis (PawelO)"
    # tresc = "Usnięto wpis o numerze {}".format(indeks)
    # tresc = tresc + "\na dla uzytkownika jest to wpis numer {}.".format(nr_wpisu)

    mail = MIMEMultipart() #pusty kontener reprezentujący nagłówek wiadomości
    mail["Subject"] = temat
    mail["To"] = "isapy@o2.pl"
    mail["From"] = "isapy@int.pl"

    body = MIMEText(tresc)
    mail.attach(body)

    serwer = smtplib.SMTP("poczta.int.pl")
    serwer.login("isapy@int.pl", "isapython;")
    serwer.send_message(mail)
    serwer.quit()

    print("Wysłano mail!")

def usun_wpis(plik_dz):
    stare_wpisy = przeczytaj_plik(plik_dz)
    length = str(len(stare_wpisy))
    print("W dzienniku jest {} wpisów".format(length))
    w_d_u = int(input("Podaj numer wpisu do usunięcia: "))
    indeks_do_usunięcia = w_d_u-1
    if w_d_u <= len(stare_wpisy) and w_d_u > 0:
        del stare_wpisy[indeks_do_usunięcia]
        plik_dz.seek(0)
        pickle.dump(stare_wpisy, plik_dz)
        print("Właśnie usunąłem wpis.")
        temat = "Ktoś unsunął wpis (PawelO)"
        tresc = "Usnięto wpis o numerze {}".format(indeks_do_usunięcia)
        tresc = tresc + "\na dla uzytkownika jest to wpis numer {}.".format(w_d_u)
        wyslij_mail(temat, tresc)
    else:
        print("Nie ma takiego wpisu.")

def wyszukaj_wpis(tekst,plik_dz):
    stare_wpisy = przeczytaj_plik(plik_dz)
    i = 0
    for wpis in stare_wpisy:
        if tekst in wpis["tresc"]:
            pprint.pprint(wpis)
            i = i+1
    if i > 0:
        print ("Znaleziono " + str(i) +" wpisów")
    if i == 0:
        print("Taki ciąg znaków nie wystepuje.")
        # else:
        #     print("Taki ciąg znaków nie wystepuje.")
        # Jeżeli bez licznika, to mozna ustawić flagę typu False na zanalezienie, któą nawet jedno zanelzienie zmieni na True

def wyswietl_menu():
    print("Dziennik".upper())
    print("Opcje:\n"
          "[1] Wyświetlanie\n"
          "[2] Dodawanie wpisu\n"
          "[3] Usuwanie wpisu\n"
          "[4] Wyszukiwanie\n"
          "[5] Wyjście z dziennika\n")

def przeczytaj_plik(plik_dz):
    try:
        dane = pickle.load(plik_dz)
        return dane
    except:
        print("Błąd")

def zapytaj():
    decyzja = input("Wybierz opcję: ") #KONTROLER (a po niegdysiejszemu mojemu - switch)
    if decyzja == "1":
        print("Wpisy: ")
        plik_dz = otworz_dziennik(plik_dziennika)
        wpisy = przeczytaj_plik(plik_dz)
        # print(wpisy) # Z kursu
        for i,wpis in enumerate(wpisy):
            print("\nNumer wpisu:" + str(i+1) + "\t" + "Data: " + wpisy[i]['data'])
            print("Treść: " + wpisy[i]['tresc']) # Moje
        zamknij_dziennik(plik_dz)
    if decyzja == "2":
        print("Dodawanie wpisu...")
        plik_dz = otworz_dziennik(plik_dziennika)
        dodaj_wpis(plik_dz)
        zamknij_dziennik(plik_dz)
    if decyzja == "3":
        print("\nUsuwanie wpisu...")
        plik_dz = otworz_dziennik(plik_dziennika)
        usun_wpis(plik_dz)
        zamknij_dziennik(plik_dz)
    if decyzja == "4":
        print("\nWyszukiwanie wpisu...")
        tekst = input("Podaj ciąg znaków do odnalezienia w dzienniku: ")
        plik_dz = otworz_dziennik(plik_dziennika)
        wyszukaj_wpis(tekst,plik_dz)
        zamknij_dziennik(plik_dz)
    if decyzja == "5": # Pamiętać, że string, więc porównujemy do stringa
        exit()

plik_dziennika = "dziennik.dz"

while True:
    wyswietl_menu()
    zapytaj()

plik_dz = otworz_dziennik(plik_dziennika) #w globalu lepiej przekazywać
zamknij_dziennik(plik_dz) #przekazujemy jako parametr do funckji

# while True: #nieskończona pętla z niczym program czeka i nie kończy się
#     pass