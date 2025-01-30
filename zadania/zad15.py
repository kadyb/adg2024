'''
Zaimplementuj wzór haversine [9] jako funkcję i porównaj z innymi otrzymanymi 
wynikami na przykładzie odległości pomiędzy Warszawą a Rzymem. Współrzędne 
geograficzne wyrażone w stopniach muszą zostać zamienione na radiany.
'''

import os
from math import *

waw_coords = (21.0122, 52.2296)
rm_coords = (12.5113, 41.8919)

def calculate_distance(point1, point2):
    earth_radius = 6371009
    if not (type(point1) in [tuple, list] and type(point2) in [tuple, list]):
        return None
    longitude1, latitude1, longitude2, latitude2 = [radians(coord) for coord in [point1[0], point1[1], point2[0], point2[1]]]
    delta_longitude = longitude2 - longitude1
    delta_latitude = latitude2 - latitude1
    distance_meters = 2 * earth_radius * asin(sqrt((1 - cos(delta_latitude) + cos(latitude1) * cos(latitude2) * (1 - cos(delta_longitude))) / 2))
    distance_kilometers = distance_meters / 1000
    return round(distance_kilometers, 2)

distance_waw_rm = calculate_distance(waw_coords, rm_coords)

if distance_waw_rm is not None:
  print(f"Odległość między Warszawą a Rzymem wynosi: {distance_waw_rm} km")
else:
    print("Nie można obliczyć odległości. Sprawdź poprawność danych wejściowych.")

