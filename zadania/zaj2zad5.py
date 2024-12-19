#Napisz funkcję, która obliczy wielkość komórki na podstawie zakresu 
#przestrzennego oraz liczby kolumn i wierszy rastra.

import os
from qgis.core import QgsRasterLayer, QgsApplication

path = os.path.join("/Users/michalbaczkiewicz/Documents/GitHub/adg2024/dane")
os.chdir(path)

rasterfile = "DEM.tif"
raster = QgsRasterLayer(rasterfile, "DEM")

if not raster.isValid():
    print("Nie udało się wczytać warstwy raster")
else:
    print("Warstwa raster wczytana pomyślnie")

def cell_size(raster):
    w = raster.width()
    h = raster.height()
    e = raster.extent()
    e_w = e.width()
    e_h = e.height()
    x = e_w / w
    y = e_h / h
    return x, y

w, h = cell_size(raster)
print(f"Wielkość komórki: szerokość = {w}, wysokość = {h}")

