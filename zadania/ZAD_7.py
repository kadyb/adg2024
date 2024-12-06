#ZAD6
import os
os.chdir("C:/Users/kacpe/OneDrive/Pulpit/Studia/Geoinformacja/III rok/Semestr zimowy/Algorytmy/zaj_06_12")

vector_name = 'powiaty_kopia.gpkg'
powiaty = QgsVectorLayer(vector_name)
print(powiaty.isValid())

from qgis.core import QgsField
from qgis.PyQt.QtCore import QVariant 

powiaty.startEditing()

new_field = [QgsField("dlugosc_granicy", QVariant.Type.Double)]
powiaty.dataProvider().addAttributes(new_field)
powiaty.updateFields()

len_idx = powiaty.fields().indexOf("dlugosc_granicy") #pobranie indeksu

for feature in powiaty.getFeatures():
    length = feature.geometry().length()
    length = length / 1000
    powiaty.changeAttributeValue(feature.id(), len_idx, length)


powiaty.commitChanges()
from qgis.core import QgsProject
QgsProject.instance().addMapLayer(powiaty)
