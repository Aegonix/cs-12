
#? Write a program to input a number in the main program and write a function fact()
#? which returns the factorial of the number
#? and prints the answer in the main program.

n = int(input("Enter a number: "))

def fact(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    
    return factorial

print("The factorial of", n, "is:", fact(n))
