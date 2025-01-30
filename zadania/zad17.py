import os
import qgis.core as qc
from math import floor

path = os.path.join(os.path.expanduser('~'),'algorytmy_geo')
os.chdir(path)

raster = qc.QgsRasterLayer(os.path.join(path,'dane','DEM.tif')) # przykładpwy


def XYfromColRow(raster,col,row):
    if col > raster.height()-1 or row > raster.width()-1: # bo się liczy od zera
        return "Wartości wykraczają poza zasięg rastra!"
    else:    
        x = raster.extent().xMinimum() + (col+0.5) * raster.rasterUnitsPerPixelX()
        y = raster.extent().yMaximum() - (row+0.5) * raster.rasterUnitsPerPixelY()
        return x, y


def ColRowFromXY(raster,x,y):
    if raster.extent().xMinimum() <= x <= raster.extent().xMaximum() or\
    raster.extent().yMinimum() <= y <= raster.extent().yMaximum(): 
        col = floor((x-raster.extent().xMinimum())/raster.rasterUnitsPerPixelX())
        row = floor((raster.extent().yMaximum()-y)/raster.rasterUnitsPerPixelY())
        return col, row
    else:
        return "Wartości wykraczają poza zasięg rastra!"
        

# przykład
ex_x, ex_y = XYfromColRow(raster, 532, 607) # dolny prawy róg
ex_col, ex_row = ColRowFromXY(raster, ex_x, ex_y) # zwróci 532, 607
