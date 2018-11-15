imie = input("Jak masz na imię? ")
imie = imie.strip(' ')
dlugosc_imienia = len(imie)
#ostatnia_litera_imienia = imie[dlugosc_imienia-1]
#print(imie[-1:])
ostatnia_litera_imienia = imie[-1:]
#[0:3] - z lewej strony przedział zamknięty (włącznie), z prawej otwarty (wyłącznie).
print("Cześć, " + str(imie).capitalize() + ".")
#print(imie[0].upper())
#print(imie[1].upper())
#print(imie[2].upper())
#print(imie[3].upper())
#print(imie[4].upper())
#print("Twoje imię ma " + str(dlugosc_imienia) + " znaków, a ostatnia litera Twojego imienia to " + str(imie[dlugosc_imienia-1]) + ".")
print("Twoje imię ma " + str(dlugosc_imienia) + " znaków, a ostatnia litera Twojego imienia to " + str(ostatnia_litera_imienia) + ".")
#print("Twoja ostatnia litera imienia to " + str(imie[4]) + ".")
