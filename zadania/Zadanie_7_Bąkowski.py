from qgis.core import *
from qgis.core import QgsProject
from qgis.core import QgsVectorLayer, QgsVectorFileWriter, QgsCoordinateTransformContext
from itertools import islice
from qgis.core import QgsField
from qgis.PyQt.QtCore import QMetaType
from qgis.PyQt.QtCore import QVariant
from qgis.core import QgsRectangle
import os

path = os.path.join(os.path.expanduser("~"),"Documents")
print(path)
os.chdir(path)

filename = "powiaty.gpkg"
wektor = QgsVectorLayer(filename, "powiaty", "ogr")
print(wektor.isValid())

#1. Start edycji
wektor.startEditing()

#2. Utworznie kolummy i dodanie atrybutów
new_field = [QgsField("dlugosc_granicy", QVariant.Type.Double)]
wektor.dataProvider().addAttributes(new_field)
wektor.updateFields()

# indeks nowego atrybutu
area_idx = wektor.fields().indexOf("dlugosc_granicy")

for feature in wektor.getFeatures():
    dlugosc = feature.geometry().length()
    dlugosc = dlugosc / 1000
    wektor.changeAttributeValue(feature.id(), area_idx, dlugosc)

#3. Zapisanie zmian
wektor.commitChanges()

QgsProject.instance().addMapLayer(wektor)