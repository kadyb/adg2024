import math
from qgis.core import QgsRasterLayer

def xy_from_colrow(raster, col, row):
    extent = raster.extent()
    width = raster.width()
    height = raster.height()
    x_res = extent.width() / width
    y_res = extent.height() / height
    if not (0 <= col < width and 0 <= row < height):
        raise ValueError("Podane indeksy wykraczają poza zakres rastra.")
    x_min = extent.xMinimum()
    y_max = extent.yMaximum()
    x = x_min + (col + 0.5) * x_res
    y = y_max - (row + 0.5) * y_res
    return x, y

def colrow_from_xy(raster, x, y):
    extent = raster.extent()
    width = raster.width()
    height = raster.height()
    x_res = extent.width() / width
    y_res = extent.height() / height
    if not (extent.xMinimum() <= x <= extent.xMaximum() and extent.yMinimum() <= y <= extent.yMaximum()):
        raise ValueError("Podane współrzędne wykraczają poza zakres rastra.")
    x_min = extent.xMinimum()
    y_max = extent.yMaximum()
    col = math.floor((x - x_min) / x_res)
    row = math.floor((y_max - y) / y_res)
    return col, row

raster = QgsRasterLayer("C:/Users/kacpe/OneDrive/Pulpit/Studia/Geoinformacja/III rok/Semestr zimowy/Algorytmy/DEM.tif")

col, row = 10, 20
x, y = xy_from_colrow(raster, col, row)
print(x,y)
col_row = colrow_from_xy(raster, x, y)
print(col,row)