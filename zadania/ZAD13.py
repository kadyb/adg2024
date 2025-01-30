import os 
import random
from qgis.core import (
    QgsVectorLayer,
    QgsFeature,
    QgsPointXY,
    QgsGeometry,
    QgsField,
    QgsFields,
    QgsVectorDataProvider,
    QgsProject
)
from qgis.PyQt.QtCore import QVariant

os.chdir("C:/Users/kacpe/OneDrive/Pulpit/Studia/Geoinformacja/III rok/Semestr zimowy/Algorytmy/dane")
wektor = QgsVectorLayer("powiaty.gpkg")

def sample_strata(warstwa, n):
    warstwa_punkty = QgsVectorLayer("Point?crs=" + warstwa.crs().authid(), "Punkty_Stratyfikowane", "memory")
    provider = warstwa_punkty.dataProvider()
    provider.addAttributes([
        QgsField("id_powiat", QVariant.Int),
        QgsField("x", QVariant.Double),
        QgsField("y", QVariant.Double)
    ])
    warstwa_punkty.updateFields()
    features = []
    for feature in warstwa.getFeatures():
        geom = feature.geometry()
        bbox = geom.boundingBox()
        id_powiat = feature.id()
        for _ in range(n):
            while True:
                x = random.uniform(bbox.xMinimum(), bbox.xMaximum())
                y = random.uniform(bbox.yMinimum(), bbox.yMaximum())
                punkt = QgsPointXY(x, y)
                if geom.contains(QgsGeometry.fromPointXY(punkt)):
                    f = QgsFeature()
                    f.setGeometry(QgsGeometry.fromPointXY(punkt))
                    f.setAttributes([id_powiat, x, y])
                    features.append(f)
                    break 
    provider.addFeatures(features)
    warstwa_punkty.updateExtents()
    QgsProject.instance().addMapLayer(warstwa)
    QgsProject.instance().addMapLayer(warstwa_punkty)


sample_strata(wektor, 5)