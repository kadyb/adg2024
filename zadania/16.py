import os
import numpy as np
import csv
from math import sqrt, cos, sin, asin
fpath = r"C:\Users\jmpos\Desktop\adp"
os.chdir(fpath)

with open("profil.csv", 'r') as x:
    profil = list(csv.reader(x, delimiter=","))

profil = np.array(profil)
profil = np.delete(profil, 0, axis=0)
profil = profil.astype(np.float64)

def dist_2points(p1, p2):
    dX = p2[0] - p1[0]
    dY = p2[1] - p1[1]
    dZ = p2[2] - p1[2]
    dist = sqrt(dX **2 + dY **2 + dZ **2)
    
    return dist

def surface_distance(profil):
    dist = 0
    i = 0
    while i < len(profil) - 1:
        dist += dist_2points(profil[i][1:4],profil[i + 1][1:4])
        i += 1
        
    return dist

print(surface_distance(profil))