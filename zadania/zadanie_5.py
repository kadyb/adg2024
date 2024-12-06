raster = QgsRasterLayer('dane/DEM.tif')
print(raster.isValid())

zakres = raster.extent()

test = zakres.xMinimum()

lk = raster.width()
roz_x = ((zakres.xMaximum() - zakres.xMinimum()) / lk)

raster.width()

def cell_size(x):
    lk = x.width()
    lw = x.height()
    zakres = x.extent()
    
    roz_x = ((zakres.xMaximum() - zakres.xMinimum()) / lk)
    
    roz_y = ((zakres.yMaximum() - zakres.yMinimum()) / lw)
    
    print(roz_x, roz_y)
    
    
cell_size(raster)
