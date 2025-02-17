#Dokonaj analizy ukształtowania terenu (plik DEM.tif)
#używając dwóch transektów północ-południe oraz wschód-zachód. 
#Wynik zaprezentuj na rycinie (na osi X powinna znajdować się odległość wyrażona w metrach).
#Zastanów się również, co zrobić w przypadku, gdy komórki nie posiadają wartości (nan).

import os
import numpy as np
import matplotlib.pyplot as plt
from osgeo import gdal

path = os.path.join(os.path.expanduser("~"), "Documents", "adp", "dane8")
raster_path = os.path.join(path, "DEM.tif")

raster_layer = QgsRasterLayer(raster_path, "DEM")

provider = raster_layer.dataProvider()
bbox = provider.extent()
x_min = bbox.xMinimum()
x_max = bbox.xMaximum()
y_min = bbox.yMinimum()
y_max = bbox.yMaximum()
x_cent = (x_min + x_max) / 2
y_cent = (y_min + y_max) / 2
x_roz = provider.xSize()
y_roz = provider.ySize()

n_s = [(x_cent, y) for y in np.linspace(y_min, y_max, y_roz)]
e_w = [(x, y_cent) for x in np.linspace(x_min, x_max, x_roz)]

raster = gdal.Open(raster_path)
band = raster.GetRasterBand(1)
transform = raster.GetGeoTransform()

wys_ns = []
odl_ns = []
x_ostatni = None
y_ostatni = None
odl_ns_cala = 0

for x, y in n_s:
    px = int((x - transform[0]) / transform[1])
    py = int((y - transform[3]) / transform[5])

    try:
        elevation = band.ReadAsArray(px, py, 1, 1)[0][0]
        if np.isnan(elevation) or elevation == 9999:
            continue
        wys_ns.append(elevation)
    except:
        continue

    if x_ostatni is not None and y_ostatni is not None:
        dx = x - x_ostatni
        dy = y - y_ostatni
        odl_ns_cala += np.sqrt(dx**2 + dy**2)
    odl_ns.append(odl_ns_cala)

    x_ostatni, y_ostatni = x, y

wys_ew = []
odl_ew = []
x_ostatni = None
y_ostatni = None
odl_ew_cala = 0

for x, y in e_w:
    px = int((x - transform[0]) / transform[1])
    py = int((y - transform[3]) / transform[5])

    try:
        elevation = band.ReadAsArray(px, py, 1, 1)[0][0]
        if np.isnan(elevation) or elevation == 9999:
            continue
        wys_ew.append(elevation)
    except:
        continue

    if x_ostatni is not None and y_ostatni is not None:
        dx = x - x_ostatni
        dy = y - y_ostatni
        odl_ew_cala += np.sqrt(dx**2 + dy**2)
    odl_ew.append(odl_ew_cala)

    x_ostatni, y_ostatni = x, y

plt.figure(figsize=(12, 6))
plt.plot(odl_ns, wys_ns, label="Północ-południe", color="blue")
plt.plot(odl_ew, wys_ew, label="Wschód-zachód", color="red")
plt.title("Ukształtowanie terenu")
plt.xlabel("Wysokość")
plt.ylabel("Odległość")
plt.legend()
plt.grid(True)

output_plot_path = os.path.join(path, "profil.png")
plt.savefig(output_plot_path)
plt.show()

print(f"Śceiżka zapisu {output_plot_path}")
