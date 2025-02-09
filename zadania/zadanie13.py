import os, random
from qgis.core import QgsVectorLayer, QgsPointXY, QgsFeature, QgsGeometry, QgsProject, QgsField, QgsVectorFileWriter
from qgis.PyQt.QtCore import QVariant

# Ścieżka do pliku
path = "C:/Users/krzys/Pulpit/algorytmy_danych/zaj4"
wektor = os.path.join(path, "powiaty.gpkg")

def sample_strata(wektor, n):
    vector_layer = QgsVectorLayer(wektor, "powiaty", "ogr")
    point_layer = QgsVectorLayer("Point?crs=" + vector_layer.crs().authid(), "sampled_points", "memory")
    provider = point_layer.dataProvider()

    provider.addAttributes([QgsField("powiat_id", QVariant.Int)])
    point_layer.updateFields()

    features = []

    for feature in vector_layer.getFeatures():
        geom = feature.geometry()
        powiat_id = feature.id()

        punkty_poligon = []
        while len(punkty_poligon) < n:
            bbox = geom.boundingBox()
            x, y = random.uniform(bbox.xMinimum(), bbox.xMaximum()), random.uniform(bbox.yMinimum(), bbox.yMaximum())
            pt = QgsPointXY(x, y)

            if geom.contains(QgsGeometry.fromPointXY(pt)):
                punkty_poligon.append(pt)

        for punkt in punkty_poligon:
            feat = QgsFeature()
            feat.setGeometry(QgsGeometry.fromPointXY(punkt))
            feat.setAttributes([powiat_id])
            features.append(feat)

    provider.addFeatures(features)
    point_layer.updateExtents()

    QgsProject.instance().addMapLayer(point_layer)

    QgsVectorFileWriter.writeAsVectorFormat(point_layer, "C:\\Users\\krzys\\Pulpit\\algorytmy_danych\\zaj4\\sampled_points.gpkg", "utf-8", vector_layer.crs(), "GPKG")

sample_strata(wektor, 5)
