import os
import random
from qgis.core import QgsPointXY
from qgis.core import QgsGeometry

path = os.path.join(os.path.expanduser("~"),"Documents/adg/04")
os.chdir(path)

# Zadanie 13: Zaimplementuj funkcję losowania stratyfikowanego sample_strata(wektor, n), która zagwarantuje, że dla każdego poligonu zostanie zwrócona dokładna liczba punktów wskazana przez użytkownika, a wynik zostanie zapisany jako warstwa wektorowa. Do analizy wykorzystaj dane z pliku powiaty.gpkg

powiaty = QgsVectorLayer("powiaty.gpkg", "powiaty")
print(powiaty.isValid())

def sample_strata(wektor, n):
    # typ geometrii i układ współrzędnych
    geometry_type = "Point"
    crs = wektor.crs().authid()
    # stworzenie nowej warstwy wektorowej
    newlayer = QgsVectorLayer(geometry_type+"?crs="+crs, "losowe_punkty", "memory")
    print(newlayer.isValid())
    newlayer.startEditing()
    # losowanie punktów
    for feat in wektor.getFeatures():
        polygon = feat.geometry()
        bbox = polygon.boundingBox()
        punkty = 0
        while punkty < n:
            x = random.uniform(bbox.xMinimum(), bbox.xMaximum())
            y = random.uniform(bbox.yMinimum(), bbox.yMaximum())
            pt = QgsPointXY(x, y)
            if polygon.contains(pt):
                pnt = QgsGeometry.fromPointXY(pt)
                feature = QgsFeature()
                feature.setGeometry(pnt)
                newlayer.addFeature(feature)
                punkty += 1
            else:
                pass
    newlayer.updateExtents()
    # zapisanie zmian
    newlayer.commitChanges()
    _writer = QgsVectorFileWriter.writeAsVectorFormat(newlayer,sciezka_zapisu,'utf-8',driverName='ESRI Shapefile')

sample_strata(powiaty, 50, "C:/Users/Komputer/Documents/adg/04/punkty.shp")
