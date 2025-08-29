
#? Samantha has created a dictionary containing ID and their Names as the key-value pairs of 8 students.
#? Write a program with separate user-defined functions to perform the following operations:-
#* i) Push the keys (ID of the students) of the dictionary into a stack, where corresponding name begins from letter "A".
#* ii) Pop and display the contents of the stack.

Student = {"S001": "Amit", "S002": "Lucky", "S003": "Akshay", "S004": "Navneet", "S005": "Jeetu", "S006": "Ajay"}

stack = []


def push_keys():
    for ID in Student:
        if Student[ID].startswith("A"):
            stack.append(ID)


def pop_display():
    print(stack.pop(), end=" ")

    top = len(stack) - 1
    for i in range(top, -1, -1):
        print(stack[i], end=" ")


push_keys()
pop_display()
