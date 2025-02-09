from math import *

def haversine_dist(pt1, pt2):
    r = 6371009
    if type(pt1) in [tuple, list] and type(pt2) in [tuple, list]:
        coords = [pt1[0], pt1[1], pt2[0], pt2[1]]
        coords = [radians(coord) for coord in coords]
        x1, y1, x2, y2 = coords
        distance = 2 * r * asin(sqrt((1 - cos(y2-y1) + cos(y1)*cos(y2) * (1 - cos(x2-x1)))/2))
        distance_km = distance / 1000
        return round(distance_km, 2)
    else:
        print("Współrzędne punktów powinny być podane w formie krotek lub list")

warsaw = (21.0122, 52.2296)
rome = (12.5113, 41.8919)

haversine_dist(warsaw, rome)