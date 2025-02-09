'''
Zaimplementuj funkcję surface_distance(), która obliczy odległość powierzchniową
między punktami w przestrzeni trójwymiarowej. Następnie wykorzystaj ją do
obliczenia całkowitej długości profilu terenu zapisanego w pliku profil.csv w 
układzie EPSG:2180. Do wczytania pliku csv można wykorzystać moduł csv lub 
klasę QgsVectorLayer w QGIS.
'''

import os
from math import sqrt
import csv

path = "/Users/michalbaczkiewicz/Documents/GitHub/adg2024/dane/"
os.chdir(path)

file = "profil.csv"

def surface_distance(filepath):

    terrain_points = [] 
    with open(filepath, 'r', encoding='utf-8') as csv_file: 
        csv_reader = csv.DictReader(csv_file)
        for record in csv_reader: 
            x_coordinate = float(record["X"])
            y_coordinate = float(record["Y"])
            z_coordinate = float(record["Z"])
            terrain_points.append((x_coordinate, y_coordinate, z_coordinate))
    
    print(f"Wczytano {len(terrain_points)} punktów profilu.")

    profile_length = 0.0 

    for point_index in range(len(terrain_points) - 1):
        p1 = terrain_points[point_index]
        p2 = terrain_points[point_index + 1]
        segment_length = sqrt(
           (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 + (p2[2] - p1[2])**2
        )
        profile_length += segment_length
    
    return round(profile_length, 2)

profile_length = surface_distance(file)
print(f"Całkowita długość profilu wynosi: {profile_length}")