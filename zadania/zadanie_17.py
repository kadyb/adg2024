import os
import qgis.core as qg

path = os.path.join(os.path.expanduser("~"),"Documents/adg/06")
os.chdir(path)

# zad 17 Napisz funkcje xy_from_colrow() oraz colrow_from_xy(), które umożliwią transformację kolumn i wierszy na współrzędne geograficzne oraz transformację w drugą stronę. Uwzględnij warunek sprawdzający czy szukane parametry znajdują się w zakresie rastra, tj. nie wychodzą  poza jego zasięg.

raster = QgsRasterLayer("DEM.tif", "raster")
print(raster.isValid())

def xy_from_colrow(raster, column, row):
    cols = raster.width() # liczba kolumn
    rows = raster.height() # liczba wierszy
    if column < cols and row < rows:
        extent = raster.extent() # zakres
        x_min = extent.xMinimum()
        y_max = extent.yMaximum()
        x_res = (extent.xMaximum() - extent.xMinimum()) / cols
        y_res = (extent.yMaximum() - extent.yMinimum()) / rows
        x = x_min + (column + 0.5) * x_res
        y = y_max - (row + 0.5) * y_res
        return x,y
    else:
        print("podane kolumny i wiersze nie znajdują się w zakresie rastra")

xy_from_colrow(raster, 2, 2)
xy_from_colrow(raster, 2, 610)

def colrow_from_xy(raster, x, y):
    cols = raster.width() # liczba kolumn
    rows = raster.height() # liczba wierszy
    extent = raster.extent() # zakres
    x_max, x_min = extent.xMaximum(), extent.xMinimum()
    y_max, y_min = extent.yMaximum(), extent.yMinimum()
    if x >= x_min and x <= x_max and y >= y_min and y <= y_max:
        x_res = (x_max - x_min) / cols
        y_res = (y_max - y_min) / row
        column = int((x - x_min)/x_res)
        row = int((y_max - y)/y_res)
        return column, row
    else:
        print("podane współrzedne x i y nie znajdują się w zakresie rastra")

colrow_from_xy(raster, 254947.67406632268, 656321.4279236842)
colrow_from_xy(raster, 244947.67406632268, 656321.4279236842)
