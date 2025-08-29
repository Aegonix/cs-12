
#? Alam has a list containing 10 integers.
#? You need to help him create a program with separate user-defined functions to perform the following operations based on this list.
#* i) Traverse the content of the list and push the even numbers into a stack.
#* ii) Pop and display the content of the stack.

integers = [5, 2, 8, 1, 4, 10, 3, 6, 9, 7]
stack = []


def push_even_numbers():
    for num in integers:
        if num % 2 == 0:
            stack.append(num)


def pop_display():
    print(stack.pop())

    top = len(stack) - 1
    for i in range(top, -1, -1):
        print(stack[i])


push_even_numbers()
pop_display()
