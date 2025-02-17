#Napisz funkcje xy_from_colrow() oraz colrow_from_xy(), 
#które umożliwią transformację kolumn i wierszy na współrzędne geograficzne 
#oraz transformację w drugą stronę. Uwzględnij warunek sprawdzający 
#czy szukane parametry znajdują się w zakresie rastra, tj. nie wychodzą poza jego zasięg.
#Marcel Tomczak 3 GI
import os
import math

path = os.path.join(os.path.expanduser("~"), "Documents", "adp", "dane8")
os.chdir(path)

rastername = "DEM.tif"
raster = QgsRasterLayer(rastername)

def xy_from_colrow(raster):
    x_res = raster.rasterUnitsPerPixelX()
    y_res = raster.rasterUnitsPerPixelY()
    ext = raster.extent()
    x_min = ext.xMinimum()
    y_max = ext.yMaximum()
    cols = raster.width()
    rows = raster.height()
    coordinates = []

    for row in range(rows):
        for column in range(cols):
            x = x_min + (column + 0.5) * x_res
            y = y_max - (row + 0.5) * abs(y_res)
            coordinates.append([x, y])
    return coordinates


def colrow_from_xy(raster, coordinates):
    x_res = raster.rasterUnitsPerPixelX()
    y_res = raster.rasterUnitsPerPixelY()
    ext = raster.extent()
    x_min = ext.xMinimum()
    y_max = ext.yMaximum()
    colrow = []

    for coord in coordinates:
        x, y = coord
        if not (x_min <= x <= ext.xMaximum() and ext.yMinimum() <= y <= y_max):
            raise ValueError("Współrzędne nie sa w zakresie rastra")

        col = math.floor((x - x_min) / x_res)
        row = math.floor((y_max - y) / abs(y_res))
        colrow.append([col, row])
    return colrow

wynik = xy_from_colrow(raster)
print(f"5 pierwszych współrzędnych geograficznych: {wynik[:5]}")
    
wynik2 = colrow_from_xy(raster, wynik)
print(f"5 pierwszych kolumny i wierszy: {wynik2[:5]}")

