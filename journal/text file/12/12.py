
#? Write a function COUNT_AND() in Python to read the text file "STORY.txt"
#? It should count the number of times "AND" occurs in the file. (Include AND, and and And in the count)

def COUNT_AND():
    with open("STORY.txt") as f:
        text = f.read()
        count = text.count("AND") + text.count("and") + text.count("And")
    
        print("Number of occurrences of 'AND':", count)

COUNT_AND()
