import os
import math
from qgis.core import QgsRasterLayer, QgsPointXY

data_directory = "/Users/michalbaczkiewicz/Documents/GitHub/adg2024/dane/"
os.chdir(data_directory)

dem_file = "dem.tif"
dem_layer = QgsRasterLayer(dem_file, "DEM")

def xy_from_colrow(raster, column, row):
    ext = raster.extent()
    x_min, x_max, y_min, y_max = ext.xMinimum(), ext.xMaximum(), ext.yMinimum(), ext.yMaximum()
    x_res, y_res = raster.rasterUnitsPerPixelX(), raster.rasterUnitsPerPixelY()
    if column > x_max or row > y_max:
        print("Współrzędne nie są w zasięgu warstwy")
    else:
        x = x_min + (column + 0.5) * x_res
        y = y_max - (row + 0.5) * y_res
        return x, y

def colrow_from_xy(raster, x, y):
    ext = raster.extent()
    x_min, x_max, y_min, y_max = ext.xMinimum(), ext.xMaximum(), ext.yMinimum(), ext.yMaximum()
    x_res, y_res = raster.rasterUnitsPerPixelX(), raster.rasterUnitsPerPixelY()
    if x > x_max or y > y_max:
        print("Współrzędne nie są w zasięgu warstwy")
    else:
        column = math.floor((x - x_min)/x_res)
        row = math.floor((y_max - y)/y_res)
        return column, row

try:
    x, y = xy_from_colrow(raster, 10, 20)
    print(f"Współrzędne geograficzne: {x}, {y}")

    column, row = colrow_from_xy(raster, x, y)
    print(f"Indeksy kolumny i wiersza: Kolumna = {column}, Wiersz = {row}")
except ValueError as e:
    print(f"Błąd: {e}")