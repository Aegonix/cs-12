
#? Write a method/function ISTOUPCOUNT() in python to read contents from a text file "WRITER.txt".
#? This is to count and display the occurence of the words "IS", "TO", "UP" in the file.

def ISTOUPCOUNT():
    with open("WRITER.txt") as f:
        words = f.read().split()
        is_count = 0
        to_count = 0
        up_count = 0

        for word in words:
            if word.lower() == "is":
                is_count += 1
            elif word.lower() == "to":
                to_count += 1
            elif word.lower() == "up":
                up_count += 1

        print("Count of 'IS':", is_count)
        print("Count of 'TO':", to_count)
        print("Count of 'UP':", up_count)

ISTOUPCOUNT()
