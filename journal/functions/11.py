
#? Write a function vowel_count() in python
#? It counts and displays the number of vowels present in the input given by the user as a string.

def vowel_count():
    vowels = "aeiouAEIOU"
    string = input("Enter a string: ")
    count = 0

    for char in string:
        if char in vowels:
            count += 1

    print("Number of vowels in the string:", count)

vowel_count()
