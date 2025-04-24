
#? Write a function COUNT() in python to read contents from file "REPEATED.txt".
#? It should count and display the occurrence of the word "Catholic" or "mother".

def COUNT():
    with open("REPEATED.txt") as f:
        words = f.read().split()
        count_catholic = words.count("Catholic")
        count_mother = words.count("mother")

        print("Occurences of 'Catholic':", count_catholic)
        print("Occurences of 'mother':", count_mother)

COUNT()
