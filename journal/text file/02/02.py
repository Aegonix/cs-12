
#? Write a user-defined function countwords() to display the total number of words present in the file,
#? from a text file "Quotes.txt".

def countwords():
    with open("Quotes.txt") as f:
        print("Number of words:", len(f.read().split()))

countwords()
