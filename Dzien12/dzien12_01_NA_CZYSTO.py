import pickle
# import smtplib
import pprint
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
from modul import wyslij_mail

class Dziennik(object):
    def __init__(self, plik_z_naszym_dziennikiem = "dziennik.dz"):     # Konstruktor klasy
        self.plik_dziennika = plik_z_naszym_dziennikiem                # Atrybuty klasy...
        self.plik_dz = open(self.plik_dziennika, 'rb+')
        self.wpisy = self.przeczytaj_plik()
        self.ilosc_wpisow = len(self.wpisy)

    def __del__(self):              # dodane w dn.13
        self.zamknij_dziennik()     # dodane w dn.13


    def przeczytaj_plik(self):                                          # Jeżeli funkcja jest w klasie, to może być gdziekolwiek. Program ją sobie znajdzie.
        """
        Funkcja która z otwartego pliku czyta dane i zwraca nam w naszym przypadku w postaci listy słowników
        czyli dokłądnie tak jak je zapisujemy (użycie pickla)
        :param plik_dz:
        :return:
        """
        try:
            dane = pickle.load(self.plik_dz)
            return dane
        except:
            print('Błąd')

    def usun_wpis(self):
        """
        Funckaj usuwa wpis z dziennika na podstawie numeru podanego przez użytkownika
        Dodatkowo po usunięciu wysyła mail informacyjnego
        :param plik_dz:
        :return:
        """
        print("Ilość wpisów w dzienniczku to: {}".format(self.ilosc_wpisow))
        wpis_do_usuniecia = int(input("Proszę podaj wpis"))

        if wpis_do_usuniecia <= self.ilosc_wpisow and wpis_do_usuniecia > 0:
            indeks_do_usuniecia = wpis_do_usuniecia - 1
            del (self.wpisy[indeks_do_usuniecia])
            self.plik_dz.seek(0)

            temat = "Pawel_O usunął wpis"
            tresc = "Usunięto wpis o indeksie: {}".format(indeks_do_usuniecia)
            tresc = tresc + "\na dla użytkownika jest to wpis numer: {}".format(wpis_do_usuniecia)

            # wyslij_mail(temat, tresc)
            pickle.dump(self.wpisy, self.plik_dz)
            print("Właśnie usunąłem wpis")
        else:
            print("Nie ma takiego wpisu")

        # self.zamknij_dziennik()

    def wyszukaj(self):
        """
        Funkcja w otwartym dzienniku szuka wpisu zawierającego w tresc zadaną przez użytkownika fraze
        Wyświetla też podsumowanie wyszukiwania
        :param plik_dz:
        :return:
        """
        fraza = input("Podaj szukaną treść: ")

        znaleziono_cos = False
        ilosc_wynikow = 0
        for index, wpis in enumerate(self.wpisy):
            if fraza in wpis["tresc"]:
                znaleziono_cos = True
                ilosc_wynikow += 1
                print(wpis["tresc"])
                print('Na indeksie: {}'.format(index))

        if ilosc_wynikow == 0:
            print("W całym dzienniku nie ma takiej frazy")
        else:
            print("Ilość wpisów: {}".format(ilosc_wynikow))

        # self.zamknij_dziennik()

    def dodaj_wpis(self):
        """
        Funkcja, która pyta użytkownika o dane do nowego wpisu i dodaje go do aktualnej listy plików
        :param plik_dz:
        :return:
        """
        data = input("Podaj datę: ")
        tresc = input("Podaj treść: ")
        nowy_wpis = {"data": data, "tresc": tresc}

        stare_wpisy = self.wpisy
        nowe_wpisy = stare_wpisy

        try:
            nowe_wpisy.append(nowy_wpis)
        except:
            print('Nie było żadnego wpisu. Dodaje pierwszy wpis :)')
            nowe_wpisy = []
            nowe_wpisy.append(nowy_wpis)

        self.plik_dz.seek(0)
        pickle.dump(nowe_wpisy, self.plik_dz)
        print("Wpis został dodany prawidłowo.")

        # self.zamknij_dziennik()

    def zamknij_dziennik(self):
        """
        Funkcja która zamyka plik dzinnika
        :param plik_dz:
        :return:
        """
        self.plik_dz.close()

def wyswietl_menu():
    """
    Proste wyświtlanie
    :return:
    """
    print("Mój dziennik v0.1 alpha\n"
          "1. Wyświetlanie\n"
          "2. Dodawanie\n"
          "3. Usuwanie\n"
          "4. Szukanie\n"
          "5. Wyjscie")

# dziennik = Dziennik() # Optymalnie wywalić to tutaj, a nie robić za każdą pętlą.

def zapytaj():
    """
    Nasz pseudo "controler" do zarządzania flow w programie
    :return:
    """
    decyzja = input("Co wybierasz?")
    if decyzja == "1":
        print("Oto twoje wpisy:")
        pprint.pprint(dziennik.wpisy)
    if decyzja == "2":
        print("Dodawanie wpisu:")
        dziennik.dodaj_wpis()
    if decyzja == "3":
        print("Usuń wpis:")
        dziennik.usun_wpis()
    if decyzja == "4":
        print("Wyszukiwarka:")
        dziennik.wyszukaj()
    elif decyzja == "5":
        exit()

while True:
    dziennik = Dziennik()  # Przensieione,  żeby liczba wpisów się aktualizowała
    wyswietl_menu()
    zapytaj()
    del(dziennik)   # usuwanie z pamięci, żeby jej nie zajmować (dodane w dn 13)