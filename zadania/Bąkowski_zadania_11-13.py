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

# Zadanie 2: Analiza teledetekcyjna
import random
from qgis.core import QgsPointXY

random.seed(999)  # Dla powtarzalności
x_coords = random.choices(range(0, 1000, 10), k=100)
y_coords = random.choices(range(0, 1000, 10), k=100)
points = [QgsPointXY(x, y) for x, y in zip(x_coords, y_coords)]

channel1_path = "C:/Users/user/Documents/Landsat_B1.tif"
channel2_path = "C:/Users/user/Documents/Landsat_B2.tif"

with rasterio.open(channel1_path) as src1, rasterio.open(channel2_path) as src2:
    ch1_data = src1.read(1)
    ch2_data = src2.read(1)

differences = ch1_data - ch2_data
correlation = np.corrcoef(ch1_data.flatten(), ch2_data.flatten())[0, 1]

plt.figure(figsize=(8, 6))
plt.scatter(ch1_data.flatten(), ch2_data.flatten(), alpha=0.5, label="Punkty")
plt.plot([0, max(ch1_data.max(), ch2_data.max())],
         [0, max(ch1_data.max(), ch2_data.max())],
         color='red', label='x = y')
plt.xlabel("Kanał 1")
plt.ylabel("Kanał 2")
plt.legend()
plt.title(f"Współczynnik korelacji: {correlation:.2f}")
plt.grid()
plt.show()

print("Średnia różnic:", np.nanmean(differences))
print("Odchylenie standardowe różnic:", np.nanstd(differences))

# Zadanie 3: Funkcja losowania stratyfikowanego
import geopandas as gpd
from shapely.geometry import Point

def sample_strata(vector_path, n):
    gdf = gpd.read_file(vector_path)
    sampled_points = []

    for _, row in gdf.iterrows():
        polygon = row.geometry
        bbox = polygon.bounds

        for _ in range(n):
            while True:
                x = random.uniform(bbox[0], bbox[2])
                y = random.uniform(bbox[1], bbox[3])
                point = Point(x, y)
                if polygon.contains(point):
                    sampled_points.append(point)
                    break

    sampled_gdf = gpd.GeoDataFrame(geometry=sampled_points, crs=gdf.crs)
    return sampled_gdf

result = sample_strata("C:/Users/user/Documents/powiaty.gpkg", 5)
result.to_file("C:/Users/user/Documents/wynik_stratyfikowane.gpkg", driver="GPKG")
