
import math

def haversine(coord1, coord2):
    r = 6371  # Promień Ziemi w kilometrach
    
    # Zamiana stopni na radiany
    lat1, lon1 = map(math.radians, coord1)
    lat2, lon2 = map(math.radians, coord2)

    # Różnica współrzędnych
    delta_lat = lat2 - lat1
    delta_lon = lon2 - lon1

    # Wzór haversine
    a = math.sin(delta_lat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(delta_lon / 2) ** 2
    c = 2 * math.asin(math.sqrt(a))

    return round(r * c, 3)

# Współrzędne Warszawy i Rzymu
warszawa = (52.2296, 21.0122)
rzym = (41.8916, 12.5113)

# Obliczenie odległości
print(haversine(warszawa, rzym))

