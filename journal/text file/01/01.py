
#? Write a function to count the number of lines starting with "W" or "H" in a text file "Country.txt".

def count_lines():
    with open("Country.txt", "r") as f:
        lines = f.readlines()
        count = 0

        for line in lines:
            if line.startswith("W") or line.startswith("H"):
                count += 1

        print(count)

count_lines()
