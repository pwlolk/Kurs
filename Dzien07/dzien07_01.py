import csv

def intro_file():
    csv_file = input("Wskaż plik do przeanalizowania: ")
    try:
        with open(csv_file, "r+", newline='') as csv_data_file:
            reader = csv.reader(csv_data_file)
            for row in reader:
                print(row)
    except:
        print("Podaj prawidłową nazwę pliku.\n")
        intro_file()

def dwt_summary():


intro_file()
#options_switch()