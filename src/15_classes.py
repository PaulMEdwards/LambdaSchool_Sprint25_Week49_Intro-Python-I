# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

class LatLon:
    def __init__(self, lat, lon):
        super().__init__()
        self.lat = lat
        self.lon = lon
    def __str__(self):
        return f"Latitude: {self.lat}, Longitude: {self.lon}"

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name
        self.lat = lat
        self.lon = lon
    def __str__(self):
        n = f"Name: {self.name}"
        l = super().__str__()
        return f"{n}\n{l}"

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)
        self.name = name
        self.difficulty = difficulty
        self.size = size
        self.lat = lat
        self.lon = lon
    def __str__(self):
        w = super().__str__()
        g = f"Difficulty: {self.difficulty}, Size: {self.size}"
        return f"{w}\n{g}"

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

waypoint = Waypoint("Catacombs", 41.70505, -121.51521)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

geocache = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)

# Print it--also make this print more nicely
print(geocache)
