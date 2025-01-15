import os 
import random
import numpy as np
from osgeo import gdal
import matplotlib.pyplot as plt
from qgis.core import QgsRasterLayer, QgsPointXY, QgsRectangle

os.chdir("C:/Users/kacpe/OneDrive/Pulpit/Studia/Geoinformacja/III rok/Semestr zimowy/Algorytmy/dane")

band3 = QgsRasterLayer("B3_zad12.tif")
band4 = QgsRasterLayer("B4_zad12.tif")

extent = band3.extent()
cell_size_x = band3.rasterUnitsPerPixelX()
cell_size_y = band4.rasterUnitsPerPixelY()

sample_size = 500
x_coords = []
y_coords = []

for i in range(sample_size):
    x = random.randint(int(extent.xMinimum()/cell_size_x), int(extent.xMaximum()/cell_size_x)) * cell_size_x
    y = random.randint(int(extent.yMinimum()/cell_size_y), int(extent.yMaximum()/cell_size_y)) * cell_size_y
    x_coords.append(x)
    y_coords.append(y)

#Tworzenie punktów
points = [QgsPointXY(x, y) for x, y in zip(x_coords, y_coords)]

#Sprawdzenie czy punkty zawieraja sie w zasiegu rastra
for point in points:
    if extent.contains(point):
        print("111111")
    else:
        print("000000")

#Pobieranie wartości pikseli dla próbek
values_band3 = []
values_band4 = []
for point in points:
    value3 = band3.dataProvider().sample(point, 1)[0]
    value4 = band4.dataProvider().sample(point, 1)[0]
    if not np.isnan(value3) and not np.isnan(value4):  # Obsługa brakujących wartości
        values_band3.append(value3)
        values_band4.append(value4)
        
#Obliczanie różnic i statystyk opisowych
differences = np.array(values_band3) - np.array(values_band4)
mean_diff = np.mean(differences)
std_diff = np.std(differences)
min_diff = np.min(differences)
max_diff = np.max(differences)

#Obliczanie współczynnika korelacji Pearsona
correlation_matrix = np.corrcoef(values_band3, values_band4)
pearson_correlation = correlation_matrix[0, 1]

#Tworzenie wykresu rozrzutu
plt.figure(figsize=(8, 6))
plt.scatter(values_band3, values_band4, alpha=0.4, color="blue", label="Próbki")
plt.plot([min(values_band3), max(values_band3)], [min(values_band3), max(values_band3)], color="red", label="Linia x = y")
plt.xlabel("Band 3")
plt.ylabel("Band 4")
plt.title("Wykres rozrzutu: Band 3 vs Band 4")
plt.legend()
plt.grid(True)
plt.show()

#Wyświetlanie wyników
print("Statystyki opisowe różnic (Band 3 - Band 4):")
print(f"Średnia różnica: {mean_diff:.2f}")
print(f"Odchylenie standardowe: {std_diff:.2f}")
print(f"Minimalna różnica: {min_diff:.2f}")
print(f"Maksymalna różnica: {max_diff:.2f}")
print(f"Współczynnik korelacji Pearsona: {pearson_correlation:.2f}")