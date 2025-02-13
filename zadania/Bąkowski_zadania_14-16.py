

def decimal_to_dms(decimal, is_latitude=True):
    """
    Konwertuje stopnie dziesiętne na wartość DMS z odpowiednim kierunkiem geograficznym.
    :param decimal: Wartość w stopniach dziesiętnych.
    :param is_latitude: Czy współrzędna to szerokość geograficzna (True) czy długość geograficzna (False).
    :return: String w formacie DMS.
    """
    # Kierunki geograficzne
    if is_latitude:
        direction = "N" if decimal >= 0 else "S"
    else:
        direction = "E" if decimal >= 0 else "W"
    
    # Konwersja na wartości absolutne
    decimal = abs(decimal)
    degrees = int(decimal)
    minutes = int((decimal - degrees) * 60)
    seconds = round((decimal - degrees - minutes / 60) * 3600, 2)
    
    return f"{degrees}°{minutes}'{seconds}\" {direction}"

# Testowanie funkcji
latitude_dd = 52.2296
longitude_dd = 21.0122

print(decimal_to_dms(latitude_dd))  # "52°13'46.56" N"
print(decimal_to_dms(longitude_dd, is_latitude=False))  # "21°0'43.92" E"



from math import radians, sin, cos, sqrt, atan2

def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Oblicza odległość pomiędzy dwoma punktami na kuli ziemskiej za pomocą wzoru haversine.
    :param lat1: Szerokość geograficzna punktu 1 (w stopniach).
    :param lon1: Długość geograficzna punktu 1 (w stopniach).
    :param lat2: Szerokość geograficzna punktu 2 (w stopniach).
    :param lon2: Długość geograficzna punktu 2 (w stopniach).
    :return: Odległość w kilometrach.
    """
    # Promień Ziemi w kilometrach
    R = 6371.009
    
    # Konwersja na radiany
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    
    # Wzór haversine
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    
    return round(R * c, 2)

# Testowanie funkcji
warsaw = (52.2296, 21.0122)
rome = (41.8919, 12.5113)

distance = haversine_distance(warsaw[0], warsaw[1], rome[0], rome[1])
print("Odległość między Warszawą a Rzymem:", distance, "km")
