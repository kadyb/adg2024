import os
from qgis import core
from osgeo import gdal, ogr, osr
import numpy as np
from matplotlib import pyplot as plt

path = os.path.join(os.path.expanduser("~"), "Documents", "dane")
os.chdir(path)

f = "DEM.tif"
raster = QgsRasterLayer(f, "DEM")
ext = raster.extent()

n = QgsPointXY(((ext.xMinimum() + ext.xMaximum())/2), ext.yMaximum() - 1000)
s = QgsPointXY(((ext.xMinimum() + ext.xMaximum())/2), ext.yMinimum() + 1000)
ns = QgsGeometry(QgsLineString([n, s]))
length_ns = ns.length()

e = QgsPointXY(ext.xMinimum() + 1000, ((ext.yMinimum() + ext.yMaximum())/2))
w = QgsPointXY(ext.xMaximum() - 1000, ((ext.yMinimum() + ext.yMaximum())/2))
ew = QgsGeometry(QgsLineString([e, w]))
length_ew = ew.length()

interval_ns = raster.rasterUnitsPerPixelY()
interval_ew = raster.rasterUnitsPerPixelX()
distance_ns = 0
distance_ew = 0

vals_ns = []
vals_ew = []

while distance_ns <= length_ns:
    pt = ns.interpolate(distance_ns).asPoint()
    v = raster.dataProvider().sample(pt, 1)
    if np.isnan(v[0]):
        pass 
    else:
        vals_ns.append(v[0])
    distance_ns += interval_ns

while distance_ew <= length_ew:
    pt = ew.interpolate(distance_ew).asPoint()
    v = raster.dataProvider().sample(pt, 1)
    if np.isnan(v[0]):
        pass 
    else:
        vals_ew.append(v[0])
    distance_ew += interval_ew
    
import matplotlib.ticker as ticker
from matplotlib.axis import Axis  
ns_linspace = np.linspace(0, length_ns, len(vals_ns))
ew_linspace = np.linspace(0, length_ew, len(vals_ew))
ticks_x = ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x/1000))

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
ax1.plot(ns_linspace, vals_ns)
ax1.set_title("North - South")
ax1.set_xlabel("Distance [km]")
ax1.set_ylabel("Elevation [m a.s.l.]")
Axis.set_major_formatter(ax1.xaxis, ticks_x)
ax2.plot(ew_linspace, vals_ew)
ax2.set_title("East - West")
ax2.set_xlabel("Distance [km]")
ax2.set_ylabel("Elevation [m a.s.l.]")
Axis.set_major_formatter(ax2.xaxis, ticks_x)
fig.show()