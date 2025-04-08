
#? Write a function series() which accepts two values (x and n as arguments)
#? It finds the sum of the series 1 + x + x^2 + x^3 + ... + x^n
#? and prints the answer in the main program.

def series(x, n):
    sum = 0
    for i in range(n + 1):
        sum += x ** i
    
    print(sum)

series(2, 3)
