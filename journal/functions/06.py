
#? Write a menu driven program to do the following tasks with the help of user-defined functions:
#* 1) Check whether the number is even and return true if it is, else return false
#* 2) Check whether number is prime or not
#* 3) Exit

def is_even(n):
    return n % 2 == 0

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True

while True:
    print("""What would you like to do?
(1) -> Check if a number is even
(2) -> Check if a number is prime
(3) -> Exit
""")
    
    o = int(input("Enter your choice: "))

    if o == 1:
        n = int(input("Enter a number: "))
        print("The number is even:", is_even(n))

    elif o == 2:
        n = int(input("Enter a number: "))
        print("The number is prime:", is_prime(n))

    elif o == 3:
        print("Exiting...")
        break

    else:
        print("Invalid choice, try again.")
