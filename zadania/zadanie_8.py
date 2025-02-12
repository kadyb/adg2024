import os
from qgis.core import QgsVectorLayer
import numpy as np

path = os.path.join(os.path.expanduser("~"),"Documents/adg/02")
os.chdir(path)

vector = QgsVectorLayer("powiaty.gpkg")

# 8 Napisz funkcję, która obliczy podstawowe statystyki opisowe i zastosuj ją 
# dla powierzchni oraz długości.

def stat_opisowe(warstwa, kolumna):
    wartosci = [feature[kolumna] for feature in warstwa.getFeatures()]
    min = round(np.min(wartosci),2)
    max = round(np.max(wartosci),2)
    mean = round(np.mean(wartosci),2)
    median = round(np.median(wartosci),2)
    std = round(np.std(wartosci),2)
    count = len(wartosci)
    return f"minimum: {min}, maksimum: {max}, średnia: {mean}, mediana: {median}, odchylenie standardowe: {std}, liczba wartości: {count}"

stat_opisowe(vector, "pole_km2")
stat_opisowe(vector, "dlugosc_granic_km")


