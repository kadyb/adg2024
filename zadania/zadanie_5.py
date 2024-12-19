#ZADANIA

import os
path = os.path.join(os.path.expanduser("~"), "Documents", "adp", "dane")
os.chdir(path)

rastername = "DEM.tif"
raster=QgsRasterLayer(rastername)

print(raster.isValid())

def wielkosc_kom(raster):
    dlu = raster.width()
    wys = raster.height()
    ext = raster.extent()
    ext_d = ext.width()
    ext_w = ext.height()
    x = ext_d / dlu
    y = ext_w / wys
    return x, y

wielkosc_kom(raster)




