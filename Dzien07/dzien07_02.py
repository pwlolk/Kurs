# NA KURSIE

# pypi.org. ma paczki konsolowe

# moduł OS służy do pracy z katalogami (przydatne np. przy funkcjach menedżera programu)
# albo przy obsłudze plików z tymczasowymi danymi, np. tempami.
# Moduł shutil - wrapper do poleceń systemowych, np. do uruchomień zewn. programów
# Moduł send2trash - przenosi do Kosza, niezależnie od systemu operacyjnego
# Moduły "pocztowe": smtlib, imaplib, email.mime.MimeText (linki na Slacku i w prezentacji)

# import csv
# import numpy
#
# reader = csv.reader()

import os
import sys
import send2trash

os.chmod("rem.txt",436)
send2trash.exceptions("rem.txt")


print (sys.path) # pokazuje ścieżki, w których python szuka modułów
print(os.getcwd()) #pokazuje katalog, w którym pracujemy aktualnie


