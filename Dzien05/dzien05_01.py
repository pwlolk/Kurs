# Dzien 5

# Używanie kluczy jako elementów słownika jest "nadużyciem", bo de facto słownik staje się listą, tylko żre wincyj pamięci.
#Zmienna, która pierwszy raz występuje w funkcji nie jest dostępna "na zewnątrz". ZMienne globalne (pierwszy poziom wcięcia) są dostępne wszędzie.
#Dostepność zmiennej "lokalnej" funkcji przez return i później przez przypisanie do jakiejś zmiennej w globalu.
#Pliki trzeba zamykać, żeby zwolnić RAM. Może to być wywolane kodem lub "scedowane" na pythona (WITH)
#KURSOR W PLIKU - kursor wykonuje operacje od miejsca, w którym jest

# osoby = {"studenci": ["Ala", "Jan", "Ania"], "wykladowcy": ["doktor", "profesor"]}
# print(osoby["studenci"][1])
#
# osoby["wykladowcy"].append("magister")
# osoby["administracja"] = ["pani Basia z dziekanatu"]
# osoby.update({"ochrona":"Impel"})
#
# print(osoby)


# slownik = {"imie": ["Lukasz", "Ala", "Ola"],
#            "nazwisko": ["Falkowicz", "Kowalska", "Malinowska", "Igrekowska"]
# }

# print(type(slownik))
# print(slownik)

# print(slownik.keys())
# print(slownik.items())

# for klucz, wartosc in slownik.items():
#     print(klucz)
#     for dana in wartosc:
#         print("\t-> " + dana)
#
# nazwiska = slownik["nazwisko"] #wyciagniecie fragmentu do podoperACJI



# miasta = {"miasta": ["Warszawa", "Gdańsk", "Sopot", "Kraków"]}
#
# def wyswietl_slownik():
#     imiona = slownik["imie"]
#     nazwiska = slownik ["nazwisko"]
#     miasto = miasta["miasta"]
#     for index, imie in enumerate (imiona):
#         print(index)
#         print("Mam na imie {} nazwisko {} i mieszkam w {}".format(imiona[index], nazwiska[index], miasto[index]))
#
# wyswietl_slownik()

# lissss = wyswietl_slownik()
# print(lissss)


# plik = open('dane.txt')
# print(plik.readline())
# print(plik.readline())
# print(plik.readline())
# plik.close()

# plik = open('dane.txt')
# print(plik.readline(), end='') #KURSOR ZOSTAJE W MIEJSCU
# plik.seek(0) #przesunięcie kursora na początek
# print(plik.readline(), end='')
# plik.seek(4) #przesunięcie kursora o 4 znaki
# print(plik.readline(), end='')
# plik.close()

# plik = open('dane.txt', "w+") # z pluse write and read
# # print(plik.readline(), end='')
# # print(plik.readline(), end='')
# # print(plik.readline(), end='')
# plik.write("AAAAAA") #nadpisze za pierwszym razem wszystko
# plik.seek(0)
# plik.write("B")
# plik.seek(0)
# print(plik.readline(), end="")
# plik.close()

# plik = open('dane.txt', "r+")
# stan = int(plik.readline()) + 1
# # stan = stan + 1
# plik.seek(0)
# plik.write(str(stan))
# print("Aktualny stan licznika: " + str(stan))
# plik.close()
#
# with open('dane.txt', "r+") as plik:
#     stan = int(plik.readline()) + 1
#     # stan = stan + 1
#     plik.seek(0)
#     plik.write(str(stan))
#     print("Aktualny stan licznika: " + str(stan))


while True:
    dane = input("Podaj imie i nazwisko: ")
    with open('dane.txt', "a+") as plik:
         plik.seek(0,2)
         plik.write('\n' + str(dane))