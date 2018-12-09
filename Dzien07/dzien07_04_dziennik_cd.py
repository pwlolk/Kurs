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

import pickle

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
    lista=[]
    lista.append(stare_wpisy)
    lista.append(nowy_wpis)
    plik_dz.seek(0)
    pickle.dump(lista,plik_dz) #NADPISUJE NAM PLIKI, TEGO NIE CHCEMY, TZN. CHCEMY ALE Z UZUPEŁNIONĄ O WPIS LISTĄ

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
        print(dane)
        return dane
    except:
        print("Błąd")

def zapytaj():
    decyzja = input("Wybierz opcję: ") #KONTROLER (a po niegdysiejszemu mojemu - switch)
    if decyzja == "1":
        print("Wpisy: ")
        plik_dz = otworz_dziennik(plik_dziennika)
        przeczytaj_plik(plik_dz)
        zamknij_dziennik(plik_dz)
    if decyzja == "2":
        print("Dodawanie wpisu...")
        plik_dz = otworz_dziennik(plik_dziennika)
        dodaj_wpis(plik_dz)
        zamknij_dziennik(plik_dz)
    if decyzja == "5": # Pamiętać, że string, więc porównujemy do stringa
        exit()

plik_dziennika = "dziennik.dz"

wyswietl_menu()
zapytaj()

plik_dz = otworz_dziennik(plik_dziennika) #w globalu lepiej przekazywać

zamknij_dziennik(plik_dz) #przekazujemy jako parametr do funckji

# while True: #nieskończona pętla z niczym program czeka i nie kończy się
#     pass