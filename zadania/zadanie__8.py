#Napisz funkcję, która obliczy podstawowe statystyki opisowe 
#i zastosuj ją dla powierzchni oraz długości.

import statistics
import numpy as np

vectorname = "powiaty.gpkg"
vector=QgsVectorLayer(vectorname)

def statystyki_opisowe(vector):
    pow = []
    dl = []
    
    for feature in vector.getFeatures():
        geometry = feature.geometry()
        pow.append(geometry.area())
        dl.append(geometry.length())

    statystyki_powierzchnia = {
        'minimum': min(pow),
        'maksimum': max(pow),
        'srednia': statistics.mean(pow),
        'mediana': statistics.median(pow),
        'odchylenie standardowe': statistics.stdev(pow),
        'kwantyl dolny': np.quantile(pow, 0.25),
        'kwantyl gorny': np.quantile(pow, 0.75),
        'suma': sum(pow)
    }

    statystyki_dlugosc = {
        'minimum': min(dl),
        'maksimum': max(dl),
        'srednia': statistics.mean(dl),
        'mediana': statistics.median(dl),
        'odchylenie standardowe': statistics.stdev(dl),
        'kwantyl dolny': np.quantile(dl, 0.25),
        'kwantyl gorny': np.quantile(dl, 0.75),
        'suma': sum(dl)
    }

    return print(f'Statysyki dla powierzchni{statystyki_powierzchnia}, \n\nStatysyki dla dlugosci{statystyki_dlugosc}')

statystyki_opisowe(vector)








