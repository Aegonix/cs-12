
#? Write a menu-driven program using MySQL connectivity to do the following, using the table CLUB (having code, name, age, date of application and coach name).
#* a) Display code, name, coach name, where coach name starts with K.
#* b) Display all records in descending order of date of application.
#* c) Display all records where age is between 15 and 25.
#* d) Exit

import mysql.connector as sql

while True:
    print("""
What would you like to do?
(1) -> Display code, name, coach name, where coach name starts with K.
(2) -> Display all records in descending order of date of application.
(3) -> Display all records where age is between 15 and 25.
(4) -> Exit""")
    
    choice = input("Enter your choice (1-4): ")
    print()
    conn = sql.connect(host="localhost", user="root", password="your password", database="Journal")
    cursor = conn.cursor()

    if choice == '1':
        cursor.execute("SELECT code, name, coach_name FROM CLUB WHERE coach_name LIKE 'K%'")
        results = cursor.fetchall()

        for row in results:
            print(row)

    elif choice == '2':
        cursor.execute("SELECT * FROM CLUB ORDER BY date_of_application DESC")
        results = cursor.fetchall()

        for row in results:
            print(row)

    elif choice == '3':
        cursor.execute("SELECT * FROM CLUB WHERE age BETWEEN 15 AND 25")
        results = cursor.fetchall()

        for row in results:
            print(row)

    elif choice == '4':
        print("Exiting...")
        break
