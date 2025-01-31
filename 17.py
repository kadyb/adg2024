import math
import os
from qgis.core import QgsRasterLayer

# Wczytanie rastra
input = "C:\\Users\\mixer\\Downloads\\adg\\DEM.tif"
raster = QgsRasterLayer(input)

if not raster.isValid():
    print("Raster jest nieprawidłowy!")
else:
    print("Raster jest prawidłowy.")

def xy_from_colrow(raster, col, row):
    cols = raster.width()
    rows = raster.height()

    if col < 0 or col >= cols or row < 0 or row >= rows:
        print("Podane parametry nie znajdują się w zakresie rastra.")
        return None

    extent = raster.extent()
    xmin = extent.xMinimum()
    ymax = extent.yMaximum()
    xres = (extent.xMaximum() - extent.xMinimum()) / cols
    yres = (extent.yMaximum() - extent.yMinimum()) / rows

    x = xmin + (col + 0.5) * xres
    y = ymax - (row + 0.5) * yres

    return x, y

def colrow_from_xy(raster, x, y):
    extent = raster.extent()
    xmin = extent.xMinimum()
    ymax = extent.yMaximum()
    xmax = extent.xMaximum()
    ymin = extent.yMinimum()

    if x < xmin or x > xmax or y < ymin or y > ymax:
        print("Podane parametry nie znajdują się w zakresie rastra.")
        return None

    cols = raster.width()
    rows = raster.height()
    xres = (xmax - xmin) / cols
    yres = (ymax - ymin) / rows

    col = math.floor((x - xmin) / xres)
    row = math.floor((ymax - y) / yres)

    return col, row

# Przykład użycia
if raster.isValid():
    col, row = 50, 150
    xy_result = xy_from_colrow(raster, col, row)
    if xy_result:
        print(f"Współrzędne dla kolumny {col} i wiersza {row}: {xy_result}")

    x, y = 500000, 600000
    colrow_result = colrow_from_xy(raster, x, y)
    if colrow_result:
        print(f"Kolumna i wiersz dla współrzędnych ({x}, {y}): {colrow_result}")