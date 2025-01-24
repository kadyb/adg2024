# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 11:08:10 2025

@author: krzys
"""

from shapely.geometry import Polygon
from shapely.affinity import translate, scale
import matplotlib.pyplot as plt

# Definicja funkcji do rysowania poligonu
def plot_polygon(polygon, title):
    x, y = polygon.exterior.xy
    plt.plot(x, y, label=title)
    plt.fill(x, y, alpha=0.5)

# Definicja oryginalnego poligonu
original_polygon = Polygon([(40, 30), (60, 30), (50, 40), (40, 30)])

# Przesunięcie poligonu o dx=10 i dy=5
shifted_polygon = translate(original_polygon, xoff=10, yoff=5)

# Skalowanie poligonu względem jego centroidu o współczynnik 1.5
scaled_polygon = scale(original_polygon, xfact=1.5, yfact=1.5, origin='centroid')

# Rysowanie oryginalnego i przekształconych poligonów
plt.figure()
plot_polygon(original_polygon, 'Oryginalny Poligon')
plot_polygon(shifted_polygon, 'Przesunięty Poligon')
plot_polygon(scaled_polygon, 'Skalowany Poligon')
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Transformacje Geometrii Poligonu')
plt.grid(True)
plt.show()
