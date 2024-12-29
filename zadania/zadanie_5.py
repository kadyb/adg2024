import os
from qgis.core import QgsVectorLayer
from qgis.core import QgsRasterLayer

path = os.path.join(os.path.expanduser("~"),"Documents/adg/01")
os.chdir(path)

wektor = QgsVectorLayer("powiaty.gpkg")
raster = QgsRasterLayer("DEM.tif")

# 5 Napisz funkcję, która obliczy wielkość komórki na podstawie zakresu 
# przestrzennego oraz liczby kolumn i wierszy rastra 

def wielkosc_komorki(raster):
    cols = raster.width() # liczba kolumn
    rows = raster.height() # liczba wierszy
    extent = raster.extent() # zakres
    cell_size_x = (extent.xMaximum() - extent.xMinimum()) / cols
    cell_size_y = (extent.yMaximum() - extent.yMinimum()) / rows
    return f"Wiekość komórki: {cell_size_x}, {cell_size_y}"

wielkosc_komorki(raster)
