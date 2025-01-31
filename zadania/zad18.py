import os
import qgis.core as qc
import numpy as np
import matplotlib.pyplot as plt
from math import pi, sin, cos, radians

# obrót poligonu
def RotateGeom(geom, deg): # wokół centroidu
    if qc.QgsGeometry.wkbType(geom) != qc.Qgis.WkbType(3):
        raise TypeError('Nieobsługiwana geometria!')
    px = geom.centroid().asPoint()[0]   
    py = geom.centroid().asPoint()[1]
    geom_np = geom.as_numpy()
    z,y,x = geom_np.shape
    geom_np = geom_np.reshape(y,x)
    radian = (deg*pi/180)
    x_np = np.array([])
    y_np = np.array([])
    for xy in geom_np:    
        x_np = np.append(x_np,(xy[0]-px) * cos(radian) - (xy[1]-py) * sin(radian) + px)
        y_np = np.append(y_np,(xy[0]-px) * sin(radian) + (xy[1]-py) * cos(radian) + py)

    geom_np_rotated = np.column_stack((x_np,y_np))
    return geom_np_rotated

# przeskalowanie poligonu
def RescaleGeom(geom, x_factor, y_factor):
    if qc.QgsGeometry.wkbType(geom) != qc.Qgis.WkbType(3):
        raise TypeError('Nieobsługiwana geometria!')
    px = geom.centroid().asPoint()[0]   
    py = geom.centroid().asPoint()[1]
    geom_np = geom.as_numpy()
    z,y,x = geom_np.shape
    geom_np = geom_np.reshape(y,x)
    x_np = np.array([])
    y_np = np.array([])
    for xy in geom_np:    
        x_np = np.append(x_np, x_factor * (xy[0]-px) + px)
        y_np = np.append(y_np, y_factor * (xy[1]-py) + py)

    geom_np_rescaled = np.column_stack((x_np,y_np))
    return geom_np_rescaled

# tworzenie geometrii, nadawanie parametrów oraz przywoływanie funkcji
geom = qc.QgsGeometry.fromWkt("POLYGON ((40 30, 60 30, 50 40, 40 30))")
deg = 90
factors = (0.6,0.6)
rotated_geom = RotateGeom(geom, deg)
rescaled_geom = RescaleGeom(geom,*factors)

# wizualizacja
geom_np = geom.as_numpy() # do łatwiejszego zarządzania

plt.figure(figsize = (4, 3))
plt.plot(geom_np[:,0], geom_np[:,1], color = "grey", linestyle = "dashed", zorder = 1)
plt.fill(rotated_geom[:,0], rotated_geom[:,1], color = "blue", zorder = 2)
plt.title('Figura obrócona o {}'.format(deg))
plt.show()

plt.figure(figsize = (4, 3))
plt.plot(geom_np[:,0], geom_np[:,1], color = "grey", linestyle = "dashed", zorder = 1)
plt.fill(rescaled_geom[:,0], rescaled_geom[:,1], color = "blue", zorder = 2)
plt.title('Figura po zmianie rozmiaru do {}% swojej szerokości\n\
oraz {}% swojej wysokości'.format(factors[0]*100,factors[1]*100))
plt.show()
