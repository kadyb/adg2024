import os
from qgis.core import QgsRasterLayer
from qgis.core import QgsProject

path_raster = r"C:\Users\jmpos\Desktop\adp\dem.tif"


def xy_from_colrow(path_raster, col, row):
    raster = QgsRasterLayer(path_raster)
    uX = raster.rasterUnitsPerPixelX()
    uY = raster.rasterUnitsPerPixelY()
    width = raster.width()
    height = raster.height()
    x = raster.extent().xMinimum() + (uX / 2)
    y = raster.extent().yMinimum() + (uY / 2)
    
    if col > width or row > height:
        raise ValueError("Niepoprawne wymiary")
    
    for i in range(col - 1):
        x += uX
    
    for i in range(row - 1):
        y += uY
    
    return x, y

x, y = xy_from_colrow(path_raster, 99,342)


def colrow_from_xy(path_raster, x, y):
    raster = QgsRasterLayer(path_raster)
    
    if x < raster.extent().xMinimum() or x > raster.extent().xMaximum():
        raise ValueError("x poza obszarem rastra")
    if y < raster.extent().yMinimum() or y > raster.extent().yMaximum():
        raise ValueError("y poza obszarem rastra")
    
    x -= raster.extent().xMinimum()
    y -= raster.extent().yMinimum()
    x /= raster.rasterUnitsPerPixelX()
    y /= raster.rasterUnitsPerPixelY()
    col = int(x + 1 - (x % 1))
    row = int(y + 1 - (y % 1))
    
    return col, row


col, row = colrow_from_xy(path_raster, x, y)





