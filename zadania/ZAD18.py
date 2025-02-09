import math
import matplotlib.pyplot as plt
from qgis.core import QgsGeometry, QgsPointXY

def shift(geometry, dx, dy):
    vertices = geometry.vertices()
    shifted = [QgsPointXY(vertex.x() + dx, vertex.y() + dy) for vertex in vertices]
    return QgsGeometry.fromPolygonXY([shifted])


def rotate(geometry, angle, pivot_x, pivot_y):
    angle_rad = -math.radians(angle) 
    vertices = geometry.vertices()
    rotated = []
    for vertex in vertices:
        x, y = vertex.x(), vertex.y()
        x_shifted, y_shifted = x - pivot_x, y - pivot_y
        x_new = x_shifted * math.cos(angle_rad) - y_shifted * math.sin(angle_rad)
        y_new = x_shifted * math.sin(angle_rad) + y_shifted * math.cos(angle_rad)
        x_final, y_final = x_new + pivot_x, y_new + pivot_y
        rotated.append(QgsPointXY(x_final, y_final))
    return QgsGeometry.fromPolygonXY([rotated])

def geometry_to_coords(geometry):
    vertices = geometry.vertices()
    x, y = [], []
    for vertex in vertices:
        x.append(vertex.x())
        y.append(vertex.y())
    x.append(x[0])
    y.append(y[0])
    return x, y


poly_wkt = "POLYGON ((40 30, 60 30, 50 40, 40 30))"
poly = QgsGeometry.fromWkt(poly_wkt)
poly_shifted = shift(poly, dx=10, dy=5)
poly_rotated = rotate(poly, angle=30, pivot_x=50, pivot_y=35)

x_original, y_original = geometry_to_coords(poly)
x_shifted, y_shifted = geometry_to_coords(poly_shifted)
x_rotated, y_rotated = geometry_to_coords(poly_rotated)

plt.figure(figsize=(5, 5))

plt.plot(x_original, y_original, color="black", linestyle="dashed", label="Oryginalny", linewidth=1.5)
plt.plot(x_shifted, y_shifted, color="blue", label="Przesunięcie (dx=10, dy=5)", linewidth=1.5)
plt.plot(x_rotated, y_rotated, color="red", label="Obrót (30° wokół (50,35))", linewidth=1.5)

plt.legend()
plt.grid(True)
plt.title("Transformacje geometrii")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()