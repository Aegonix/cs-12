
#? Sanjana has created a dictionary containing ProdName and Price as the key-value pairs of 8 products.
#? Write a program with separate user-defined functions to perform the following operations: -
#* i) Push the keys (ProdName) of the dictionary into a stack, where corresponding price range is 5000-25000 (inclusive of both values).
#* ii) Pop and display the contents of the stack.

Product = {"TV": 20000, "Mobile": 19999, "Camera": 4999, "Printer": 5999, "Mouse": 499, "Keyboard": 600, "AC": 25000}

stack = []

def push_keys():
    for prod_name in Product:
        if 5000 <= Product[prod_name] <= 25000:
            stack.append(prod_name)


def pop_display():
    print(stack.pop(), end=" ")

    top = len(stack) - 1
    for i in range(top, -1, -1):
        print(stack[i], end=" ")


push_keys()
pop_display()
