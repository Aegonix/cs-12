
#? Write a program to split the file employee.dat into two.
#? One file is named as "manager.dat" and has employee details whose designations are "Manager"
#? The other file is named "accountant.dat" which contains details of employees whose designations are "Accountant".

import pickle

def split():
    with open("employee.dat", "rb") as f:
        employees = pickle.load(f)
    
    managers = {}
    accountants = {}

    for employee in employees:
        if employees[employee][1] == "Manager":
            managers[employee] = employees[employee]
        elif employees[employee][1] == "Accountant":
            accountants[employee] = employees[employee]

    with open("manager.dat", "wb") as managers_file:
        pickle.dump(managers, managers_file)
    
    with open("accountant.dat", "wb") as accountants_file:
        pickle.dump(accountants, accountants_file)

split()
