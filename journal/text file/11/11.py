
#? Write a function in Python to read lines from file "POEM.txt" and display all the words with two characters.

def two_chars():
    with open("POEM.txt") as f:
        lines = f.readlines()
        for line in lines:
            words = line.split()
            for word in words:
                if len(word) == 2:
                    print(word)

two_chars()
