
#? Write a function AMCOUNT() in Python, which reads each character of a text file STORY.txt
#? It counts and displays the occurences of alphabets "A", "M", "a", and "m".

def AMCOUNT():
    with open("STORY.txt") as f:
        text = f.read()
        count_a = text.count("a")
        count_A = text.count("A")
        count_m = text.count("m")
        count_M = text.count("M")
        
        print("Count of 'a':", count_a)
        print("Count of 'A':", count_A)
        print("Count of 'm':", count_m)
        print("Count of 'M':", count_M)

AMCOUNT()
