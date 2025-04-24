
#? Write a method in Python to read lines from a text file DIARY.txt and display those lines which start with "p".

def p_lines():
    with open("DIARY.txt") as f:
        lines = f.readlines()
        for line in lines:
            if line.lower().startswith("p"):
                print(line, end="")
    
p_lines()
