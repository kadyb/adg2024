import qgis.core as qc
from PyQt5.QtCore import QVariant
import os

sciezka_danych = os.path.join('/Users/kuba/Desktop/STUDIA/3 ROK/1 SEMESTR/Algorytmy danych przestrzennych')
os.chdir(sciezka_danych)

warstwa = qc.QgsVectorLayer("powiaty.gpkg", "powiaty", "ogr")

def dlugosc_granicy(warstwa, pole="dlugosc_granicy"):
    warstwa.startEditing()
    warstwa.dataProvider().addAttributes([qc.QgsField(pole, QVariant.Double)])
    warstwa.updateFields()

    id_pola = warstwa.fields().indexFromName(pole)
    zmiany = {feat.id(): feat.geometry().length() for feat in warstwa.getFeatures()}

    warstwa.dataProvider().changeAttributeValues({k: {id_pola: v} for k, v in zmiany.items()})
    warstwa.commitChanges()
    print(f"Atrybut '{pole}' został dodany i wypełniony.")



dlugosc_granicy(warstwa_powiaty)
