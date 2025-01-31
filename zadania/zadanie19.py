import random
from qgis.core import *
from qgis.PyQt.QtCore import QVariant

#Losowanie punktow w poligonie

layer_path = "C:/Users/krzys/Pulpit/algorytmy_danych/zaj4/powiaty.gpkg"
vector_layer = QgsVectorLayer(layer_path, "powiaty", "ogr")

point_layer = QgsVectorLayer("Point?crs=" + vector_layer.crs().authid(), "sampled_points", "memory")
provider = point_layer.dataProvider()

provider.addAttributes([QgsField("id", QVariant.Int), QgsField("powiat_id", QVariant.Int)])
point_layer.updateFields()

features = []
global_idx = 0

for feature in vector_layer.getFeatures():
    geom = feature.geometry()
    powiat_id = feature.id()
    
    for _ in range(5):
        bbox = geom.boundingBox()
        x = random.uniform(bbox.xMinimum(), bbox.xMaximum())
        y = random.uniform(bbox.yMinimum(), bbox.yMaximum())
        pt = QgsPointXY(x, y)
        
        if geom.contains(QgsGeometry.fromPointXY(pt)):
            feat = QgsFeature()
            feat.setGeometry(QgsGeometry.fromPointXY(pt))
            feat.setAttributes([global_idx, powiat_id])
            features.append(feat)
            global_idx += 1

provider.addFeatures(features)
point_layer.updateExtents()

QgsProject.instance().addMapLayer(point_layer)
