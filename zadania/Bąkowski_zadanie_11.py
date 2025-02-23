# Zadanie 1: Analiza geomorfometryczna
import rasterio 
import numpy as np
import matplotlib.pyplot as plt

dem_path = "C:/Users/user/Documents/dem.tif"
with rasterio.open(dem_path) as src:
    dem_data = src.read(1)
    transform = src.transform

def transect_line(dem, direction, transform):
    if direction == "NS":  # North-South
        transect = dem[:, dem.shape[1] // 2]
        distance = np.arange(0, transect.size) * transform[0]
    elif direction == "EW":  # East-West
        transect = dem[dem.shape[0] // 2, :]
        distance = np.arange(0, transect.size) * transform[4]
    return distance, transect

ns_distance, ns_transect = transect_line(dem_data, "NS", transform)
ew_distance, ew_transect = transect_line(dem_data, "EW", transform)

ns_transect = np.nan_to_num(ns_transect)
ew_transect = np.nan_to_num(ew_transect)

plt.figure(figsize=(10, 5))
plt.plot(ns_distance, ns_transect, label="Północ-Południe")
plt.plot(ew_distance, ew_transect, label="Wschód-Zachód")
plt.xlabel("Odległość (m)")
plt.ylabel("Wysokość (m)")
plt.legend()
plt.title("Transekty wysokościowe")
plt.grid()
plt.show()
