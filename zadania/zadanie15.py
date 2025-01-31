import math

def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c

lat_warszawa = 52.2296756
lon_warszawa = 21.0122287

lat_rzym = 41.9027835
lon_rzym = 12.4963655

odleglosc = haversine(lat_warszawa, lon_warszawa, lat_rzym, lon_rzym)
odleglosc_zaokraglona = round(odleglosc, 2)
print("Odległość między Warszawą a Rzymem wynosi:", odleglosc_zaokraglona, "km")
