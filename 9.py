from qgis.core import *
import os

sciezka_katalogu = r"C:\Users\mixer\Downloads\adg"
os.chdir(sciezka_katalogu)

plik_wektorowy = "powiaty.gpkg"
warstwa = QgsVectorLayer(plik_wektorowy, "Powiaty", "ogr")

print(vector.isValid())

QgsProject.instance().addMapLayer(warstwa)


typ_geom = "Point"
CRS = "EPSG:2180"
centroidy_layer = QgsVectorLayer(f"{typ_geom}?crs={CRS}", "Centroidy", "memory")
centr_provider = warstwa_centroidy.dataProvider()

centroidy_layer.startEditing()
for obiekt in warstwa.getFeatures():
    centroid = QgsFeature()
    centroid.setGeometry(obiekt.geometry().centroid())
    centr_provider.addFeature(centroid)

warstwa_centroidy.updateExtents()
warstwa_centroidy.commitChanges()

opcje_zapisu = QgsVectorFileWriter.SaveVectorOptions()
opcje_zapisu.driverName = "GPKG"
opcje_zapisu.fileEncoding = "UTF-8"
opcje_zapisu.layerName = "centroidy"

QgsVectorFileWriter.writeAsVectorFormatV3(
    warstwa_centroidy, "powiaty_centroidy3.gpkg", QgsCoordinateTransformContext(), opcje_zapisu
)
