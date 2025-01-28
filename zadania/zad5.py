# poprawiona wersja 

import qgis.core as qc

dem = qc.QgsRasterLayer('dane/DEM.tif')
dem.isValid()

def cell_size(dem):
    cell_xsize = abs((dem.extent().width())/dem.width())
    cell_ysize = abs((dem.extent().height())/dem.height())
    
    return [cell_xsize, cell_ysize]

cell_size(dem)

