
#? Write a function filter(oldfile, newfile) that copies all the lines of a text file "source.txt" onto "target.txt"
#? except those lines which starts with "@".

def filter(oldfile, newfile):
    oldf = open(oldfile)
    old_data = oldf.readlines()
    oldf.close()

    with open(newfile, "w") as newf:
        for line in old_data:
            if not line.startswith("@"):
                newf.write(line)

filter("source.txt", "target.txt")
