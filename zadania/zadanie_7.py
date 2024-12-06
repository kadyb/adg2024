
# Oblicz długość granic i dodaj jako nowy atrybut do warstwy.

from qgis.core import *
from qgis.core import QgsVectorLayer
from qgis.core import QgsProject
import os

filepath = os.path.join(os.path.expanduser("~"),"Documents", "algorytmy", "dane")
os.chdir(filepath)

filename = "powiaty.gpkg"
vector = QgsVectorLayer(filename, "powiaty", "ogr")

print(vector.isValid())

# krok 1 - wlaczenie edycji warstwy
vector.startEditing()

# krok 2 - stworzenie nowego trybutu
new_field = [QgsField("dlugosc", QVariant.Type.Double)]
vector.dataProvider().addAttributes(new_field)
vector.updateFields()

length_indeks = vector.fields().indexOf("dlugosc")
print(length_indeks)

for feature in vector.getFeatures():
    length = feature.geometry().length()
    length = length / 1000
    vector.changeAttributeValue(feature.id(), length_indeks, length)

vector.commitChanges()

QgsProject.instance().addMapLayer(vector)










