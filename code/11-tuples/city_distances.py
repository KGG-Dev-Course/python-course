home = ("Lisbon", 38.72, -9.14)
trips = [
    ("Porto", 41.15, -8.61),
    ("Madrid", 40.42, -3.70),
    ("Faro", 37.02, -7.93),
]

home_name, home_lat, home_lon = home
print(f"Starting from {home_name} at {home_lat}, {home_lon}")

for name, lat, lon in trips:
    # A rough distance: 111 km per degree, good enough for a quick estimate
    lat_km = (lat - home_lat) * 111
    lon_km = (lon - home_lon) * 87
    distance = (lat_km ** 2 + lon_km ** 2) ** 0.5
    print(f"{name}: about {distance:.0f} km")

first_trip = trips[0]
print(f"First trip on the list: {first_trip[0]}")
print(f"Number of trips planned: {len(trips)}")
