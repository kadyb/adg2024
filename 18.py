from shapely.geometry import Polygon
from shapely import wkt
import math as m
import matplotlib.pyplot as plt

def rotacja(wkt_str, k):
    k = -(k * m.pi) / 180  
    geometry = wkt.loads(wkt_str)
    centroid = geometry.centroid
    px, py = centroid.x, centroid.y

    rotated_coords = []
    for x, y in geometry.exterior.coords:
        x_2 = (x - px) * m.cos(k) - (y - py) * m.sin(k) + px
        y_2 = (x - px) * m.sin(k) + (y - py) * m.cos(k) + py
        rotated_coords.append((x_2, y_2))

    rotated_polygon = Polygon(rotated_coords)

    x1, y1 = geometry.exterior.xy
    x2, y2 = rotated_polygon.exterior.xy

    plt.figure(figsize=(6, 6))
    plt.plot(x1, y1, color="grey", linestyle="dashed", zorder=1)  
    plt.fill(x2, y2, color="blue", alpha=0.5, zorder=2) 
    plt.scatter(px, py, color="red", zorder=3, label="Centroid")
    plt.title(f"Rotacja o {k * 180 / m.pi}°")
    plt.grid(True)
    plt.show()

def przeskala(wkt_input, scale_x, scale_y):
    poly = wkt.loads(wkt_input)
    
    center = poly.centroid
    cx, cy = center.x, center.y
    
    new_coords = []
    for coord in poly.exterior.coords:
        scaled_x = scale_x * (coord[0] - cx) + cx
        scaled_y = scale_y * (coord[1] - cy) + cy
        new_coords.append((scaled_x, scaled_y))
    
    scaled_poly = Polygon(new_coords)
    
    orig_x, orig_y = poly.exterior.xy
    scaled_x, scaled_y = scaled_poly.exterior.xy
    
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.plot(orig_x, orig_y, color="gray", linestyle="--", label="Oryginał", zorder=1)
    ax.fill(scaled_x, scaled_y, color="lightblue", alpha=0.6, label="Przeskalowany", zorder=2)
    ax.scatter(cx, cy, color="darkred", label="Centroid", zorder=3)
    ax.set_title(f"Przeskalowanie: Δx={scale_x}, Δy={scale_y}")
    ax.grid(True)
    ax.legend()
    plt.show()


polygon = "POLYGON ((40 30, 60 30, 50 40, 40 30))"
rotacja(polygon, 50)  
przeskala(polygon, 0.5, 0.5)
