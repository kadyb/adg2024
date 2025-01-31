import qgis.core as qc
import numpy as np
import os

sciezka_danych = os.path.join('/Users/kuba/Desktop/STUDIA/3 ROK/1 SEMESTR/Algorytmy danych przestrzennych')
os.chdir(sciezka_danych)

warstwa = qc.QgsVectorLayer("powiaty.gpkg", "powiaty", "ogr")

def oblicz_statystyki(warstwa):
    if not warstwa.isValid():
        raise ValueError("Niepoprawna warstwa!")

    powierzchnie = [feat.geometry().area() for feat in warstwa.getFeatures()]
    dlugosci = [feat.geometry().length() for feat in warstwa.getFeatures()]

    def statystyki(dane):
        return {met: round(func(dane), 4) for met, func in 
                [("min", np.min), ("max", np.max), ("mean", np.mean), 
                 ("median", np.median), ("std", np.std)]}

    return {"powierzchnia": statystyki(powierzchnie), "dlugosc": statystyki(dlugosci)}

# Obliczenie i wyświetlenie statystyk
wyniki = oblicz_statystyki(warstwa)
print("Statystyki powierzchni:", wyniki["powierzchnia"])
print("Statystyki długości:", wyniki["dlugosc"])