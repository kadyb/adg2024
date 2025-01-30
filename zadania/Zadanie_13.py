import random
from qgis.core import QgsPointXY, QgsFeature, QgsGeometry, QgsField, QgsVectorLayer, QgsVectorFileWriter
from PyQt5.QtCore import QVariant
import os


os.chdir('/Users/kuba/Desktop/STUDIA/3 ROK/1 SEMESTR/Algorytmy danych przestrzennych/')


vector = QgsVectorLayer('powiaty.gpkg')

def sample_strata(wektor, n):
    punkty = []
    
    
    point_layer = QgsVectorLayer("Point?crs=EPSG:2180", "Warstwa_punkty", "memory")
    pr = point_layer.dataProvider()
    
    
    pr.addAttributes([QgsField("id", QVariant.Int)])
    point_layer.updateFields()
    
    features = []

    
    for feature in wektor.getFeatures():
        geom = feature.geometry()
        liczba_punktow = n
        
        punkty_poligon = []
        
       
        while len(punkty_poligon) < liczba_punktow:
            bbox = geom.boundingBox()
            
            
            x = random.uniform(bbox.xMinimum(), bbox.xMaximum())
            y = random.uniform(bbox.yMinimum(), bbox.yMaximum())
            pt = QgsPointXY(x, y)
            
            
            if geom.contains(QgsGeometry.fromPointXY(pt)):
                punkty_poligon.append(pt)
        
        punkty.append(punkty_poligon)
        
        
        for idx, punkt in enumerate(punkty_poligon):
            feat = QgsFeature()
            feat.setGeometry(QgsGeometry.fromPointXY(punkt))
            feat.setAttributes([idx])
            features.append(feat)
    
    
    pr.addFeatures(features)


    QgsVectorFileWriter.writeAsVectorFormat(point_layer, "/Users/kuba/Desktop/STUDIA/3 ROK/1 SEMESTR/Algorytmy danych przestrzennych/sampled_points.gpkg", "UTF-8", point_layer.crs(), "GPKG")
    
    return point_layer


sample_strata(vector, 5)
