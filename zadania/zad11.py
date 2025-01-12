import os
from qgis.core import *
from qgis.analysis import *
import numpy as np
import matplotlib.pyplot as plt

data_directory = os.path.join("/Users/michalbaczkiewicz/Documents/GitHub/adg2024/dane")
os.chdir(data_directory)

dem_layer = QgsRasterLayer("DEM.tif", 'Model_Terenu')
QgsProject.instance().addMapLayer(dem_layer)

area_extent = dem_layer.extent()

north_south_line = QgsGeometry.fromPolylineXY([
    QgsPointXY(area_extent.center().x(), area_extent.yMaximum()), 
    QgsPointXY(area_extent.center().x(), area_extent.yMinimum())
])

east_west_line = QgsGeometry.fromPolylineXY([
    QgsPointXY(area_extent.xMinimum(), area_extent.center().y()), 
    QgsPointXY(area_extent.xMaximum(), area_extent.center().y())
])

ns_feature = QgsFeature()
ns_feature.setGeometry(north_south_line)

ew_feature = QgsFeature()
ew_feature.setGeometry(east_west_line)

transects_layer = QgsVectorLayer('LineString?crs=EPSG:2180', 'Przekroje_Terenu', 'memory')

layer_provider = transects_layer.dataProvider()
layer_provider.addFeatures([ns_feature, ew_feature])

QgsProject.instance().addMapLayer(transects_layer)

def extract_profile_values(raster, line, sample_points=100):
    elevation_values = []
    for i in range(sample_points):
        sampling_point = line.interpolate(line.length() / sample_points * i).asPoint()
        elevation = raster.dataProvider().identify(
            QgsPointXY(sampling_point),
            QgsRaster.IdentifyFormatValue
        ).results().get(1, None)
        elevation_values.append(elevation)
    return elevation_values

def handle_missing_values(data):
    data = np.array(data, dtype=float)
    missing_values = np.isnan(data)
    if missing_values.any():
        data[missing_values] = np.interp(
            np.flatnonzero(missing_values),
            np.flatnonzero(~missing_values),
            data[~missing_values]
        )
    return data

ns_elevations = extract_profile_values(dem_layer, north_south_line)
ew_elevations = extract_profile_values(dem_layer, east_west_line)

ns_elevations = handle_missing_values(ns_elevations)
ew_elevations = handle_missing_values(ew_elevations)

ns_distance = np.linspace(0, north_south_line.length(), len(ns_elevations))
ew_distance = np.linspace(0, east_west_line.length(), len(ew_elevations))

plt.figure(figsize=(12, 6))
plt.plot(ns_distance, ns_elevations, label='Kierunek Północ-Południe')
plt.plot(ew_distance, ew_elevations, label='Kierunek Wschód-Zachód')
plt.xlabel('Dystans [m]')
plt.ylabel('Wysokość [m]')
plt.title('Profil wysokościowy wzdłuż wybranych transektów')
plt.legend()
plt.grid()
plt.show()
