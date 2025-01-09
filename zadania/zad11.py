import os
import qgis.core as qc
import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication
import random
app = QApplication(sys.argv)

path = os.path.join(os.path.expanduser('~'),'algorytmy_geo')
os.chdir(path)
path_data = os.path.join(path,'dane')

def GetZValue(vals,raster):
    z_value = np.array([])
    for i in range(len(vals)):
        sample = raster.dataProvider().sample(qc.QgsPointXY(vals[i][0],vals[i][1]),1)
        z_value = np.append(z_value, [sample[0]])
        
    return z_value

rast = qc.QgsRasterLayer(os.path.join(path_data,'DEM.tif'))

# tworzenie tablicy numpy z wartości rastra
block = rast.dataProvider().block(1, rast.extent(), rast.width(), rast.height())
array = np.frombuffer(block.data(), dtype = np.float32)
array = array.reshape(rast.height(), rast.width())

# jako transekty posłużyły linie wsch-zach i płn-płd, położone w centralnej częśći rastra
x_cent_mean = (rast.extent().xMaximum() + rast.extent().xMinimum()) / 2
y_cent_mean = (rast.extent().yMaximum() + rast.extent().yMinimum()) / 2

# każda lista zawiera koorydnaty X,Y (może też Z,M, więcej tutaj:
# https://qgis.org/pyqgis/3.40/core/QgsLineString.html#qgis.core.QgsLineString)
ns = np.linspace([x_cent_mean,(rast.extent().yMaximum())],[x_cent_mean,(rast.extent().yMinimum())],50)
ew = np.linspace([(rast.extent().xMaximum()),y_cent_mean],[(rast.extent().xMinimum()),y_cent_mean],50)

# wydobywanie wartości Z
ns_z = GetZValue(ns, rast)
ew_z = GetZValue(ew, rast)

# maskowanie braku wartości rastra
nadata = rast.dataProvider().sourceNoDataValue(1)
data = np.ma.masked_values(array, nadata)

ext = [rast.extent().xMinimum(), rast.extent().xMaximum(), rast.extent().yMinimum(), rast.extent().yMaximum()] # zasięg rastra

# tworzenie wykresu
gridSpec = {"width_ratios":(3,1), 
            "height_ratios":(1,3),
            "wspace":0.4,"hspace":0.1}
figsize = (rast.width()/200,rast.height()/200)
fig, axes = plt.subplots(2,2,figsize=figsize,gridspec_kw=gridSpec)
axes[1][0].plot(*ns.T,color="#F00")
axes[1][0].plot(*ew.T,color="#F00")
axes[1][0].imshow(data,extent=ext)
axes[0][0].plot(ew,ew_z)
axes[1][1].plot(ns_z,ns)
axes[0][1].set_axis_off()
axes[0][0].xaxis.set_visible(False)
axes[1][1].yaxis.set_visible(False)
axes[1][1].tick_params(labeltop=True, labelbottom=False)
plt.show()
