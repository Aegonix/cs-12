
#? Write a menu-driven program in Python to perform/manipulate a text file called "POETIC.txt"
#? The file "POETIC.txt" has n number of lines and is created using the create() user-defined function.
#? The menu should have the following user-defined functions:
#* (1) -> CREATE(): Creates "POETIC.txt"
#* (2) -> DISPLAY(): Displays the complete content of the file.
#* (3) -> COUNTCHAR(): Reads the text file and displays the number of vowels, consonants, uppercase, and lowercase characters.
#* (4) -> HASHSHOW(): Reads the text file line by line and displays each word separated by "#".
#* (5) -> COPY(): Copies all the lines which contain "#" to another file called "special.txt".
#* (6) -> REPLACE(): Replaces a word with another user-given word into another file called duplcate.txt. Displays both files.
#* (7) -> DELETE(): Deletes a given word in the text file.
#* (8) -> COUNTEND(): Counts the number of lines ending with "y" or "i".
#* (9) -> VOWEL(): Copies all words that start with a vowel to another file "vowel.txt". Displays both files.
#* (10) -> CHANGE(): Replaces every space with "**". Displays both files.


def CREATE():
    with open("POETIC.txt", "w") as f:
        n = int(input("Enter number of lines: "))
        for i in range(1, n + 1):
            line = input("Enter line " + str(i) + " : ")
            f.write(line + "\n")


def DISPLAY():
    with open("POETIC.txt") as f:
        for char in f.read():
            print(char, end="")


def COUNTCHAR():
    with open("POETIC.txt") as f:
        vowels_count = 0
        consonants_count = 0
        uppercase_count = 0
        lowercase_count = 0

        for char in f.read():
            if char in "aeiouAEIOU":
                vowels_count += 1
            elif char in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
                consonants_count += 1            
            if char.isupper():
                uppercase_count += 1
            elif char.islower():
                lowercase_count += 1
            
        print("Number of vowels:", vowels_count)
        print("Number of consonants:", consonants_count)
        print("Number of uppercase characters:", uppercase_count)
        print("Number of lowercase characters:", lowercase_count)


def HASHSHOW():
    with open("POETIC.txt") as f:
        lines = f.readlines()
        for line in lines:
            words = line.split()
            for word in words:
                print(word, end="#")
            print()


def COPY():
    f = open("POETIC.txt")
    lines = f.readlines()
    f.close()
    
    with open("special.txt", "w") as f1:
        for line in lines:
            if "#" in line:
                f1.write(line)


def REPLACE():
    f = open("POETIC.txt")
    text = f.read()
    f.close()

    with open("duplicate.txt", "w+") as duplicate:
        word_to_replace = input("Enter the word to replace: ")
        new_word = input("Enter the new word: ")

        changed_text = text.replace(word_to_replace, new_word)
        duplicate.write(changed_text)

        print("Original text:")
        for char in text:
            print(char, end="")

        duplicate.flush()
        duplicate.seek(0)

        print("\nChanged text:")
        for char in duplicate.read():
            print(char, end="")


def DELETE():
    f = open("POETIC.txt")
    text = f.read()
    f.close()

    word_to_delete = input("Enter the word to delete: ")
    text = text.replace(word_to_delete, "")

    with open("POETIC.txt", "w") as f:
        f.write(text)


def COUNTEND():
    with open("POETIC.txt") as f:
        lines = f.readlines()
        count = 0
        for line in lines:
            if line.rstrip().endswith("y") or line.rstrip().endswith("i"):
                count += 1
        print("Number of lines ending with 'y' or 'i':", count)


def VOWEL():
    f = open("POETIC.txt")
    text = f.read()

    with open("vowel.txt", "w+") as v:
        for word in text.split():
            if word[0].lower() in "aeiou":
                v.write(word + "\n")
                v.flush()

        print("Original file:")
        for char in text:
            print(char, end="")

        v.flush()
        v.seek(0)
        print("\nVowel file:")
        for char in v.read():
            print(char, end="")

    f.close()


def CHANGE():
    f = open("POETIC.txt")
    text = f.read()
    f.close()

    changed_text = text.replace(" ", "**")

    with open("changed.txt", "w+") as f:
        f.write(changed_text)

        f.flush()
        f.seek(0)

        print("Original text:")
        for char in text:
            print(char, end="")

        print("\nChanged text:")
        for char in f.read():
            print(char, end="")


while True:
    print("""What would you like to do?
(1) -> CREATE(): Creates "POETIC.txt"
(2) -> DISPLAY(): Displays the complete content of the file.
(3) -> COUNTCHAR(): Reads the text file and displays the number of vowels, consonants, uppercase, and lowercase characters.
(4) -> HASHSHOW(): Reads the text file line by line and displays each word separated by "#".
(5) -> COPY(): Copies all the lines which contain "#" to another file called "special.txt".
(6) -> REPLACE(): Replaces a word with another user-given word into another file called duplicate.txt. Displays both files.
(7) -> DELETE(): Deletes a given word in the text file.
(8) -> COUNTEND(): Counts the number of lines ending with "y" or "i".
(9) -> VOWEL(): Copies all words that start with a vowel to another file "vowel.txt". Displays both files.
(10) -> CHANGE(): Replaces every space with "**". Displays both files.""")
    
    o = int(input("Enter an option: "))
    print()
    
    if o == 1:
        CREATE()

    elif o == 2:
        DISPLAY()

    elif o == 3:
        COUNTCHAR()

    elif o == 4:
        HASHSHOW()

    elif o == 5:
        COPY()

    elif o == 6:
        REPLACE()

    elif o == 7:
        DELETE()

    elif o == 8:
        COUNTEND()

    elif o == 9:
        VOWEL()

    elif o == 10:
        CHANGE()

    else:
        print("Invalid option. Please try again.")

    print()
