
#? Write a menu-driven program in Python, using functions to perform the following:
#* CREATE(): To create a "TOY.CSV" file containing records having the following details:
#*  [name of toy, price, category, stock]
#* (1) -> DISPLAY(): To display the contents of the "TOY.CSV" file.
#* (2) -> SEARCH(): To search and display for given name of toy as an input by the user.
#*  Give an appropriate message if the record is not found.
#* (3) -> APPEND(): To add additional "n" records into "TOY.CSV"
#* (4) -> HIGHEST(): To copy the records of toys where the price is greater than 100, into another file called "HIGHEST.CSV"
#* (5) -> MODIFY(): To modify stock of toys by adding 10 to the toys with stock less than 10
#* (6) -> DELETE(): To delete all toys with category as "FUN"

import csv


def CREATE():
    with open("TOY.CSV", "w", newline="") as f:
        details = eval(input("Enter all records in the order: [[name of toy, price, category, stock], ...]: "))
        writer = csv.writer(f)
        header = ["NAME", "PRICE", "CATEGORY", "STOCK"]
        details.insert(0, header)

        writer.writerows(details)


CREATE()


def DISPLAY():
    with open("TOY.CSV", "r") as f:
        reader = csv.reader(f)
        skipped = False

        for line in reader:
            if skipped:
                print(line)

            else:
                skipped = True


def SEARCH():
    with open("TOY.CSV", "r") as f:
        reader = csv.reader(f)
        name = input("Enter the name to search for: ")
        skipped = False

        for line in reader:
            if skipped:
                if line[0] == name:
                    print(line)
                    break

            else:
                skipped = True

        else:
            print("Name was not found in TOY.CSV")


def APPEND():
    n = int(input("Enter number (n) of records to be added: "))
    current_details = []

    with open("TOY.CSV", "r") as f:
        reader = csv.reader(f)

        for line in reader:
            current_details.append(line)

    for i in range(1, n + 1):
        print("Record", i)
        record = eval(input("Enter the record in the form of [name of toy, price, category, stock]: "))
        current_details.append(record)

    with open("TOY.CSV", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(current_details)


def HIGHEST():
    with open("HIGHEST.CSV", "w", newline="") as highest_csv:
        with open("TOY.CSV", "r") as toy_csv:
            reader = csv.reader(toy_csv)
            writer = csv.writer(highest_csv)
            highest = []
            skipped = False

            for record in reader:
                if skipped:
                    if float(record[1]) > 100:
                        highest.append(record)
                else:
                    skipped = True

            if highest:
                writer.writerows(highest)
            else:
                print("No toys have price greater than 100.")


def MODIFY():
    with open("TOY.CSV", "r") as f:
        reader = csv.reader(f)
        current_details = []
        skipped = False

        for line in reader:
            if skipped:
                if int(line[3]) < 10:
                    line[3] = str(int(line[3]) + 10)
                current_details.append(line)

            else:
                current_details.append(line)
                skipped = True

    with open("TOY.CSV", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(current_details)


def DELETE():
    with open("TOY.CSV", "r") as f:
        reader = csv.reader(f)
        current_details = []
        skipped = False

        for line in reader:
            if skipped:
                if line[2] != "FUN":
                    current_details.append(line)
            else:
                current_details.append(line)
                skipped = True

    with open("TOY.CSV", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(current_details)


while True:
    print("""Enter an option:
(1) -> DISPLAY(): To display the contents of the "TOY.CSV" file.
(2) -> SEARCH(): To search and display for given name of toy as an input by the user.
(3) -> APPEND(): To add additional "n" records into "TOY.CSV"
(4) -> HIGHEST(): To copy the records of toys where the price is greater than 100, into another file called "HIGHEST.CSV"
(5) -> MODIFY(): To modify stock of toys by adding 10 to the toys with stock less than 10
(6) -> DELETE(): To delete all toys with category as \"FUN\"""")
    
    o = input()

    if o == "1":
        DISPLAY()

    elif o == "2":
        SEARCH()

    elif o == "3":
        APPEND()

    elif o == "4":
        HIGHEST()

    elif o == "5":
        MODIFY()

    elif o == "6":
        DELETE()

    else:
        print("Invalid option. Please try again.")
