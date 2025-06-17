
#? Vedansh is a Python programmer working in a school.
#? For the Annual Sports Event, he has created a CSV file named "Result.csv", to store the results of students in different sports events.
#? The structure of Result.csv is:
#* [St_Id (int), St_Name (str), Game_Name (str), Result (str) -> ('Won' / 'Lost' / 'Tie')]
#? Vedansh wants to write the following user-defined functions:
#* Accept(): To accept a record from the user and add it to "Result.csv". Include a header.
#* wonCount(): To count the number of students who have won any event.

import csv

def Accept(st_id, st_name, game_name, result):
    with open("Result.csv", "a+", newline="") as f:
        reader = csv.reader(f)
        writer = csv.writer(f)

        if f.tell() == 0:
            writer.writerow(["St_Id", "St_Name", "Game_Name", "Result"])
            writer.writerow([st_id, st_name, game_name, result])
        else:
            writer.writerow([st_id, st_name, game_name, result])

Accept(1, "John", "Basketball", "Won")

def wonCount():
    count = 0
    with open("Result.csv", "r") as f:
        reader = csv.reader(f)
        skipped = False

        for row in reader:
            if skipped:
                if row[3] == "Won":
                    count += 1
            else:
                skipped = True
    
    print("Count:", count)

wonCount()
