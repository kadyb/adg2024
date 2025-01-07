## przygotowanie danych
# biblioteki
import os
import numpy as np
import qgis.core as qc
import sys
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication
import qgis.analysis as qa
import processing as proc
app = QApplication(sys.argv)


# sciezki, wybranie plików
path = os.path.join(os.path.expanduser('~'),'algorytmy_geo')
os.chdir(path)

path2 = os.path.join(path,'dane')

files = os.listdir(path2)
landsat_files = [i for i in files if i.endswith('.TIF')]
landsat_files.sort()

# wczytanie, stworzenie okien dla rastrów. UWAGA NALEŻY ZDEFINIOWAĆ NAZWĘ WARSTWY

B2 = qc.QgsRasterLayer(os.path.join(path2, landsat_files[0]), 'B2') #R
B3 = qc.QgsRasterLayer(os.path.join(path2, landsat_files[1]), 'B3') #G
B4 = qc.QgsRasterLayer(os.path.join(path2, landsat_files[2]), 'B4') #B
B8 = qc.QgsRasterLayer(os.path.join(path2, landsat_files[3]), 'B8') # panchromatyczny

# B2.isValid() # - przetestować

## FUNKCJE DO PROCESSINGU

def CreateRect(raster,xsize_left,ysize_up,xsize_right=0,ysize_down=0):
    xsize_right = xsize_left
    ysize_down = ysize_up
    extent = raster.extent()
    ext_x_min = (extent.xMaximum()+extent.xMinimum())/2-xsize_left*(raster.rasterUnitsPerPixelX())
    ext_x_max = (extent.xMaximum()+extent.xMinimum())/2+xsize_right*(raster.rasterUnitsPerPixelX())
    ext_y_min = (extent.yMaximum()+extent.yMinimum())/2-ysize_up*(raster.rasterUnitsPerPixelY())
    ext_y_max = (extent.yMaximum()+extent.yMinimum())/2+ysize_down*(raster.rasterUnitsPerPixelY())
    rect = qc.QgsRectangle(ext_x_min,ext_y_min,ext_x_max,ext_y_max)
    return rect

def CreateQgsBlock(raster,rect):
    provider = raster.dataProvider()
    width = int(rect.width() / raster.rasterUnitsPerPixelX())
    height = int(rect.height() / raster.rasterUnitsPerPixelY())
    block = provider.block(1, rect, width, height)
    return block

def SaveRaster(raster,block,rect):
    file_name = os.path.join(path2,'block_temp_'+raster.name()+'.tif')
    pipe = qc.QgsRasterPipe()
    provider = raster.dataProvider()
    pipe.set(provider.clone())
    writer = qc.QgsRasterFileWriter(file_name)
    writer.setCreateOptions(["COMPRESS=LZW"])
    writer.setOutputFormat("GTiff")
    status = writer.writeRaster(
        pipe,
        block.width(),
        block.height(),
        rect,
        raster.crs(),
        qc.QgsCoordinateTransformContext()
    )
    if status != 0:
        print("Błąd zapisu")
    else: 
        print("OK")

## processing

# tworzenie zasięgu (opartego o QgsRectangle)
rectB2 = CreateRect(B2,500,500)
rectB3 = CreateRect(B3,500,500)
rectB4 = CreateRect(B4,500,500)
rectB8 = CreateRect(B8,1000,1000)

# tworzenie bloku
blockB2 = CreateQgsBlock(B2,rectB2)
blockB3 = CreateQgsBlock(B3,rectB3)
blockB4 = CreateQgsBlock(B4,rectB4)
blockB8 = CreateQgsBlock(B8,rectB8)

# zapis
SaveRaster(B2, blockB2, rectB2)
SaveRaster(B3, blockB3, rectB3)
SaveRaster(B4, blockB4, rectB4)
SaveRaster(B8, blockB8, rectB8)


## algebra
 
# wczytywanie zapisanych rastrów
newB2 = qc.QgsRasterLayer(os.path.join(path2,'block_temp_'+B2.name()+'.tif'),'B2')
newB3 = qc.QgsRasterLayer(os.path.join(path2,'block_temp_'+B3.name()+'.tif'),'B3')
newB4 = qc.QgsRasterLayer(os.path.join(path2,'block_temp_'+B4.name()+'.tif'),'B4')
newB8 = qc.QgsRasterLayer(os.path.join(path2,'block_temp_'+B8.name()+'.tif'),'B8')

def PansharpProcessing(sp_rast,pan_rast):
    output = os.path.join(path,'pansharp_'+sp_rast.name()+'.tif')
    pansharp_params = {"SPECTRAL": sp_rast,
                       "PANCHROMATIC": pan_rast,
                       "OUTPUT": output}
    proc.run('gdal:pansharp',pansharp_params)

PansharpProcessing(newB2, newB8)
PansharpProcessing(newB3, newB8)
PansharpProcessing(newB4, newB8)
