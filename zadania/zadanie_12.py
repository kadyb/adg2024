# Zadanie 12: Analiza teledetekcyjna

import random
import numpy as np
import rasterio
import matplotlib.pyplot as plt
from qgis.core import QgsPointXY

# Ustawienie ziarna dla generatora liczb losowych w celu uzyskania powtarzalnych wyników
random.seed(999)

# Generowanie losowych współrzędnych punktów w zakresie od 0 do 1000 z krokiem co 10
x_coordinates = random.choices(range(0, 1000, 10), k=100)
y_coordinates = random.choices(range(0, 1000, 10), k=100)

# Tworzenie listy obiektów punktowych (QgsPointXY)
punkty = [QgsPointXY(x, y) for x, y in zip(x_coordinates, y_coordinates)]

# Ścieżki do plików rastrowych (kanałów)
kanał1_ścieżka = "Landsat_B1.tif"
kanał2_ścieżka = "Landsat_B2.tif"

# Odczyt danych z plików rastrowych za pomocą biblioteki rasterio
with rasterio.open(kanał1_ścieżka) as źródło1, rasterio.open(kanał2_ścieżka) as źródło2:
    dane_kanał1 = źródło1.read(1)  # Odczyt pierwszego kanału
    dane_kanał2 = źródło2.read(1)  # Odczyt drugiego kanału

# Obliczenie różnic pomiędzy pikselami dwóch kanałów
różnice = dane_kanał1 - dane_kanał2

# Obliczenie współczynnika korelacji między dwoma kanałami
współczynnik_korelacji = np.corrcoef(dane_kanał1.flatten(), dane_kanał2.flatten())[0, 1]

# Wizualizacja danych: wykres rozrzutu z linią x = y
plt.figure(figsize=(8, 6))
plt.scatter(dane_kanał1.flatten(), dane_kanał2.flatten(), alpha=0.5, label="Punkty danych")
plt.plot(
    [0, max(dane_kanał1.max(), dane_kanał2.max())],
    [0, max(dane_kanał1.max(), dane_kanał2.max())],
    color='red', label='Linia x = y'
)
plt.xlabel("Wartości pikseli - Kanał 1")
plt.ylabel("Wartości pikseli - Kanał 2")
plt.legend()
plt.title(f"Współczynnik korelacji: {współczynnik_korelacji:.2f}")
plt.grid()
plt.show()

# Wyświetlenie statystyk różnic
print("Średnia różnic pikseli:", np.nanmean(różnice))
print("Odchylenie standardowe różnic pikseli:", np.nanstd(różnice))
