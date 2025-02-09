#ad 11

import numpy as np
import matplotlib.pyplot as plt

dem = QgsRasterLayer("DEM.tif", 'DEM')
extent = dem.extent()

ns = QgsGeometry.fromPolylineXY([
    QgsPointXY(extent.center().x(), extent.yMaximum()),
    QgsPointXY(extent.center().x(), extent.yMinimum())
])

ew = QgsGeometry.fromPolylineXY([
    QgsPointXY(extent.xMinimum(), extent.center().y()), 
    QgsPointXY(extent.xMaximum(), extent.center().y())
])

ns_feature = QgsFeature()
ns_feature.setGeometry(ns)
ew_feature = QgsFeature()
ew_feature.setGeometry(ew)

transects = QgsVectorLayer('LineString?crs=EPSG:2180', 'transekty', 'memory')

prov = transects.dataProvider()
prov.addFeatures([ns_feature, ew_feature])

QgsProject.instance().addMapLayer(transects)

def transampling(dem, transect, num_points = 100):
    values = []
    for i in range(num_points):
        point = transect.interpolate(transect.length() / num_points * i).asPoint()
        value = dem.dataProvider().identify(
            QgsPointXY(point),
            QgsRaster.IdentifyFormatValue
        ).results().get(1, None) 
        values.append(value)
    return values
    
def ifnan(values):
    values = np.array(values, dtype=float)
    nan_indices = np.isnan(values)
    if nan_indices.any():
        values[nan_indices] = np.interp(
        np.flatnonzero(nan_indices),
        np.flatnonzero(~nan_indices),
        values[~nan_indices]
        )
    return values
    
ns_val = transampling(dem, ns)
ew_val = transampling(dem, ew)
ns_val = ifnan(ns_val)
ew_val = ifnan(ew_val)

ns_dist = np.linspace(0, ns.length(), len(ns_val))
ew_dist = np.linspace(0, ew.length(), len(ew_val))

plt.figure(figsize=(12, 6))
plt.plot(ns_dist, ns_val, label='Północ-Południe')
plt.plot(ew_dist, ew_val, label='Wschód-Zachód')
plt.xlabel('Odległość [m]')
plt.ylabel('Wysokość [m]')
plt.title('Analiza geomorfometryczna wzdłuż transektów')
plt.legend()
plt.grid()
plt.show()