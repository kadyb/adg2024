# AD 17
import math
import os

path = os.path.join(os.path.expanduser("~"), "OneDrive", "Dokumenty", "adg", "dane")
os.chdir(path)

raster = QgsRasterLayer("DEM.tif")
print(raster.isValid)

def xy_from_colrow(raster, col, row):
    cols = raster.width()
    rows = raster.height()
    if col <= cols and row <= rows:
        extent = raster.extent()
        xmin = extent.xMinimum()
        ymax = extent.yMaximum()
        xres = (extent.xMaximum() - extent.xMinimum())/cols
        yres = (extent.yMaximum() - extent.yMinimum())/rows
        x =  xmin + (col + 0.5) * xres
        y = ymax - (row + 0.5) * yres
        return print(f"{x},{y}")
    else:
        print("Podane parametry nie znajduje się w zakresie rastra.")
    
def colrow_from_xy(raster, x, y):
    wid = raster.width()
    hei = raster.height()
    extent = raster.extent()
    xmin = extent.xMinimum()
    ymax = extent.yMaximum()
    if x >= xmin and y <= ymax:
        xres = (extent.xMaximum() - extent.xMinimum())/wid
        yres = (extent.yMaximum() - extent.yMinimum())/hei
        col = math.floor((x - xmin)/xres)
        row = math.floor((ymax - y)/yres)
        return print(f"{col},{row}")
    else:
        print("Podane parametry nie znajduje się w zakresie rastra.")