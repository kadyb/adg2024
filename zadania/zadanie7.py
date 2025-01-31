#Oblicz długość granic i dodaj jako nowy atrybut do warstwy.

wektor = os.path.join(path, "powiaty.gpkg")
vector_layer = QgsVectorLayer(wektor, "powiaty.gpkg")
print(vector_layer.isValid())

from qgis.core import (
    QgsVectorLayer,
    QgsField,
    QgsProject,
    QgsFeature
)
from qgis.PyQt.QtCore import QVariant

############
vector_layer.startEditing()
############
fields = [QgsField("granica_dlugosc", QVariant.Double)]
provider = vector_layer.dataProvider()
provider.addAttributes(fields)
vector_layer.updateFields()

for feature in vector_layer.getFeatures():
    geom = feature.geometry()
    if geom:
        length = geom.length()
        feature["granica_dlugosc"] = length
        vector_layer.updateFeature(feature)

vector_layer.commitChanges()

QgsProject.instance().addMapLayer(vector_layer)


