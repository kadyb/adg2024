from qgis.core import *
from qgis.core import QgsProject
from qgis.core import QgsVectorLayer, QgsVectorFileWriter, QgsCoordinateTransformContext
from qgis.PyQt.QtCore import QVariant
import os

# Ustawienie ścieżki do pliku
path = os.path.join(os.path.expanduser("~"), "Documents")
os.chdir(path)

filename = "powiaty.gpkg"
wektor = QgsVectorLayer(filename, "powiaty", "ogr")
print("Warstwa poprawnie załadowana:", wektor.isValid())

if wektor.isValid():
    # 1. Start edycji
    wektor.startEditing()
    # 2. Dodanie nowego atrybutu, jeśli nie istnieje
    field_name = "dlugosc_granicy"
    if field_name not in [field.name() for field in wektor.fields()]:
        wektor.dataProvider().addAttributes([QgsField(field_name, QVariant.Double)])
        wektor.updateFields()
    # Pobranie indeksu nowego pola
    field_idx = wektor.fields().indexOf(field_name)
    # 3. Obliczanie długości granic i przypisanie wartości
    for feature in wektor.getFeatures():
        dlugosc = feature.geometry().length() / 1000  # Przeliczenie na kilometry
        wektor.changeAttributeValue(feature.id(), field_idx, dlugosc)
    # 4. Zapisanie zmian
    wektor.commitChanges()
    print("Dodano atrybut z długością granic.")
else:
    print("Nie udało się załadować warstwy.")

QgsProject.instance().addMapLayer(wektor)
