#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 11:56:17 2024
"""
#%% zadanie 5 (zadanie 1 z ćwiczenia 2)

from qgis.core import QgsRasterLayer

dem = QgsRasterLayer('dane/DEM.tif')
dem.isValid()

def cell_size(dem):
    xsize = dem.width()
    ysize = dem.height()
    ext = dem.extent().toString() # zwraca zasięg w postaci str
    ext = ext.replace(' : ' ,',') # poprawki 
    ext = ext.split(',') # rozdzielenie wartości
    ext = [float(ext[i]) for i in range(len(ext))] # z str to float
    cell_xsize = abs((ext[2]-ext[0])/xsize)
    cell_ysize = abs((ext[3]-ext[1])/ysize)
    
    return [cell_xsize, cell_ysize]

cell_size(dem)
