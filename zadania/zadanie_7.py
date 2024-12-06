import os
from qgis.core import QgsVectorLayer
from qgis.core import QgsField
from qgis.PyQt.QtCore import QVariant

path = os.path.join(os.path.expanduser("~"),"Documents/adg/02")
os.chdir(path)

vector = QgsVectorLayer("powiaty.gpkg")

# 7 Oblicz długość granic i dodaj jako nowy atrybut do warstwy.
# rozpoczęcie trybu edycji warstwy
vector.startEditing()

# dodanie nowego atrybutu do tabeli
new_field = [QgsField("dlugosc_granic_km", QVariant.Double)]
vector.dataProvider().addAttributes(new_field)
vector.updateFields()

# indeks nowego atrybutu
length_idx = vector.fields().indexOf("dlugosc_granic_km")

# obliczenie powierzchni dla każdego obiektu
for feature in vector.getFeatures():
    length = feature.geometry().length()/1000
    # wprowadzenie wartości do atrybutu obiektu
    vector.changeAttributeValue(feature.id(), length_idx, length)

# zapisanie zmian
vector.commitChanges()
