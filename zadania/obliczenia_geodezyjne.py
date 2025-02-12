import math
import pandas as pd

def decimal_to_dms(decimal_degrees, is_lat):
    degrees = int(decimal_degrees)
    minutes = int((decimal_degrees - degrees) * 60)
    seconds = (decimal_degrees - degrees - minutes / 60) * 3600

    direction = ''
    if is_lat:
        direction = 'N' if degrees >= 0 else 'S'
    else:
        direction = 'E' if degrees >= 0 else 'W'

    return f"{abs(degrees)}°{abs(minutes)}'{abs(seconds):.2f}\" {direction}"

def haversine(angle):
    return (1 - math.cos(angle))/2

def haversineDistance(lat1, lon1, lat2, lon2):
    R = 6371.0

    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    
    anglePart = haversine(dlat) + (1 - haversine(dlat) - haversine(lat2_rad + lat1_rad))*haversine(dlon)
    distance = 2 * R * math.asin(math.sqrt(anglePart))
    
    return distance

def calculateTotalProfileDistance(profilTerenu):
    totalDistance = 0
    for i in range(1, len(profilTerenu)):
        point1 = profilTerenu.iloc[i - 1][['X', 'Y', 'Z']]
        point2 = profilTerenu.iloc[i][['X', 'Y', 'Z']]
        totalDistance += surfaceDistance(point2, point1)
        
    return totalDistance / 1000

def surfaceDistance(point1, point2):
    totalSum = 0
    for i in range(len(point1)):
        totalSum += (point2[i] - point1[i])**2
    return math.sqrt(totalSum)

def main():
    latitude = 52.2927
    longitude = 16.7335
    print(decimal_to_dms(latitude, True))
    print(decimal_to_dms(longitude, False))
    
    warsaw_lat, warsaw_lon = 52.2296756, 21.0122287
    rome_lat, rome_lon = 41.9027835, 12.4963655
    distance = haversineDistance(warsaw_lat, warsaw_lon, rome_lat, rome_lon)
    print(f"Odległość między Warszawą a Rzymem: {distance:.2f} km")
    
    
    csvPath = "C:/Users/tymon/OneDrive/Pulpit/Projects/Justyna/Algorytmy/Dane/profil.csv"
    profilTerenu = pd.read_csv(csvPath)
    
    totalDistance = calculateTotalProfileDistance(profilTerenu)
    print(f"Całkowita długość profulu terenu wynosi {totalDistance} km")
        

main()

