
#? Write a function move() which accepts a list of numbers as arguments and puts all numbers divisible by 5 to the right.

def move(l):
    for i in l:
        if i % 5 == 0:
            l.remove(i)
            l.append(i)

    print(l)

move([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
