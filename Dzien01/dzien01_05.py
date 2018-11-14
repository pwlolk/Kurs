imie = input("Jak masz na imię? ")
imie = imie.strip(' ')
ostatnia_litera_imienia = imie[-1:]
if(ostatnia_litera_imienia == 'a'):
    print("Cześć, dziewczyno!")
else:
    print("Cześć, chłopaku!")
# coś ta