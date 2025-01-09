import os
from qgis import core
import random

path = os.path.join(os.path.expanduser("~"), "Documents", "dane")
os.chdir(path)

file = "powiaty.gpkg"
powiaty = QgsVectorLayer(file, "powiaty", "ogr")

def sample_strata(wektor, n):
    n = int(n)
    geometry_type = "Point"
    crs = wektor.crs().toWkt()
    output = QgsVectorLayer(geometry_type+"?crs="+crs, "sample_strata", "memory")
    output_provider = output.dataProvider()
    if n >= 1:
        if wektor.isValid():
            if wektor.geometryType() == QgsWkbTypes.PolygonGeometry:
                for feature in wektor.getFeatures():
                    count = 1
                    while count <= n:
                        bbox = feature.geometry().boundingBox()
                        x = random.uniform(bbox.xMinimum(), bbox.xMaximum())
                        y = random.uniform(bbox.yMinimum(), bbox.yMaximum())
                        pt = QgsPointXY(x, y)
                        if feature.geometry().contains(QgsGeometry.fromPointXY(pt)):
                            f_output = QgsFeature()
                            f_output.setGeometry(QgsGeometry.fromPointXY(pt))
                            output_provider.addFeature(f_output)
                            count += 1
                QgsProject.instance().addMapLayer(output)
            else:
                print("Warstwa wektorowa powinna być poligonem")
        else:
            print("Warstwa wektorowa nie została załadowana poprawnie")
    else:
        print("Co najmniej jeden punkt musi zostać wygenerowany")
    
sample_strata(powiaty, 3)

