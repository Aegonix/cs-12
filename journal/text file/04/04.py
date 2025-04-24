
#? Write a function VowelCount() in Python, which should read each character of a text file MY_TEXT_FILE.txt.
#? It should count and display the occurence of vowels.

def VowelCount():
    with open("MY_TEXT_FILE.txt") as f:
        text = f.read()
        vowel_count = 0

        for char in text:
            if char in "aeiouAEIOU":
                vowel_count += 1

        print("Number of vowels in the file:", vowel_count)

VowelCount()
