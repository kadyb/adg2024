# Zadanie 13 
# Funkcja losowania stratyfikowanego

from qgis.core import (
    QgsVectorLayer, 
    QgsVectorFileWriter, 
    QgsFeature, 
    QgsGeometry, 
    QgsPointXY, 
    QgsProject,
    QgsField
)
from qgis.PyQt.QtCore import QVariant
import random

def sample_strata_qgis(vector_path, output_path, n):
    # Wczytaj warstwę wektorową
    layer = QgsVectorLayer(vector_path, "input_layer", "ogr")
    if not layer.isValid():
        print("Nie udało się wczytać warstwy.")
        return

    # Tworzenie nowej warstwy punktowej
    fields = layer.fields()
    fields.append(QgsField("id", QVariant.Int))  # Dodaj pole ID

    point_layer = QgsVectorLayer("Point?crs=" + layer.crs().authid(), "sampled_points", "memory")
    point_layer_data = point_layer.dataProvider()
    point_layer_data.addAttributes(fields)
    point_layer.updateFields()

    # Przechodzenie przez poligony i losowanie punktów
    features = layer.getFeatures()
    new_features = []
    feature_id = 0

    for feature in features:
        polygon = feature.geometry()

        if not polygon.isEmpty():
            bbox = polygon.boundingBox()

            for _ in range(n):
                while True:
                    x = random.uniform(bbox.xMinimum(), bbox.xMaximum())
                    y = random.uniform(bbox.yMinimum(), bbox.yMaximum())
                    point = QgsPointXY(x, y)
                    point_geom = QgsGeometry.fromPointXY(point)

                    if polygon.contains(point_geom):
                        new_feature = QgsFeature()
                        new_feature.setGeometry(point_geom)
                        new_feature.setAttributes(feature.attributes() + [feature_id])
                        new_features.append(new_feature)
                        feature_id += 1
                        break

    # Dodanie nowych punktów do warstwy
    point_layer_data.addFeatures(new_features)
    point_layer.updateExtents()

    # Zapis wyników do pliku GeoPackage
    QgsVectorFileWriter.writeAsVectorFormat(point_layer, output_path, "utf-8", point_layer.crs(), "GPKG")

    print("Zapisano wynik do:", output_path)

# Ścieżki plików
input_vector = "C:/Users/weron/Documents/algorytmy/powiaty.gpkg"
output_vector = "C:/Users/weron/Documents/algorytmy/wynik_stratyfikowane.gpkg"

# Uruchomienie funkcji
sample_strata_qgis(input_vector, output_vector, 5)

