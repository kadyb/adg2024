# ---| zad 12 - analiza teledetekcyjna |--- #
# biblioteki
import os
import qgis.core as qc
import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication
import random
app = QApplication(sys.argv)

# tworzenie próbki
def GetSample(raster):
    random.seed(34516) # jako przykładowy
    samples = np.array([])
    for i in range(100):
        cols = raster.extent().xMinimum() + raster.width() * raster.rasterUnitsPerPixelX() * random.random()
        rows = raster.extent().yMinimum() + raster.height() * raster.rasterUnitsPerPixelY() * random.random()
        sample = raster.dataProvider().sample(qc.QgsPointXY(cols,rows),1)
        samples = np.append(samples, [sample[0]])
        
    return samples

# przygotowanie danych
def PrepData(path1,path2):
    r1 = qc.QgsRasterLayer(path1) # pyqgis nie lubi się z ścieżkami względnymi
    r2 = qc.QgsRasterLayer(path2)
    if r1.isValid() == False:
        print('nieprawidłowy plik!')
    if r2.isValid() == False:
        print('nieprawidłowy plik!')
           
    a = GetSample(r1)
    b = GetSample(r2)
    return a,b

# oblicz statystyki opisowe z wartości różnic między tymi kanałami.
def GetStats(a,b):
    diff = a - b
    return pd.DataFrame(diff,columns=['stats']).describe()

# wykonaj wykres rozrzutu uwzględniając przezroczystość punktów oraz zaznacz linię x = y,
def ImgCorr(a,b):
    r_pow_2 = round(np.corrcoef(a, b)[0, 1]**2, 3)
    # lokalizacja tekstu z współczynnikiem Pearsona
    if b.max() > 0:
        ypos = b.max() * 0.9
    elif b.max() == 0:
        ypos = b.min() + 0.1
    else:
        ypos = b.max() * 1.1

    # dopasowywanie danych metodą najmniejszych kwadratów, użyte to zostanie do stworzenia kwadratu
    m, p = np.polyfit(a, b, 1) 

    #  tworzenie wykresu
    fig, ax = plt.subplots()
    ax.plot(a, m*a + p, color="k", lw=1.5)
    ax.scatter(a,b, s = 10, alpha = 0.6)
    ax.text(a.min(),ypos,s='r^2= {}'.format(r_pow_2), color = '#ff0000')
    plt.show()


# przykładowe  ścieżki
B2 = os.path.join(path,'block_B2.tif') 
B3 = os.path.join(path,'block_B3.tif')

prepd = PrepData(B2,B3)
comp = ImgCorr(*prepd)
stats = GetStats(*prepd)
