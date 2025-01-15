import os
from qgis.core import (
    QgsProject,
    QgsRasterLayer,
    QgsGeometry,
    QgsPointXY,
    QgsLineString,
    QgsFeature,
    QgsVectorLayer,
    QgsCoordinateReferenceSystem,
    QgsCoordinateTransformContext,
)
import numpy as np
import matplotlib.pyplot as plt

os.chdir('C:/Users/kacpe/OneDrive/Pulpit/Studia/Geoinformacja/III rok/Semestr zimowy/Algorytmy')

#wczytanie dem
dem_layer = QgsRasterLayer("DEM.tif")

#Funkcja do interpolacji wartości wysokości wzdłuż linii
def sample_along_line(line, dem_layer, interval=10):
    points = []
    distances = []
    values = []
    
    length = line.length()
    distance = 0
    
    while distance <= length:
        point = line.interpolate(distance)
        points.append(point.asPoint())
        distances.append(distance)
        
        # Pobieranie wartości wysokości
        result = dem_layer.dataProvider().sample(point.asPoint(), 1)
        value = result[0]
        if np.isnan(value):  # Obsługa brakujących wartości
            values.append(0)  # Można zmienić na inną wartość zastępczą lub interpolować
        else:
            values.append(value)
        
        distance += interval
    
    return distances, values

#Definiowanie transektów (linie)
extent = dem_layer.extent()
crs = QgsCoordinateReferenceSystem(dem_layer.crs())
line_ns = QgsGeometry.fromPolylineXY([
    QgsPointXY(extent.center().x(), extent.yMinimum()),
    QgsPointXY(extent.center().x(), extent.yMaximum())
])
line_ew = QgsGeometry.fromPolylineXY([
    QgsPointXY(extent.xMinimum(), extent.center().y()),
    QgsPointXY(extent.xMaximum(), extent.center().y())
])

#Próbkowanie wzdłuż transektów
interval = 10  # Interwał w metrach
distances_ns, values_ns = sample_along_line(line_ns, dem_layer, interval)
distances_ew, values_ew = sample_along_line(line_ew, dem_layer, interval)

#Tworzenie wykresu
plt.figure(figsize=(10, 6))

#Transekt północ-południe
plt.subplot(2, 1, 1)
plt.plot(distances_ns, values_ns, label="Transect N-S", color="blue")
plt.xlabel("Odległość [m]")
plt.ylabel("Wysokość [m n.p.m.]")
plt.title("Profil terenu: transekt N-S")
plt.grid(True)

#Transekt wschód-zachód
plt.subplot(2, 1, 2)
plt.plot(distances_ew, values_ew, label="Transect E-W", color="green")
plt.xlabel("Odległość [m]")
plt.ylabel("Wysokość [m n.p.m.]")
plt.title("Profil terenu: transekt E-W")
plt.grid(True)

plt.tight_layout()
plt.show()