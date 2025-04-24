
#? Write a function in Python that displays the number of lines starting with "H" in the file "para.txt".

def h_lines():
    with open("para.txt") as f:
        lines = f.readlines()
        for line in lines:
            if line.lower().startswith("h"):
                print(line, end="")
    
h_lines()
