import qgis.core as qc
from PyQt5.QtCore import QVariant
import os

sciezka_danych = os.path.join('/Users/kuba/Desktop/STUDIA/3 ROK/1 SEMESTR/Algorytmy danych przestrzennych')
os.chdir(sciezka_danych)

warstwa = qc.QgsVectorLayer("powiaty.gpkg", "powiaty", "ogr")

warstwa_centroidy = qc.QgsVectorLayer("Point?crs=" + warstwa.crs().authid(), "centroidy_powiatow", "memory")
prov = warstwa_centroidy.dataProvider()

prov.addAttributes(warstwa_powiaty.fields())
warstwa_centroidy.updateFields()

warstwa_centroidy.startEditing()
for feature in warstwa_powiaty.getFeatures():
    centroid = feature.geometry().centroid()
    nowy_feature = qc.QgsFeature()
    nowy_feature.setGeometry(centroid)
    nowy_feature.setAttributes(feature.attributes())
    prov.addFeature(nowy_feature)

warstwa_centroidy.commitChanges()

output_path = os.path.join(sciezka_danych, "centroidy_powiatow.gpkg")
qc.QgsVectorFileWriter.writeAsVectorFormat(warstwa_centroidy, output_path, "UTF-8", warstwa_centroidy.crs(), "GPKG")

print(f"Zapisano warstwę centroidów do {output_path}.")
