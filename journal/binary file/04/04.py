
#? Write a menu-driven program in Python using user-defined functions to perform the following:
#* (1) -> CREATE(): To create "STUDENT.DAT" file containing records having the following details:
#*  1. Roll No.
#*  2. Name of the student
#*  3. Marks
#*  4. House
#* (2) -> DISPLAY(): To display the contents of the file whose file name is an input from the user.
#* (3) -> SEARCHNAME(): To search and display for a given name as input from the user.
#*  Give appropriate message if the record is not found.
#* (4) -> SEARCHID(): To search and display for a given roll number as input from the user.
#*  Give appropriate message if the record is not found.
#* (5) -> APPEND(): To add additional 'n' records to the file "STUDENT.DAT".
#* (6) -> COUNT(): To count the total number of records in the file. Also, find the average marks of the students.
#* (7) -> HIGHEST(): To copy the records of students whose mark is greater than 90 into another file called "HIGH.dat".
#* (8) -> MODIFY(): To modify marks of those students where mark is less than 23, by adding 10 to their existing marks.
#* (9) -> DELETE(): To delete all students where house is "Emerald".
#* (10) -> DELETEROLL(): To delete student record with the given roll number.
#*  Give appropriate message if the record is not found.

import pickle


def CREATE():
    with open("STUDENT.DAT", "wb") as f:
        n = int(input("Enter number of records: "))

        for i in range(n):
            print("Student", i + 1)
            roll_no = int(input("Enter Roll No: "))
            name = input("Enter Name: ")
            marks = float(input("Enter Marks: "))
            house = input("Enter House: ")
            print()

            record = [roll_no, name, marks, house]
            pickle.dump(record, f)

        print("Records created successfully.\n")


def DISPLAY():
    with open(input("Enter file name of file to display: "), "rb") as f:
        try:
            while True:
                print(pickle.load(f))
        except EOFError:
            print()


def SEARCHNAME():
    name = input("Enter name to search for: ")

    with open("STUDENT.DAT", "rb") as f:
        try:
            while True:
                record = pickle.load(f)
                if record[1] == name:
                    print(record)
                    break
        except EOFError:
            print("Record not found.")

    print()

def SEARCHID():
    roll_no = int(input("Enter roll number to search for: "))

    with open("STUDENT.DAT", "rb") as f:
        try:
            while True:
                record = pickle.load(f)
                if record[0] == roll_no:
                    print(record)
                    break
        except EOFError:
            print("Record not found.")

    print()


def APPEND():
    records = []
    with open("STUDENT.DAT", "rb") as f:
        try:
            while True:
                records.append(pickle.load(f))
        except EOFError:
            pass

    n = int(input("Enter number of records to append: "))
    for i in range(n):
        print("New student", i + 1)
        roll_no = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))
        house = input("Enter House: ")
        print()

        record = [roll_no, name, marks, house]
        records.append(record)

    with open("STUDENT.DAT", "wb") as f:
        for record in records:
            pickle.dump(record, f)

    print("Records appended successfully.\n")


def COUNT():
    count = 0
    total_marks = 0
    with open("STUDENT.DAT", "rb") as f:
        try:
            while True:
                record = pickle.load(f)
                total_marks += record[2]
                count += 1
        except EOFError:
            pass

    print("Total number of records:", count)
    if count > 0:
        print("Average marks of students:", total_marks / count)
        print()
    else:
        print("No records found.\n")


def HIGHEST():
    highest = []
    with open("STUDENT.DAT", "rb") as f:
        try:
            while True:
                record = pickle.load(f)
                if record[2] > 90:
                    highest.append(record)
        except EOFError:
            pass

    with open("HIGH.DAT", "wb") as f:
        for record in highest:
            pickle.dump(record, f)

    print()


def MODIFY():
    records = []
    with open("STUDENT.DAT", "rb") as f:
        try:
            while True:
                record = pickle.load(f)
                if record[2] < 23:
                    record[2] += 10
                records.append(record)
        except EOFError:
            pass

    with open("STUDENT.DAT", "wb") as f:
        for record in records:
            pickle.dump(record, f)

    print("Records modified successfully.\n")


def DELETE():
    records = []
    with open("STUDENT.DAT", "rb") as f:
        try:
            while True:
                record = pickle.load(f)
                if record[3] != "Emerald":
                    records.append(record)
        except EOFError:
            pass

    with open("STUDENT.DAT", "wb") as f:
        for record in records:
            pickle.dump(record, f)

    print("Records deleted successfully.\n")


def DELETEROLL():
    roll_no = int(input("Enter roll number to delete: "))
    records = []
    with open("STUDENT.DAT", "rb") as f:
        try:
            while True:
                record = pickle.load(f)
                if record[0] != roll_no:
                    records.append(record)
        except EOFError:
            pass

    with open("STUDENT.DAT", "wb") as f:
        for record in records:
            pickle.dump(record, f)

    print("Record deleted successfully.\n")


while True:
    print(
        """What would you like to do?
(1) -> Creates "STUDENT.DAT"
(2) -> Displays the complete content of the file.
(3) -> Searches for a given name.
(4) -> Searches for a given roll number.
(5) -> Appends additional records to the file.
(6) -> Counts total records and average marks.
(7) -> Copies records with marks > 90 to "HIGH.DAT".
(8) -> Modifies marks < 23 by adding 10.
(9) -> Deletes students in "Emerald" house.
(10) -> Deletes student with given roll number."""
    )

    o = int(input("Enter an option: "))
    print()

    if o == 1:
        CREATE()

    elif o == 2:
        DISPLAY()

    elif o == 3:
        SEARCHNAME()

    elif o == 4:
        SEARCHID()

    elif o == 5:
        APPEND()

    elif o == 6:
        COUNT()

    elif o == 7:
        HIGHEST()

    elif o == 8:
        MODIFY()

    elif o == 9:
        DELETE()

    elif o == 10:
        DELETEROLL()

    else:
        print("Invalid option. Please try again.\n")
