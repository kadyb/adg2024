import matplotlib.pyplot as plt
from shapely.geometry import Polygon
import numpy as np

def scale_polygon(polygon, px, py, scale_x, scale_y):
    scaled_coords = []
    for x, y in polygon.exterior.coords:
        new_x = scale_x * (x - px) + px
        new_y = scale_y * (y - py) + py
        scaled_coords.append((new_x, new_y))
    return Polygon(scaled_coords)

def reflect_polygon(polygon, axis, value):
    reflected_coords = []
    for x, y in polygon.exterior.coords:
        if axis == 'vertical':
            new_x = 2 * value - x
            new_y = y
        elif axis == 'horizontal':
            new_x = x
            new_y = 2 * value - y
        reflected_coords.append((new_x, new_y))
    return Polygon(reflected_coords)

# Przykładowe dane
poly_wkt = "POLYGON ((40 30, 60 30, 50 40, 40 30))"
poly = Polygon([(40, 30), (60, 30), (50, 40), (40, 30)])

# Skalowanie
poly_scaled = scale_polygon(poly, px=50, py=35, scale_x=1.5, scale_y=0.5)

# Odbicie
poly_reflected = reflect_polygon(poly, axis='vertical', value=50)

# Rysowanie za pomocą matplotlib
fig, ax = plt.subplots()
x, y = poly.exterior.xy
ax.plot(x, y, label='Original', color='blue')
x, y = poly_scaled.exterior.xy
ax.plot(x, y, label='Scaled', color='green')
x, y = poly_reflected.exterior.xy
ax.plot(x, y, label='Reflected', color='red')
ax.legend()
plt.show()
