from qgis.core import QgsVectorLayer

def oblicz_statystyki(lista):
    return {
        "suma": sum(lista),
        "srednia": sum(lista) / len(lista),
        "min": min(lista),
        "max": max(lista)
    }

# Ścieżka do warstwy
wektor = "C:\\Users\\krzys\\Pulpit\\algorytmy_danych\\zaj4\\powiaty.gpkg"
vector_layer = QgsVectorLayer(wektor, "powiaty", "ogr")

# Pobranie wartości powierzchni i długości
powierzchnie = [feat.geometry().area() for feat in vector_layer.getFeatures()]
dlugosci = [feat.geometry().length() for feat in vector_layer.getFeatures()]

# Obliczenie statystyk
stat_powierzchnia = oblicz_statystyki(powierzchnie)
stat_dlugosc = oblicz_statystyki(dlugosci)

print("Statystyki powierzchni:", stat_powierzchnia)
print("Statystyki długości:", stat_dlugosc)