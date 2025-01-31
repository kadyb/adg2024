import math

def spheric_dist(coord1, coord2):
    r = 6371
    
    delta_x = (coord2[0] - coord1[0]) * math.pi / 180.0
    delta_y = (coord2[1] - coord1[1]) * math.pi / 180.0
    
    lat1 = coord1[0] * math.pi / 180.0
    lat2 = coord2[0] * math.pi / 180.0
    
    stg1 = 1 - math.cos(delta_x) + (math.cos(lat2) * math.cos(lat1) * (1 - math.cos(delta_y)))
    
    stg2 = math.sqrt(stg1 / 2)
    
    stg3 = 2 * r * math.asin(stg2) #dystans w km
    
    return round(stg3, 3)

pt1 = (52.2296, 21.0122)
pt2 = (41.8919, 12.5113)

print(spheric_dist(pt1,pt2))

#wyliczony dystans wynosi 1315.506 km, czyli zbliżona do odległości sferycznej i elipsoidalnej ~1km