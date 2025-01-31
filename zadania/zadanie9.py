import os
from qgis.core import QgsVectorLayer, QgsPointXY, QgsFeature, QgsGeometry, QgsField, QgsVectorFileWriter
from qgis.PyQt.QtCore import QVariant

# Ścieżka do pliku
path = "C:/Users/krzys/Pulpit/algorytmy_danych/zaj4"
wektor = os.path.join(path, "powiaty.gpkg")

# Wczytanie warstwy powiatów
vector_layer = QgsVectorLayer(wektor, "powiaty", "ogr")

# Utworzenie nowej warstwy z centroidami
centroid_layer = QgsVectorLayer("Point?crs=" + vector_layer.crs().authid(), "centroidy", "memory")
provider = centroid_layer.dataProvider()

# Dodanie pola ID do warstwy centroidów
provider.addAttributes([QgsField("id", QVariant.Int)])
centroid_layer.updateFields()

# Tworzenie centroidów i dodanie ich do nowej warstwy
features = []
for feature in vector_layer.getFeatures():
    geom = feature.geometry()
    centroid = geom.centroid().asPoint()
    feat = QgsFeature()
    feat.setGeometry(QgsGeometry.fromPointXY(centroid))
    feat.setAttributes([feature.id()])
    features.append(feat)

# Dodanie cech (centroidów) do warstwy
provider.addFeatures(features)
centroid_layer.updateExtents()

# Zapisanie warstwy do pliku .gpkg
QgsVectorFileWriter.writeAsVectorFormat(centroid_layer, 
                                        "C:\\Users\\krzys\\Pulpit\\algorytmy_danych\\zaj4\\centroidy.gpkg", 
                                        "utf-8", 
                                        vector_layer.crs(), 
                                        "GPKG")

# Dodanie warstwy centroidów do projektu
QgsProject.instance().addMapLayer(centroid_layer)
