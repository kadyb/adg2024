# importy, organizacja plików
import qgis.core as qc
import os
import sys
from qgis.PyQt.QtCore import QVariant

vect = qc.QgsVectorLayer(os.path.join('dane','powiaty.gpkg'))
try:
    vect.isValid()
except rect.isValid != True:
    print('nieprawidłowy plik!')


# tworzenie warstwy i atrybutów
new_vect = qc.QgsVectorLayer('point','centroidy_powiaty','memory')
new_vect.setCrs(vect.crs())

attr_list = [qc.QgsField('nazwa',QVariant.String),qc.QgsField('x',QVariant.Double),
             qc.QgsField('y',QVariant.Double)]
new_vect.dataProvider().addAttributes(attr_list)
new_vect.updateFields()


# tworzenie obiektów/geometrii
features = vect.getFeatures()
for feature in features:
    geom = feature.geometry().centroid()
    for part in geom.constParts():
        for v in part.vertices():
            x = v.x()
            y = v.y()
    new_feat = qc.QgsFeature()
    new_geom = qc.QgsGeometry().fromPointXY(qc.QgsPointXY(x,y))
    new_feat.setGeometry(new_geom)
    new_feat.setAttributes([feature.attributes()[2],x,y])
    new_vect.dataProvider().addFeature(new_feat)
new_vect.updateExtents()

# zapis
options = qc.QgsVectorFileWriter.SaveVectorOptions()
options.driverName = 'gpkg'
options.fileEncoding = 'utf-8'
options.layerName = 'centroidy powiatów'
write = qc.QgsVectorFileWriter.writeAsVectorFormatV3(new_vect,"dane/centroidy.gpkg", 
                               qc.QgsCoordinateTransformContext(),options)
