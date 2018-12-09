import csv
# import numpy as np
# from numpy import genfromtxt
# my_data = genfromtxt('a.csv', delimiter=',')

def intro_file_as_csv():
    csv_file = input("Enter a data file name: ")
    try:
        return csv_file
    except:
        print("Incorrect file name. Try again.\n")
        intro_file_as_csv()

def main_menu():
    print("\nOptions:\n"
          "[1] Digging for similar ships [OLPA criteria] -> pick up IMO number\n"
          "[2] Digging for ships of defined parameters \n")

def intro_IMO_number(csv_file):
    search_IMO_number = str(input("Podaj numer IMO: "))
    with open(csv_file, "r+") as csv_data_file:
        reader = csv.reader(csv_data_file)
        for i,row in enumerate(reader):
            if (i == 0):
                print(row)
                continue
            if (row[0] == search_IMO_number):
                print(row)

#Teoretycznie operacja na konkretnej wielkości z tabeli powinna być tożsama z konkretnym indexem w row.
#Tak można przyporzadkować funkcję.

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

def length_criteria(csv_file):
    with open(csv_file, "r+") as csv_data_file:
        reader = csv.reader(csv_data_file) #handler
        for i,row in enumerate(reader):
            if (i == 0):
                continue
            if (float(row[4]) > 85.00 and float(row[4]) < 100.00):
                print(row[0], row[1])

def decision_switch():
    decyzja = input("Pick option: ")
    if decyzja == "1":
        intro_IMO_number(csv_file)
    else:
        exit()

csv_file = intro_file_as_csv()
main_menu()
decision_switch()
# dwt = dwt_summary(csv_file)
# print(format(dwt, ".2f"))
# length_criteria(csv_file)