#
# # zmienna = r"Jakiś \nekst"
# # print(zmienna)
#
#
# # zmienna = 'To jest jakiś" "tekst"'
# # print(zmienna)
#
#
# #różne sposoby formatowania zmiennych
# napis = "huhu"
# zmienna = f"To jest napis: {napis}"
# print(zmienna)
#
#
# napis = "huhu"
# zmienna = "To jest napis " + str(napis)
# print(zmienna)
#
#
# zmienna = 012.230000
# print ("zmienna %s" %zmienna)
# print ("zmienna %f" %zmienna)
# print ("zmienna %d" %zmienna)
#
# #nie musimy znać kolejności nawiasów
# print("To jest {} sposób na wprowadzenie {}".format(3, 'zmiennych'))
#
# print("To jest {ilosc} sposób na wprowadzenie {nazwa}".format(ilosc=3, nazwa ='zmiennych'))
# #widoczne tylko w ramach string, w obrębie tej linii to nie są zmienne, ale argument funkcji; dobre do przyporządkowywania pół o znanej nazwie


#zasobowo wywoałanie funkcji raz jest efektywniejsze niż 3x, na proste rzeczy lepiej robić matematykę niż bibliotekę


# import string #kolejna biblioteka służąca do wyświetleń pewnych domyślnych zbiorów w obrębie stringóœ
# print(string.ascii_uppercase)
# print(string.hexdigits)
# print(string.digits)
# print(string.hexdigits)

# zdanie = "encyklopedia"
# print(zdanie [4])
# print(zdanie[-3])
# print(zdanie[2:8])
# print(zdanie[1:7:2])
# print(zdanie[-1])
# print(zdanie[2:-2])

# range1 = range(3,4)
# range2 = range(1,40)
# lista1 = [1, 2, 3, "napis"]
# lista11 = list("dwa") #string jest iterowalny więc zostaje rozindeksowany na litery
# lista12 = list(lista1)
# lista13 = list(range2)
# # lista2 = ["kwiatek", "dziadek", "burek"]
# # lista5 = list("dwa")
# print(lista1)
# print(type(lista1))
# print(range1)
# print(type(range1))
# print(lista11)
# print(type(lista11))
# print(lista12)
# print(type(lista12))
# print(lista13)
# print(type(lista13))

#range z 40 mln rekordów nic nie robi, lista z 40 mln rekordów boli pamięć

# lista1 = [1, 2, 3, "napis"]
# print(lista1)
# lista1[3] = "trzy"
# print(lista1)
# del(lista1[2]) #usuwanie na postawie indeksu
# print(lista1)
# lista1.append("14")
# print(lista1)
# print(lista1.pop()) #usuwa ostatni i go zwraca
# print(lista1)
# print(lista1.pop(2)) #usuwa wskazany indeksem element (liczone od lewej, z minusem od prawej zwracając go)

# lista34 = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,"burek"]
#     ]
# print(lista34[2][2][1:])
#
# lista35 = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,"burek"]
#     ]
# print(lista35[2][2])

#tuple (KROTKA - dokładnie tak) działa prawie identycznie jak listam, tylko, że nie jest mutowalny. Nie można tam wstawiać odejmować, z reguły wstawia się tam wzorcowy zestaw danych. Rzadko stosowane. Ale
#do mojej tablicy cydrowniczej mogłoby to być użyte.

# wyrazy =("raz", "dwa", "trzy")
# wyrazy[0] = "jeden"
# print(wyrazy)
#
# odwoływanie się do indeksów zawsze w nawiasach kwadratowych, bo w zwykłych jest odwołanie do funkcji.

# x=0
# while(x<10): #while tłumaczone jako "dopóki"
#     print("wyświetl mnie!")
#     x=x+1 #albo x+=1

decyzja = None
while (decyzja != 'T'):
    decyzja = input("Wciśnij t, żeby zakończyć program ---> ")
    decyzja = decyzja.capitalize()