import sqlite3
import math

#connect to (or create) the database
conn = sqlite3.connect('cities.db')
cursor = conn.cursor()

#create table if not exists
cursor.execute('''
CREATE TABLE IF NOT EXISTS cities (
    name TEXT PRIMARY KEY,
    latitude REAL,
    longitude REAL
)
''')


def get_coordinates(city_name):
    #try to get city from database
    cursor.execute("SELECT latitude, longitude FROM cities WHERE name = ?", (city_name,))
    result = cursor.fetchone()

    if result:
        return result
    else:
        print(f"Coordinates for {city_name} not found.")
        lat = float(input(f"Enter latitude for {city_name}: "))
        lon = float(input(f"Enter longitude for {city_name}: "))
        cursor.execute("INSERT INTO cities (name, latitude, longitude) VALUES (?, ?, ?)",
                       (city_name, lat, lon))
        conn.commit()
        return (lat, lon)


def calculate_distance(coord1, coord2):
    # Haversine formula
    Radius_Earth = 6371  # Radius of Earth in kilometers

    lat1, lon1 = coord1
    lat2, lon2 = coord2

    # Convert degrees to radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    dlat = lat2 - lat1  # difference between the two latitudes
    dlon = lon2 - lon1  # difference between the two longitudes

    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(
        dlon / 2) ** 2  #part formula to find the shortest path between two points on a sphere
    c = 2 * math.atan2(math.sqrt(a),
                       math.sqrt(1 - a))  #part of formula to find the shortest path between two points on a sphere

    distance = Radius_Earth * c  #formula to find the shortest path between two points on a sphere
    return distance


def main():
    city1 = input("Enter the first city name: ").strip()
    city2 = input("Enter the second city name: ").strip()

    coord1 = get_coordinates(city1)
    coord2 = get_coordinates(city2)

    distance = calculate_distance(coord1, coord2)

    print(f"\nDistance between {city1} and {city2} is {distance:.2f} km")


if __name__ == '__main__':
    main()
