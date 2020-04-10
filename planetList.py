planet_list = ["Mercury", "Mars"]

# Use append() to add Jupiter and Saturn at the end of the list.

planet_list.append("Jupiter")
planet_list.append("Saturn")

# Use the extend() method to add another list of the last two planets in our solar system to the end of the list.

planet_list.extend(["Uranus", "Neptune"])

# Use insert() to add Earth, and Venus in the correct order.

planet_list.insert(1, "Earth")
planet_list.insert(1, "Venus")

# Use append() again to add Pluto to the end of the list.

planet_list.append("Pluto")

# Now that all the planets are in the list, slice the list in order to get the rocky planets into a new list called rocky_planets.

rocky_planets = planet_list[0:4]

# Being good amateur astronomers, we know that Pluto is now a dwarf planet, so use the del operation to remove it from the end of planet_list.

del planet_list[-1]

print("planets:", planet_list)
print("rocky planets:", rocky_planets)

# Create another list containing tuples. Each tuple will hold the name of a spacecraft that we have launched, and the names of the planet(s) that it has visited, or landed on.

spacecraftList = [
    ("Mariner 4", ["Mars"]),
    ("Mariner 6", ["Mars"]),
    ("Mariner 7", ["Mars"]),
    ("Mariner 8", ["Mars"]),
    ("Mariner 9", ["Mars"]),
    ("Spirit Rover", ["Mars"]),
    ("Oppurtunity Rover",["Mars"]),
    ("Sojourner Rover", ["Mars"]),
    ("Deep Space 2", ["Mars"]),
    ("Mars Reconnaissance Orbiter", ["Mars"]),
    ("Curiosity Rover", ["Mars"]),
    ("Mars Atmosphere and Volatile EvolutioN", ["Mars"]),
    ("Phoenix", ["Mars"]),
    ("Viking 1", ["Mars"]),
    ("Viking 2", ["Mars"]),
    ("Cassini-Huygens", ["Saturn"]),
    ("Galileo", ["Jupiter"]),
    ("Juno", ["Jupiter"]),
    ("Mariner 1", ["Venus"]),
    ("Mariner 2", ["Venus"]),
    ("Mariner 5", ["Venus"]),
    ("Mariner 10", ["Venus", "Mercury"]),
    ("Messenger", ["Venus", "Mercury"]),
    ("Pioneer 11", ["Jupiter", "Saturn"]),
    ("Voyager 1", ["Jupiter", "Saturn"]),
    ("Voyager 2", ["Jupiter", "Saturn", "Uranus", "Neptune"])
]

# Iterate over your list of planets, and inside that loop, iterate over the list of tuples. Print, for each planet, which satellites have visited it.

for planet in planet_list:
    satellites_visited = []
    for spacecraft, planets_visited in spacecraftList:
        if planet in planets_visited:
            satellites_visited.append(spacecraft)
    if len(satellites_visited) == 0:
            print(f"no satellites have visited {planet}")
    if len(satellites_visited) > 1:
            print(f"{satellites_visited} have visited {planet}")
        