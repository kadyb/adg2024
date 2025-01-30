import os 
from math import sqrt
import csv

path = os.path.join(os.path.expanduser("~"), "Documents", "dane")
os.chdir(path)

file = "profil.csv"

def surface_distance(file):
    points = []
    with open(file) as file_csv:
        reader = csv.DictReader(file_csv)
        for row in reader:
            x, y, z = float(row["X"]), float(row["Y"]), float(row["Z"])
            points.append((x, y, z))
    
    for point in range(len(points)):
        if point == 0:
            dist = 0
        else:
            x1, y1, z1 = points[point - 1]
            x2, y2, z2 = points[point]
            dist += sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    return round(dist, 2)

surface_distance("profil.csv")
