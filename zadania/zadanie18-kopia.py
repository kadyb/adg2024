'''
Zaimplementuj dwie wybrane operacje transformacji geometrii, a następnie
wyświetl ich wyniki. Jako przykładowe dane wykorzystaj poligon "POLYGON 
((40 30, 60 30, 50 40, 40 30))".
'''

import os
import qgis.core as qg
import matplotlib.pyplot as plt
import math

poligon = "POLYGON ((40 30, 60 30, 50 40, 40 30))"
geometry = qg.QgsGeometry.fromWkt(poligon)

def scale_geometry(geometry, factor_x, factor_y):
    centroid = geometry.centroid()
    center_x = centroid.asPoint().x()
    center_y = centroid.asPoint().y()

    scaled_vertices = []
    for vertex in geometry.vertices():
        x = vertex.x() - center_x
        y = vertex.y() - center_y
        new_x = center_x + x * factor_x
        new_y = center_y + y * factor_y
        scaled_vertices.append(qg.QgsPointXY(new_x, new_y))
    return qg.QgsGeometry.fromPolygonXY([scaled_vertices])

def rotate_geometry(geometry, angle_degrees, center_x, center_y):
    angle_radians = math.radians(angle_degrees)
    rotated_vertices = []
    for vertex in geometry.vertices():
        x = vertex.x() - center_x
        y = vertex.y() - center_y

        new_x = center_x + x * math.cos(angle_radians) - y * math.sin(angle_radians)
        new_y = center_y + x * math.sin(angle_radians) + y * math.cos(angle_radians)
        rotated_vertices.append(qg.QgsPointXY(new_x, new_y))
    return qg.QgsGeometry.fromPolygonXY([rotated_vertices])

def translate_geometry(geometry, offset_x, offset_y):
    translated_vertices = []
    for vertex in geometry.vertices():
        new_x = vertex.x() + offset_x
        new_y = vertex.y() + offset_y
        translated_vertices.append(qg.QgsPointXY(new_x, new_y))
    return qg.QgsGeometry.fromPolygonXY([translated_vertices])

def geometry_to_coords(geometry):
    if isinstance(geometry, str):
        geometry = qg.QgsGeometry.fromWkt(geometry)

    points = geometry.asPolygon()
    if points:
        for p in points:
            x, y = zip(*p)
        return x, y
    else:
        return [], []
        
shifted_geometry = translate_geometry(geometry, 10, 5)
rotated_geometry = rotate_geometry(geometry, 45, 50, 30)
scaled_geometry = scale_geometry(geometry, 1.5, 1.5)

plt.figure(figsize=(10, 6))

def plot_polygon(geometry, title, color):
    x, y = geometry_to_coords(geometry)
    plt.plot(x, y, label=title, color=color)
    plt.fill(x, y, color=color, alpha=0.3)

plot_polygon(geometry, 'Oryginalny', 'blue')
plot_polygon(shifted_geometry, 'Przesunięty', 'orange')
plot_polygon(rotated_geometry, 'Obrót (45°)', 'green')
plot_polygon(scaled_geometry, 'Skalowany', 'purple')

plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Transformacje Geometrii Poligonu')
plt.grid(True)
plt.show()