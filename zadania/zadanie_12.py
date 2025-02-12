import os
import qgis.core as qg
import matplotlib.pyplot as plt
import random
import statistics
import numpy

path = os.path.join(os.path.expanduser("~"),"Documents/adg/04")
os.chdir(path)

b2 = QgsRasterLayer("LC09_L2SP_004026_20241210_20241211_02_T1_SR_B2.tif", "B2")
print(b2.isValid())
b4 = QgsRasterLayer("LC09_L2SP_004026_20241210_20241211_02_T1_SR_B4.tif", "B4")
print(b4.isValid())

# zad 12: Wygeneruj losową próbę i następnie dla dwóch wybranych kanałów spektralnych z 
# Landsat 8/9: wykonaj wykres rozrzutu uwzględniając przezroczystość punktów oraz zaznacz 
# linię x = y, oblicz statystyki opisowe z wartości różnic między tymi kanałami.
# Dodatkowo można obliczyć współczynnik korelacji Pearsona (numpy.corrcoef()).

# losowa próba
extent = b2.extent()
punkty = []

for i in range(100):
    x = random.uniform(extent.xMinimum(), extent.xMaximum())
    y = random.uniform(extent.yMinimum(), extent.yMaximum())
    pt = QgsPointXY(x, y)
    punkty.append(pt)
    
# pobranie wartosci
wartosci_b2 = []

for pt in punkty:
    wartosc = b2.dataProvider().sample(pt, 1)
    if wartosc[1] == True:
        wartosci_b2.append(wartosc[0])
    
wartosci_b4 = []

for pt in punkty:
    wartosc = b4.dataProvider().sample(pt, 1)
    if wartosc[1] == True:
        wartosci_b4.append(wartosc[0])

# wykres rozrzutu
plt.figure(figsize=(8, 6))
plt.scatter(wartosci_b2, wartosci_b4, alpha=0.5)
plt.xlabel('Wartości B2')
plt.ylabel('Wartości B4')
plt.legend()
plt.show()

# statystyki opisowe
roznice =[]
for i in range(len(wartosci_b2)):
    roznice.append(wartosci_b2[i] - wartosci_b4[i])

maximum = max(roznice)
minimum = min(roznice)
srednia = sum(roznice) / len(roznice)
mediana = statistics.median(roznice)
od_standardowe = statistics.stdev(roznice)
od_standardowe = round(od_standardowe, 2)
pearson = numpy.corrcoef(roznice)

print(f"Wartyość maksymalna: {maximum} "
      f"Wartość minimalna: {minimum} "
      f"Średnia: {srednia} "
      f"Mediana: {mediana} "
      f"Odchylenie standardowe: {od_standardowe} "
      f"Współczynnik korelacji Pearsona: {pearson}")
    