import csv
# import numpy as np
# from numpy import genfromtxt
# my_data = genfromtxt('a.csv', delimiter=',')

def intro_file_as_csv():
    csv_file = input("Wskaż plik do przeanalizowania: ")
    try:
        return csv_file
    except:
        print("Podaj prawidłową nazwę pliku.\n")
        intro_file_as_csv()

# def intro_file_as_csv():
#     csv_file = input("Wskaż plik do przeanalizowania: ")
#     try:
#         with open(csv_file, "r+", newline='') as csv_data_file:
#             reader = csv.reader(csv_data_file)
#             return reader
#     except:
#         print("Podaj prawidłową nazwę pliku.\n")
#         intro_file_as_csv()

# def intro_file_as_txt():
#     csv_file = input("Wskaż plik do przeanalizowania: ")
#     try:
#          with open(csv_file, "r+") as txt_file:
#             txt_file.seek(0)
#             single_string = str(txt_file.read())
#             return single_string
#     except:
#         print("Podaj prawidłową nazwę pliku.\n")
#         intro_file_as_txt()

#Teoretycznie operacja na konkretnej wielkości z tabeli powinna być tożsama z konkretnym indexem w row.
#Tak można przyporzadkować funkcję.

# intro_file_as_csv()

def dwt_summary(csv_file):
    with open(csv_file, "r+") as csv_data_file:
        reader = csv.reader(csv_data_file) #handler
        dwt_summary = 0
        for i, row in enumerate(reader):
            if (i == 0):
                continue
            else:
                dwt_summary = dwt_summary + float(row[9])
        return dwt_summary

csv_file = intro_file_as_csv()
dwt = dwt_summary(csv_file)
print(format(dwt, ".2f"))

#problemy: czym jest reader, jak podejrzeć pickle, jak odnieść się do row w readerze