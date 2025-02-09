import os
from qgis.core import QgsVectorLayer, QgsProject, QgsField
import statistics
from itertools import islice

# Funkcja do obliczenia podstawowych statystyk opisowych
def oblicz_statystyki(lista_wartosci):
    return {
        'liczba_elementow': len(lista_wartosci),
        'srednia': statistics.mean(lista_wartosci),
        'mediana': statistics.median(lista_wartosci),
        'odchylenie_standardowe': statistics.stdev(lista_wartosci) if len(lista_wartosci) > 1 else 0,
        'min': min(lista_wartosci),
        'max': max(lista_wartosci)
    }

# Wczytanie warstwy wektorowej
filepath = os.path.join(os.path.expanduser("~"),"Documents", "algorytmy", "powiaty.gpkg")
vector = QgsVectorLayer(filepath, "powiaty", "ogr")

if not vector.isValid():
    raise Exception("Nie można wczytać warstwy wektorowej.")

# Sprawdzenie metadanych
print(f"Typ geometrii: {vector.geometryType()}")
print(f"Liczba obiektów: {vector.featureCount()}")
print(f"Pola: {[field.name() for field in vector.fields()]}")

# Pobranie powierzchni i długości obiektów
powierzchnie = []
dlugosci = []

for feature in islice(vector.getFeatures(), 5):
    attrs = feature.attributes()
    geom = feature.geometry()
    print(attrs)
    # print(geom)
    powierzchnie.append(geom.area())
    dlugosci.append(geom.length())
    print(powierzchnie)
    print(dlugosci)

# Obliczenie i wyświetlenie statystyk opisowych
statystyki_powierzchni = oblicz_statystyki(powierzchnie)
statystyki_dlugosci = oblicz_statystyki(dlugosci)

print("Statystyki powierzchni:", statystyki_powierzchni)
print("Statystyki długości:", statystyki_dlugosci)
