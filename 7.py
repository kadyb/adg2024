
import os
os.chdir("C:\\Users\\user\\Downloads\\algorytmy_przetwarzania_kadyb")
filepath = os.path.join("powiaty.gpkg")
vector = QgsVectorLayer(filepath,"powiaty","ogr")

print(vector.isValid())

from qgis.core import (
    QgsVectorLayer,
    QgsField,
    QgsProject,
    QgsFeature
)

from qgis.core import QgsField
from qgis.PyQt.QtCore import QMetaType

vector.startEditing()

# (2) dodanie nowego atrybutu do tabeli
new_field = [QgsField("pole_dlugosci2", QVariant.Double)]
vector.dataProvider().addAttributes(new_field)
vector.updateFields()

# indeks nowego atrybutu
length_idx = vector.fields().indexOf("pole_dlugosci2")

# (3) obliczenie powierzchni dla każdego obiektu
for feature in vector.getFeatures():
    length = feature.geometry().length()
    # wprowadzenie wartości do atrybutu obiektu
    vector.changeAttributeValue(feature.id(), length_idx, length)

# (4) zapisanie zmian
vector.commitChanges()