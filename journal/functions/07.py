
#? Write a program to input two numbers in the main program and write a function findbig() which returns the bigger number.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

def findbig(a, b):
    if a > b:
        return a
    else:
        return b
    
print(findbig(a, b))
