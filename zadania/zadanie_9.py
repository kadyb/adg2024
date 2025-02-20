import os
from qgis.core import (
    QgsApplication,
    QgsVectorLayer,
    QgsFeature,
    QgsGeometry,
    QgsField,
    QgsVectorFileWriter
)
from qgis.PyQt.QtCore import QVariant


# Wczytanie warstwy wektorowej
filepath = os.path.join(os.path.expanduser("~"),"Documents", "algorytmy", "powiaty.gpkg")
vector = QgsVectorLayer(filepath, "powiaty", "ogr")

if not vector.isValid():
    raise Exception("Nie można wczytać warstwy wektorowej.")

# Tworzenie nowej warstwy wektorowej dla centroidów
centroid_layer = QgsVectorLayer("Point?crs=EPSG:4326", "centroidy", "memory")
prov = centroid_layer.dataProvider()
prov.addAttributes([QgsField("ID", QVariant.Int)])
centroid_layer.updateFields()

# Obliczanie centroidów i dodawanie ich do nowej warstwy
features = vector.getFeatures()

for feature in features:
    geom = feature.geometry()
    centroid = geom.centroid()
    
    new_feature = QgsFeature()
    new_feature.setGeometry(centroid)
    new_feature.setAttributes([feature.id()])
    prov.addFeatures([new_feature])

# Aktualizacja warstwy
centroid_layer.updateExtents()

# Zapisanie nowej warstwy na dysku
output_filepath = os.path.join(os.path.expanduser("~"),"Documents", "algorytmy", "centroidy.gpkg")
QgsVectorFileWriter.writeAsVectorFormat(
    centroid_layer,
    output_filepath,
    "UTF-8",
    centroid_layer.crs(),
    "GPKG"
)


