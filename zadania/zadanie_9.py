import os
from qgis.core import QgsVectorLayer, QgsFeature, QgsProject, QgsVectorFileWriter, QgsCoordinateTransformContext

path = os.path.join(os.path.expanduser("~"),"Documents/adg/02")
os.chdir(path)

vector = QgsVectorLayer("powiaty.gpkg")

# 9 Stwórz nową warstwę z obliczonymi centroidami dla powiatów i zapisz ją na 
# dysku w formacie .gpkg

# typ geometrii i układ współrzędnych
geometry_type = "Point"
crs = "EPSG:2180"

# stworzenie nowej warstwy punktowej
newlayer = QgsVectorLayer(geometry_type+"?crs="+crs, "centroidy", "memory")
print(newlayer.isValid())

# rozpoczęcie edycji
newlayer.startEditing()

# dodanie dodanie centroidów
for feature in vector.getFeatures():
    centroid = feature.geometry().centroid()
    feature = QgsFeature()
    feature.setGeometry(centroid)
    newlayer.addFeature(feature)

# aktualizacja zasięgu warstwy
newlayer.updateExtents()
# zapisanie zmian
newlayer.commitChanges()

QgsProject.instance().addMapLayer(newlayer)

# zapis do geopaczki
output_path = "C:/Users/Komputer/Documents/adg/02/centoidy.gpkg"

options = QgsVectorFileWriter.SaveVectorOptions()
options.driverName = "GPKG"
options.fileEncoding = "UTF-8"

writer = QgsVectorFileWriter.writeAsVectorFormatV3(
    layer = newlayer,
    fileName = output_path,
    transformContext = QgsCoordinateTransformContext(),
    options = options)


    