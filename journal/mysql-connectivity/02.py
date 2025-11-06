
#? Write a menu-driven program using MySQL connectivity to do the following, using the tables:
#*  student(grno, name, age, dob, class, tcode1, tcode2, fees) and
#*  teacher(code, name, subject)

#* 1) To insert a record in the student and teacher table by taking values from the user.
#* 2) To delete a record either from student.
#* 3) Increase fees by 100 if the student is in class 12.
#* 4) Display number of students in each class.
#* 5) Display grno, student name, class, code, teacher name, and subject for code.
#* 6) Exit.

import mysql.connector as sql

conn = sql.connect(host="localhost", user="root", password="your password", database="Journal")
cursor = conn.cursor()

while True:
    print("""
What would you like to do?
(1) -> Insert a record in the student and teacher table.
(2) -> Delete a record from student table.
(3) -> Increase fees by 100 if the student is in class 12.
(4) -> Display number of students in each class.
(5) -> Display grno, student name, class, code, teacher name, and subject for code.
(6) -> Exit""")
    
    choice = input("Enter your choice (1-6): ")
    print()

    if choice == "1":
        grno = input("Enter student GR No: ")
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        dob = input("Enter student DOB (YYYY-MM-DD): ")
        s_class = input("Enter student class: ")
        tcode1 = input("Enter teacher code 1: ")
        tcode2 = input("Enter teacher code 2: ")
        fees = input("Enter student fees: ")

        cursor.execute("INSERT INTO student VALUES ({}, '{}', {}, '{}', '{}', '{}', '{}', {})".format(grno, name, age, dob, s_class, tcode1, tcode2, fees))
        conn.commit()

    elif choice == "2":
        del_grno = input("Enter GR No of student to delete: ")

        cursor.execute("DELETE FROM student WHERE grno = {}".format(del_grno))
        conn.commit()

    elif choice == "3":
        cursor.execute("UPDATE student SET fees = fees + 100 WHERE class = '12'")
        conn.commit()

    elif choice == "4":
        cursor.execute("SELECT class, COUNT(*) FROM student GROUP BY class")
        results = cursor.fetchall()

        print("Class | Number of Students")
        for row in results:
            print(row[0], "|", row[1])

    elif choice == "5":
        code = input("Enter teacher code: ")
        cursor.execute("SELECT student.grno, student.name, student.class, teacher.code, teacher.name, teacher.subject FROM student, teacher WHERE (student.tcode1 = teacher.code OR student.tcode2 = teacher.code) AND teacher.code = {}".format(code))
        results = cursor.fetchall()

        print("Gr No | Student Name | Class | Teacher Code | Teacher Name | Subject")
        for row in results:
            print(row[0], "|", row[1], "|", row[2], "|", row[3], "|", row[4], "|", row[5])

    elif choice == "6":
        print("Exiting...")
        break
