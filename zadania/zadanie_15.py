# zadanie 15
from math import radians, sin, cos, sqrt, atan2

def haversine_distance(lat1, lon1, lat2, lon2):
    # promień Ziemi w kilometrach
    R = 6371.009
    # konwersja na radiany
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    # Wzór haversine
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return round(R * c, 2)

# testowanie funkcji
warsaw = (52.2296, 21.0122)
rome = (41.8919, 12.5113)

distance = haversine_distance(warsaw[0], warsaw[1], rome[0], rome[1])
print("Odległość z Warszawy do Rzymu wynosi:", distance, "km")



