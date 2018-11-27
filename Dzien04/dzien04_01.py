# Dzien 4

# Typy iteracyjne: listy, range, krotki, stringi - tam mozna się odwołać po indeksie. FLoat, integer, bools - nie są.

# od - do - pamiętać o zamykaniu przedziałów!

# liczby = range(0,51)
# for liczba in liczby:
#     if(liczba % 2 != 0):
#         continue #powrót do warunku pętli
#     print(liczba)

# liczby = range(0,51)
# for liczba in liczby:
#     if(liczba % 2 != 0):
#         break #wyjście z pętli
#     print(liczba)
#
# liczby = range(0,51)
# for liczba in liczby:
#     if(liczba % 2 != 0):
#         pass #przechodzi do następnej linii pętli zanidebując warunek
#     print(liczba)

# napis = 'Ala ma kota'
# lista_z_napisu = list(napis) # przejęcie stringa do listy
# print (lista_z_napisu)


# napis = 'Ala ma coś tam cokolwiek'
# for index in napis: #index jest tutaj odwołaniem do zawartości pod danym indeskem w danym typie iteracyjnym, czyli jakby napis[index]
#     print(index)


# lista_imion = ['Ola', 'Ala', 'Tomek', 'Jan']
# for imie in lista_imion:
#     print(imie)


# lista_imion = ['Ola', 'Ala', 'Tomek', 'Jan']
# for i, imie in enumerate(lista_imion): #enumerate wyciąga konkretny index i wartośc spod niego
#     print('Na pozycji {} jest imie: {}'.format(i+1, imie))


# lista_imion = ['Ola', 'Ala', 'Tomek', 'Jan']
# lista_nazwiska = ['Kowalska', 'Malinowska', 'Iksiński', 'Igrekowski']
# for imie,nazwisko in zip(lista_imion, lista_nazwiska): #imie, nazwisko jest tutaj zawartoscią spod kolejnego indeksu
#     print('{} {}'.format(imie,nazwisko))

# --- to wyżej to było uzupełnienie do dnia nr 3 ---

#Dzien 4

# Typ referencyjny - referencja mówi, gdzie zawartość danej danej znajduje się w pamięci.
# CHodzi o to, że np. kopie listy nie są kopiami sesnu stricto, tylko odniesieniami do miejsca w pamięci z tą listą.
# Analogia do skrótów na pulpicie (referują do rzeczywistej lokalizacji)
# Listy są typami referencyjnymi.
# Mozna kopiować (powielać) typy refenrecyjne - biblioteka 'copy' + metoda copy.deepcopy(......) lub deepcopy.
# Stringi, inty - nie są typami referencyjnymi, kopia danej zmiennej rezerwuje kolejne miejsce w pamięci.


# lista = ['aaa', 'bbb', 'ccc', 'ddd']
# przypisanie = lista
#
# #lista[0] = 'xxx' albo
# przypisanie[0] = 'xxx' # tak samo
#
# print (lista)
# print (przypisanie)


# import copy
# lista = ['aaa', 'bbb', 'ccc', 'ddd']
# przypisanie = lista
#
# kopia_indeksami = lista[:]
# kopia_kontruktorem = list(lista)
# kopia_metoda = lista.copy()
# kopia_biblioteka = copy.copy(lista)
#
# lista[0] = 'XXX'
# kopia_biblioteka[0] = 'YYY'
#
# print (lista)
# print (przypisanie) #referencja
# print(kopia_indeksami) #nowy obiekt, już nie referencja (WAŻNE)
# print(kopia_kontruktorem) #nowy obiekt, już nie referencja (WAŻNE)
# print(kopia_metoda) #nowy obiekt, już nie referencja (WAŻNE)
# print(kopia_biblioteka) #nowy obiekt, już nie referencja (WAŻNE)  - ALE NA PIERWSZYM POZIOMIE (patrz niżej)



# import copy
# lista2 = ['AAA', ['BBB', ['CCC', ['DDD']]]]
#
# lista2_przypisanie = lista2
# lista2_copy = copy.copy(lista2)
# lista2_deepcopy = copy.deepcopy(lista2)
#
# lista2_przypisanie[1][0] = 'YYY'
#
# print(lista2)
# print(lista2_przypisanie)
# print(lista2_copy) # tutaj ciągle na kolejnych poziomach są referencje do oryginalnej listy, stąd podmiana na [1][0] jest ciągle operacją na lista2.
# print(lista2_deepcopy)

# ---- FUNKCJE ---

#Funkcja jest type referencyjnym, jak np. lista
# Np. print jest funkcją predefiniowaną w pythonie :o)

# def wyswietl_napis(napis, koniec='.', poczatek='-'): #parametr jak end # jaki typ argumentu zdefiniujemy, taki musi być zadawany dalej. Jak koniec czy poczatek sa stringami to dalej musi byc string lub zrzutować.
#     print(poczatek + napis + koniec)
#     # print(str(poczatek) + str(napis) + str(koniec)) # rzutowanie, żeby był zawsze string
#
# koniec = 'elo'
# poczatek = 'hello'
# napis = 'cokolwiek'
# zmienna = '!'*20
# wyswietl_napis(napis)

litera = "m"
ciag_znakow = 'BabaX max kotAX'

def policz_literke (litera, ciag_znakow):
    lower_ciag = ciag_znakow.lower() # obniżenie wszystkiego, żeby nie było case sensitive
    lower_literka = litera.lower() # obniżenie wszystkiego, żeby nie było case sensitive
    ilosc = lower_ciag.count(lower_literka)
    return ilosc

print(policz_literke(litera, ciag_znakow))

# PEP 257 opisuje sposób opisywania funkcji



