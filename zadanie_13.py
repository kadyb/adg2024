#Zaimplementuj funkcję losowania stratyfikowanego sample_strata(wektor, n),
#która zagwarantuje, że dla każdego poligonu zostanie zwrócona
#dokładna liczba punktów wskazana przez użytkownika.

import os
import random

input_vector_path = os.path.join(os.path.expanduser("~"), "Documents", "adp", "dane8", "powiaty.gpkg")
output_vector_path = os.path.join(os.path.expanduser("~"), "Documents", "adp", "dane8", "wynik.gpkg")

n = 5

vector_layer = QgsVectorLayer(input_vector_path, "input_layer", "ogr")

fields = QgsFields()
fields.append(QgsField("polygon_id", QVariant.Int))
crs = vector_layer.crs()
writer = QgsVectorFileWriter(
    output_vector_path, "UTF-8", fields, QgsWkbTypes.Point, crs, "GPKG"
)

for polygon_id, feature in enumerate(vector_layer.getFeatures(), start=1):
    geom = feature.geometry()

    bbox = geom.boundingBox()
    l_pkt = 0
    while l_pkt < n:
        x = random.uniform(bbox.xMinimum(), bbox.xMaximum())
        y = random.uniform(bbox.yMinimum(), bbox.yMaximum())
        punkt = QgsPointXY(x, y)

        if geom.contains(QgsGeometry.fromPointXY(punkt)):
            new_feature = QgsFeature(fields)
            new_feature.setGeometry(QgsGeometry.fromPointXY(punkt))
            new_feature.setAttributes([polygon_id])
            writer.addFeature(new_feature)
            l_pkt += 1

del writer

print(f"Ścieżka zapisu: {output_vector_path}")


