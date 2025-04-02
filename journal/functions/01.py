
#? Write a function count() which accepts a variable length argument
#? It counts the number of odd and even numbers and returns both the values.

def count(*nums):
    odd = 0
    even = 0

    for num in nums:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1

    return odd, even

odd, even = count(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("Number of odd numbers:", odd)
print("Number of even numbers:", even)
