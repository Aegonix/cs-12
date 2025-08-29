
#? Write a menu-driven program to implement a stack called "train", where each element of the stack contains (train_no, train_name).
#? Using functions, implement all the operations permissible on a stack: push(), pop(), display(), and peek().


def push(stack, item):
    stack.append(item)


def pop(stack):
    if stack == []:
        return "Underflow"
    else:
        return stack.pop()


def peek(stack):
    if stack == []:
        return "Underflow"
    else:
        return stack[-1]


def display(stack):
    if stack == []:
        return "Underflow"
    else:
        top = len(stack) - 1

        for i in range(top, -1, -1):
            print(stack[i])


train = []

while True:
    print(
        """
Enter an option:
(1) -> push()
(2) -> pop()
(3) -> peek()
(4) -> display()
(5) -> exit"""
    )
    o = int(input())

    if o == 1:
        train_no = input("Enter train number: ")
        train_name = input("Enter train name: ")
        push(train, (train_no, train_name))

    elif o == 2:
        print(pop(train))

    elif o == 3:
        print(peek(train))

    elif o == 4:
        display(train)

    elif o == 5:
        exit()

    else:
        print("Invalid option")
