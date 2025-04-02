
#? Consider a dictionary called vehicle with the following key value pairs:
#* veh = {vtype: [brand, model, year, price], vtype: [brand, model, year, price], ...}
#? Write a program to accept the dictionary and count the number of vehicles released in 2020.
#? Also display all vehicles in alphabetical order with its brand name.

veh = {
    "car": ["Aston Martin", "DB12", 2020, 20000],
    "bike": ["Royal Enfield", "901B", 2025, 15000],
    "racecar": ["McLaren", "Senna", 2020, 10000],
    "truck": ["Ford", "F-150", 2019, 30000],
    "bus": ["Tata", "Bus", 2020, 40000],
    "jet": ["Lockheed Martin", "F22", 2020, 50000],
}


def vehicles_2020():
    count = 0
    for value in veh.values():
        if value[2] == 2020:
            count += 1

    print("Number of vehicles released in 2020:", count)


def vehicles_sorter():
    vehicles_list = list(veh.items())

    for vehicle in range(len(vehicles_list)):
        while vehicle > 0 and vehicles_list[vehicle - 1][1][0].lower() >= vehicles_list[vehicle][1][0].lower():
            vehicles_list[vehicle], vehicles_list[vehicle - 1] = vehicles_list[vehicle - 1], vehicles_list[vehicle]
            vehicle -= 1

    print(dict(vehicles_list))


vehicles_2020()
vehicles_sorter()
