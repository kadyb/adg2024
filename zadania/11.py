import os
from qgis.core import (
QgsRasterLayer,
QgsLineString,
QgsPointXY,
QgsGeometry,
QgsVectorLayer,
QgsFields,
QgsField)
import matplotlib.pyplot as plt

#otwarcie i utworzenie warstw
dem = r"C:\Users\jmpos\Desktop\adp\DEM.tif"
dem = QgsRasterLayer(dem,"DEM")

points_WE = QgsVectorLayer("Point", "punkty", "memory")
points_NS = QgsVectorLayer("Point", "punkty", "memory")
points = [points_WE, points_NS]

#dodanie atrybutów to warstw z punktami
for layer in points:
    layer.startEditing()
    layer.addAttribute(QgsField("id", QVariant.Int))
    layer.addAttribute(QgsField("X", QVariant.Double))
    layer.addAttribute(QgsField("Y", QVariant.Double))
    layer.commitChanges()
    layer.setCrs(dem.crs())

# oś WE
jump_x = dem.rasterUnitsPerPixelX()
position_x = dem.extent().xMinimum()
position_y = (dem.extent().yMinimum() + dem.extent().yMaximum()) /2
features = []
for i in range(dem.width() - 1):
    feature = QgsFeature()
    feature.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(position_x, position_y)))
    feature.setAttributes([i + 1,position_x, position_y])
    position_x += jump_x 
    features.append(feature)

points_WE.dataProvider().addFeatures(features)

# oś NS
jump_y = dem.rasterUnitsPerPixelY()
position_x = (dem.extent().xMinimum() + dem.extent().xMaximum()) /2
position_y = dem.extent().yMinimum()
features = []
for i in range(dem.height() - 1):
    feature = QgsFeature()
    feature.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(position_x, position_y)))
    feature.setAttributes([i + 1,position_x, position_y])
    position_y += jump_y 
    features.append(feature)

points_NS.dataProvider().addFeatures(features)

#przypisanie wartości z rastra do punktów
params = {
    'INPUT': points_WE,
    'RASTERCOPY': dem,
    'OUTPUT': 'memory:'
}
output_WE = processing.run("native:rastersampling", params)
params['INPUT'] = points_NS
output_NS = processing.run("native:rastersampling", params)

#funkcja utworzenia wykresu
def plot_from_layer(layer, axis):
    feature_count = layer['OUTPUT'].featureCount()
    x_values = []
    y_values = []
    
    for i in range(1, feature_count):
        feature = layer['OUTPUT'].getFeature(i)
        x_values.append(feature[axis])
        y_values.append(feature['SAMPLE_1'])
    
    plt.plot(x_values, y_values)
    plt.xlabel(axis)
    plt.ylabel('Z')
    plt.title('Profile')
    plt.show()

plot_from_layer(output_NS, 'Y')
plot_from_layer(output_WE, 'X')

# jestem świadom iż segment z utworzeniem punktów napisać jako funkcję ale nie mam siły :D
