class Krzeslo(object): ## jeżeli więcej wyrazów w nazwie, to bez podkreślnika za to oddzielając wyrazy wielkimi literami

    def __init__(self, nazwa = 'Wing', material = 'sklaejka', kolor = 'jasny', cena_netto = 20, marza = 10):
        self.ilosc_nog = 4
        self.ilosc_podlokietnikow = None
        self.oparcie = True
        self.wymiary = (80, 40, 40)
        self.producent = 'Bodzio'

        self.nazwa = nazwa
        self.material = material
        self.kolor = kolor
        self.cena_netto = cena_netto

        self.marza = marza

    def cena_sprzedazy(self):
        return self.cena_netto * (1 + self.marza/100)

    def cena_brutto(self):
        return self.cena_sprzedazy()*1.23    # dostep do ceny dla konkretnej instancji

    def cena_brutto_euro(self):
        return self.cena_brutto()*4.30

    def __str__(self): # zamiana na string
        return 'Nazywam się {} i kosztuję {}.'.format(self.nazwa, self.cena_brutto())

obiekt_1 = Krzeslo()
print(obiekt_1.nazwa)
print(obiekt_1) # działa tak, a nie inaczej, bo __str__
# print(obiekt_1.cena_netto)
# print(obiekt_1.cena_brutto())

obiekt_2 = Krzeslo('Wing Lux', 'drewno', 'ciemny', 1000000, 50)
print(obiekt_2.nazwa)
print(obiekt_2)
# print(obiekt_2.cena_netto)
# print(obiekt_2.cena_brutto())