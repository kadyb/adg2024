import os
import math
from qgis.core import QgsRasterLayer, QgsPointXY

#sciezka do rastra
dem_file = "C:/Users/krzys/Pulpit/algorytmy_danych/zaj4/DEM.tif"
dem_layer = QgsRasterLayer(dem_file, "DEM")

def convert_colrow_to_xy(raster, column, row):
    extent = raster.extent()
    x_min, x_max, y_min, y_max = extent.xMinimum(), extent.xMaximum(), extent.yMinimum(), extent.yMaximum()
    x_res, y_res = raster.rasterUnitsPerPixelX(), raster.rasterUnitsPerPixelY()
     
    if column < 0 or row < 0 or column >= raster.width() or row >= raster.height():
        raise ValueError("Wartości są poza zasięgiem rastra!")
    x = x_min + (column + 0.5) * x_res
    y = y_max + (row + 0.5) * y_res
    
    return x, y
    
def convert_xy_to_colrow(raster, x, y):
    extent = raster.extent()
    x_min, x_max, y_min, y_max = extent.xMinimum(), extent.xMaximum(), extent.yMinimum(), extent.yMaximum()
    x_res, y_res = raster.rasterUnitsPerPixelX(), raster.rasterUnitsPerPixelY()
    
    if x < x_min or x > x_max or y < y_min or y > y_max:
        raise ValueError("Współrzędnie są poza zasięgiem rastra!")
    
    column = math.floor((x - x_min) / x_res)
    row = math.floor ((y_max - y) / y_res)
    
    return column, row

column = 10
row = 20

#  wywolanie funkcji kownetrująca kolumny, wiersze -> wspolrzedne
x, y = convert_colrow_to_xy(dem_layer, column, row)
print(f"Współrzędne geograficzne dla kolumny {column} i wiersza {row}: ({x}, {y})")

# Wywołanie funkcji konwertująca wspolrzedne -> indeksy, kolumny, wiersze
column_new, row_new = convert_xy_to_colrow(dem_layer, x, y)
print(f"Indeksy kolumny i wiersza dla współrzędnych ({x}, {y}): Kolumna = {column_new}, Wiersz = {row_new}")
