
# zad 17
# Napisz funkcje xy_from_colrow() oraz colrow_from_xy(), które umożliwią transformację kolumn i wierszy 
# na współrzędne geograficzne oraz transformację w drugą stronę. Uwzględnij warunek sprawdzający 
# czy szukane parametry znajdują się w zakresie rastra, tj. nie wychodzą poza jego zasięg.


import math
import matplotlib.pyplot as plt
from qgis.core import QgsGeometry, QgsPointXY

# Transformacja kolumn i wierszy na współrzędne geograficzne oraz odwrotnie
def xy_from_colrow(column, row, x_min, y_max, x_res, y_res):
    x = x_min + (column + 0.5) * x_res
    y = y_max - (row + 0.5) * y_res
    return x, y

def colrow_from_xy(x, y, x_min, y_max, x_res, y_res, cols, rows):
    column = math.floor((x - x_min) / x_res)
    row = math.floor((y_max - y) / y_res)
    if 0 <= column < cols and 0 <= row < rows:
        return column, row
    else:
        raise ValueError("Współrzędne poza zakresem rastra!")


# Dane wejściowe
column = 5          # numer kolumny
row = 7             # numer wiersza
x_min = 0           # minimalna wartość x
y_max = 100         # maksymalna wartość y
x_res = 10          # rozdzielczość w osi x
y_res = 10          # rozdzielczość w osi y

# Wywołanie funkcji
xy_from_colrow(column, row, x_min, y_max, x_res, y_res)


# Dane wejściowe
x = 25             # Współrzędna x
y = 65             # Współrzędna y
cols = 10          # Liczba kolumn w rastrze
rows = 10          # Liczba wierszy w rastrze

# Wywołanie funkcji
colrow_from_xy(x, y, x_min, y_max, x_res, y_res, cols, rows)









