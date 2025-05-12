
#? Write a function to insert more data at the end of the file "employee.dat".

import pickle

def insert_data():
    with open("employee.dat", "rb") as f:
        current_employees = pickle.load(f)
        current_employees[104] = ["Tom Hanks", "Actor", 30000]
        current_employees[105] = ["Charlie Cox", "Actor", 15000]

    with open("employee.dat", "wb") as f:
        pickle.dump(current_employees, f)

insert_data()
