import os
import matplotlib.pyplot as plt

path = os.path.join(os.path.expanduser("~"),"Documents/adg/04")
os.chdir(path)

DEM = QgsRasterLayer("DEM.tif", "DEM")

# Dokonaj analizy ukształtowania terenu (plik DEM.tif) używając dwóch transektów 
# północ-południe oraz wschód-zachód. Wynik zaprezentuj na rycinie (na osi X powinna 
# znajdować się odległość wyrażona w metrach). Zastanów się również, co zrobić w przypadku, 
# gdy komórki nie posiadają wartości (nan).

# tworzenie linii
pt1 = QgsPointXY(275874, 382244)
pt2 = QgsPointXY(275874, 641400)
pt3 = QgsPointXY(499443, 641400)
lineNS = QgsGeometry(QgsLineString([pt1, pt2]))
lineWE = QgsGeometry(QgsLineString([pt2, pt3]))

NS_length = lineNS.length()
WE_length = lineWE.length()

# generowanie regularnych punktów
interval = 2600

distance = 0
pointsNS = []
while distance <= NS_length:
    point = lineNS.interpolate(distance)
    pointsNS.append(point.asPoint())
    distance = distance + interval

distance = 0
pointsWE = []
while distance <= WE_length:
    point = lineWE.interpolate(distance)
    pointsWE.append(point.asPoint())
    distance = distance + interval

# pobranie wartości z rastra
valueNS = []
for pt in pointsNS:
    value = DEM.dataProvider().sample(pt, 1)
    if value[1] == True:
        valueNS.append(value[0])
    else:
        valueNS.append(0)
    
valueWE = []
for pt in pointsWE:
    value = DEM.dataProvider().sample(pt, 1)
    if value[1] == True:
        valueWE.append(value[0])
    else:
        valueWE.append(0)

# odległości między punktami
distancesNS = [i * interval for i in range(len(pointsNS))]
distancesWE = [i * interval for i in range(len(pointsWE))]

# profile terenu
plt.figure(figsize=(12, 5))
plt.plot(distancesNS, valueNS)
plt.title('Profil terenu - transekt północ-południe')
plt.ylabel("Wysokość terenu [m n.p.m]")
plt.xlabel("[m]")
plt.grid()
plt.show()

plt.figure(figsize=(12, 5))
plt.plot(distancesWE, valueWE)
plt.title('Profil terenu - transekt wschód-zachód')
plt.ylabel("Wysokość terenu [m n.p.m]")
plt.xlabel("[m]")
plt.grid()
plt.show()

    
    
    
    
    
    
    
