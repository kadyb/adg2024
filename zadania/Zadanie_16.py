import qgis.core as qc
import math as m
import os

sciezka_danych = os.path.join('/Users/kuba/Documents/GitHub/adg2024/dane')
os.chdir(sciezka_danych)

warstwa = qc.QgsVectorLayer("profil.csv", "profil", "ogr")

def surface_distance(warstwa):
    if not warstwa.isValid():
        raise ValueError("Warstwa nie jest poprawna!")

    lista_obiektow = list(warstwa.getFeatures())
    odleglosc_calkowita = 0.0

    for i in range(len(lista_obiektow) - 1):
        aktualny_punkt = lista_obiektow[i]
        nastepny_punkt = lista_obiektow[i + 1]

        x1, y1, z1 = float(aktualny_punkt[1]), float(aktualny_punkt[2]), float(aktualny_punkt[3])
        x2, y2, z2 = float(nastepny_punkt[1]), float(nastepny_punkt[2]), float(nastepny_punkt[3])

        odleglosc_calkowita += m.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

    return round(odleglosc_calkowita, 2)

odleglosc = surface_distance(warstwa)
print(f"Obliczona odległość powierzchniowa: {odleglosc} metrów")