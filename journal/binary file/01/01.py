
#? Write the following functions:
#? (i) createb(): To create a binary file named as "employee.dat" that contains the details:
#* Employee No., Employee Name, Designation, Salary (as a dictionary)
#? (ii) Search(): To search for an employee detail by taking employee number as a key field in the file "employee.dat".
#? If the employee is not found, give an appropriate message
#? Otherwise, print the details and give bonus of 2000 to those whose salary is less than 20000, and make the changes in the file.

import pickle

def createb():
    with open("employee.dat", "wb") as f:
        emp_data = {
            101: ["John Doe", "Manager", 25000],
            102: ["Sam Smith", "Developer", 18000],
            103: ["Jack Brown", "Accountant", 22000],
        }

        pickle.dump(emp_data, f)

def search(emp_no):
    f = open("employee.dat", "rb")
    employees = pickle.load(f)
    f.close()

    f = open("employee.dat", "wb")
    if emp_no in employees:
        emp_details = employees[emp_no]
        print(f"Employee No: {emp_no}")
        print(f"Employee Name: {emp_details[0]}")
        print(f"Designation: {emp_details[1]}")
        print(f"Salary: {emp_details[2]}")

        if emp_details[2] < 20000:
            emp_details[2] += 2000
            print("Added bonus of 2000 to salary")
            employees[emp_no] = emp_details
            pickle.dump(employees, f)
    else:
        print("Employee not found.")
    
    f.close()

createb()
search(102)
