
#? Write a python function that displays all the words containing @cmail from the input given by the user.

def cmail(words):
    for word in words:
        if "@cmail" in word:
            print(word)
    
words = input("Enter a sentence: ").split()
cmail(words)
