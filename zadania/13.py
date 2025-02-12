import os
from qgis.core import QgsVectorLayer
from qgis.core import QgsProject
import random

path = r"C:\Users\jmpos\Desktop\adp"
powiaty = QgsVectorLayer(os.path.join(path, 'powiaty.gpkg'),"powiaty")


def sample_strata(wektor, n):
    
    random_points = []
    for feature in wektor.getFeatures():
        bbox = feature.geometry().boundingBox()
        points = []
        while len(points) < n:
            x = random.uniform(bbox.xMinimum(), bbox.xMaximum())
            y = random.uniform(bbox.yMinimum(), bbox.yMaximum())
            pt = QgsPointXY(x, y)
            if feature.geometry().contains(pt):
                points.append(pt)
        random_points.extend(points)
    
    features = []
    for i, point in enumerate(random_points):
        feature = QgsFeature()
        feature.setGeometry(QgsGeometry.fromPointXY(point))
        features.append(feature)
    
    layer = QgsVectorLayer("Point?crs=EPSG:2180", "Punkty stratyfikowane", "memory")
    provider = layer.dataProvider()
    provider.addFeatures(features)
    layer.updateExtents()
    QgsProject.instance().addMapLayer(layer)
    
    return


sample_strata(powiaty,2)




