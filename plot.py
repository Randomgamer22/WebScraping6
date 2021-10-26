import matplotlib.pyplot as plt
import csv

all_star_data = []

with open('main.csv', 'r') as f:
    csv_reader = csv.reader(f)

    all_star_data = list(csv_reader)[1:]

mass_list = []
radius_list = []
gravity_list = []

for index, star_data in enumerate(all_star_data):
    if len(star_data) == 0:
        del all_star_data[index]

for star_data in all_star_data:
    mass_list.append(star_data[3])
    radius_list.append(star_data[4])
    gravity_list.append(star_data[5])

def convert_to_float_list(given_list):
    for index, item in enumerate(given_list):
        given_list[index] = float(item)
    return given_list

mass_list = convert_to_float_list(mass_list)
radius_list = convert_to_float_list(radius_list)
gravity_list = convert_to_float_list(gravity_list)

mass_list.sort()
radius_list.sort()
gravity_list.sort()

mr = plt.figure()

plt.scatter(mass_list, radius_list)
plt.xlabel("Mass of Star")
plt.ylabel("Radius of Star")
plt.title("Mass - Radius relation of Star")
plt.savefig("mass_radius_relation.png")

mg = plt.figure()

plt.scatter(mass_list, gravity_list)
plt.xlabel("Mass of Star")
plt.ylabel("Gravity of Star")
plt.title("Mass - Gravity relation of Star")
plt.savefig("mass_gravity_relation.png")

