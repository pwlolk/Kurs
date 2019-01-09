import pprint

class Telefon(object):

    vat = 1.23
    __marza = 1.2             # marża obbowiązująca wszystkie obiekty danej klasy (nie jest to związane z samą instancją obiektu)
    __system = "Inny system"

    @staticmethod
    def sprawdz_cene(cena):
        if cena <= 0:
            return False
        return True

    def __init__(self, producent, nazwa, system, cale, cena):
        self.producent = producent
        self.nazwa = nazwa
        self.system = system
        self.cale = cale
        # self.cena = cena

        if self.sprawdz_cene(cena) is False:
            cena = 99999

        self.cena = cena * __class__.__marza

    def cena_brutto(self):
        return self.cena * __class__.vat

    @classmethod                                            #m metody klasy to głównie alternatywny konstruktor
    def SamsungS10(cls):
        return cls("Samsung", "S10", "Android", 5.5, 0)

    @classmethod
    def SamsungS4(cls):
        return cls("Samsung", "S4", "Android", 5.0, 800)

# print(Telefon.marza)
# print(Telefon.system)

telefon1 = Telefon("Apple", "iPhone", "OSX10", 5.5, 2000)
telefon2 = Telefon.SamsungS10()
telefon3 = Telefon.SamsungS4()

print(telefon1.nazwa)
print(telefon2.nazwa)
print(telefon3.nazwa)

print(telefon1.system)
print(telefon2.system)
print(telefon3.system)

print(telefon1.cena)
print(telefon2.cena)
print(telefon3.cena)

print(telefon1.cena_brutto())
print(telefon2.cena_brutto())
print(telefon3.cena_brutto())

print(telefon1.__dict__) # dict wyświetla wszustko na temat obiektu, klasy
print(Telefon.__dict__) # i tak wyświetli pola pseudo prywtne jak np. __system :o]

# print(Telefon.system) # nie pokaże w wydruku
print(Telefon.marza)