
#? Write a python function that finds and displays all the words longer than 5 characters from the input given by the user.

def long_words(words):
    for word in words:
        if len(word) > 5:
            print(word)

words = input("Enter a sentence: ").split()
long_words(words)
