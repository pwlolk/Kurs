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

def main_menu():
    print("\nOpcje:\n"
          "[1] Wyszukanie statków podobnych [kryteria OLPA]\n"
          "[2] Wyszukanie statków o zadanych parametrach\n")

# def decision_switch():

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

def legth_criteria(csv_file):
    with open(csv_file, "r+") as csv_data_file:
        reader = csv.reader(csv_data_file) #handler
        for i,row in enumerate(reader):
            if (i == 0):
                continue
            if (float(row[4]) > 85.00 and float(row[4]) < 100.00):
                print(row[0], row[1])

csv_file = intro_file_as_csv()
main_menu()
# dwt = dwt_summary(csv_file)
# print(format(dwt, ".2f"))
# legth_criteria(csv_file)

#problemy: czym jest reader, jak podejrzeć pickle, jak odnieść się do row w readerze