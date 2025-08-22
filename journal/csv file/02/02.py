
#? Write a menu-driven program, using functions, to perform the following:
#* (1) -> CREATE(): To create a "student.csv" file containing n records having the following details:
#*  [name, eng mark, cs mark, phy mark, chem mark, math mark]
#* (2) -> DISPLAY(): To display the contents of the "student.csv" file.
#* (3) -> SEARCH(): To search and display for given name as input by the user.
#*  Give an appropriate message if record is not found.
#* (4) -> APPEND(): To add additional 'n' records to the file.
#* (5) -> FAILURE(): To copy the names of students who have failed in at least one subject into another file called "fail.txt".
#* (6) -> MODIFY(): To modify marks of CS of students who have scored less than 50, by adding 10 to their marks.
#* (7) -> DELETE(): To delete all students whose average is less than 40%.

import csv


def CREATE():
    n = int(input("Enter the number of student records: "))
    records = []

    for i in range(1, n + 1):
        print("Student", i)
        name = input("Enter name: ")
        eng_mark = float(input("Enter English mark: "))
        cs_mark = float(input("Enter Computer Science mark: "))
        phy_mark = float(input("Enter Physics mark: "))
        chem_mark = float(input("Enter Chemistry mark: "))
        math_mark = float(input("Enter Mathematics mark: "))

        records.append([name, eng_mark, cs_mark, phy_mark, chem_mark, math_mark])

    with open("student.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(records)


def DISPLAY():
    with open("student.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


def SEARCH():
    name = input("Enter the name to search: ")

    with open("student.csv", "r") as f:
        reader = csv.reader(f)

        for row in reader:
            if row[0].lower() == name.lower():
                print("Record found:", row)
                break
        else:
            print("Record not found.")


def APPEND():
    n = int(input("Enter the number of additional student records to add: "))
    current_records = []

    with open("student.csv", "r") as f:
        reader = csv.reader(f)
        for line in reader:
            current_records.append(line)

    for i in range(1, n + 1):
        print("Student", i)
        name = input("Enter name: ")
        eng_mark = float(input("Enter English mark: "))
        cs_mark = float(input("Enter Computer Science mark: "))
        phy_mark = float(input("Enter Physics mark: "))
        chem_mark = float(input("Enter Chemistry mark: "))
        math_mark = float(input("Enter Mathematics mark: "))

        current_records.append([name, eng_mark, cs_mark, phy_mark, chem_mark, math_mark])

    with open("student.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(current_records)


def FAILURE():
    with open("student.csv", "r") as f:
        reader = csv.reader(f)
        failed = []

        for line in reader:
            if min(
                    float(line[1]),
                    float(line[2]),
                    float(line[3]),
                    float(line[4]),
                    float(line[5]),
                ) < 33:
                failed.append(line[0])

    with open("fail.txt", "w") as f:
        f.write("\n".join(failed))


def MODIFY():
    current_records = []
    with open("student.csv", "r") as f:
        reader = csv.reader(f)
        for line in reader:
            current_records.append(line)

    for i in range(len(current_records)):
        if float(current_records[i][2]) < 50:
            current_records[i][2] = str(float(current_records[i][2]) + 10)
            
    with open("student.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(current_records)


def DELETE():
    current_records = []
    with open("student.csv", "r") as f:
        reader = csv.reader(f)
        for line in reader:
            current_records.append(line)

    for record in current_records:
        avg = (float(record[1]) + float(record[2]) + float(record[3]) + float(record[4]) + float(record[5])) / 5
        if avg < 40:
            current_records.remove(record)
    
    with open("student.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(current_records)


while True:
    print("""
Enter an option:
(1) -> CREATE(): To create a "student.csv" file.
(2) -> DISPLAY(): To display the contents of the "student.csv" file.
(3) -> SEARCH(): To search and display for a given name.
(4) -> APPEND(): To add additional 'n' records to the file.
(5) -> FAILURE(): To copy the names of students who have failed in at least one subject into another file called "fail.txt".
(6) -> MODIFY(): To modify marks of CS of students who have scored less than 50, by adding 10 to their marks.
(7) -> DELETE(): To delete all students whose average is less than 40%.
""")
    o = input("Choose an option: ")

    if o == "1":
        CREATE()

    elif o == "2":
        DISPLAY()

    elif o == "3":
        SEARCH()

    elif o == "4":
        APPEND()

    elif o == "5":
        FAILURE()

    elif o == "6":
        MODIFY()

    elif o == "7":
        DELETE()

    else:
        print("Invalid option. Please try again.")
