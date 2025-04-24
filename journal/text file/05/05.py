
#? Write a code in Python that counts the number of "The" or "This" words present in a text file "MY_TEXT_FILE.txt"

count = 0
with open("MY_TEXT_FILE.txt") as f:
    for words in f.read().split():
        if words.lower() == "the" or words.lower() == "this":
            count += 1

print("The number of 'The' or 'This' words present in the text file is:", count)
