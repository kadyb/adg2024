import os 
import qgis.core
import math

path = os.path.join(os.path.expanduser("~"), "Documents", "dane")
os.chdir(path)

f = "DEM.tif"
raster = QgsRasterLayer(f, "DEM")
            
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

#x, y = xy_from_colrow(raster, 22, 18)


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

#colrow_from_xy(raster, x, y)