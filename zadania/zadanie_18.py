import qgis.core as qg
import matplotlib.pyplot as plt
from math import *

# zad 18 Zaimplementuj dwie wybrane operacje transformacji geometrii, a następnie wyświetl ich wyniki. Jako przykładowe dane wykorzystaj poligon "POLYGON ((40 30, 60 30, 50 40, 40 30))".

poligon = "POLYGON ((40 30, 60 30, 50 40, 40 30))"

# obrócenie
def obrot(poligon, kat):
    kat_obrot = radians(kat)
    geometry = QgsGeometry.fromWkt(poligon)
    vertices = list(geometry.vertices())
    centroid = geometry.centroid().asPoint()
    px,py = centroid.x(), centroid.y()
    
    obrot = []
    for vertex in vertices:
        x, y = vertex.x(), vertex.y()
        new_x = (x - px) * cos(kat_obrot) - (y - py) * sin(kat_obrot) + px
        new_y = (x - px) * sin(kat_obrot) + (y - py) * cos(kat_obrot) + py
        obrot.append(QgsPointXY(new_x, new_y))
    new_geom = QgsGeometry.fromPolygonXY([obrot])
    return new_geom

obrocony_poligon = obrot(poligon, 45)

# odbicie
def odbicie(poligon , linia_wertykalna):
    geometry = QgsGeometry.fromWkt(poligon)
    vertices = list(geometry.vertices())
    
    odbicie = []
    for vertex in vertices:
        new_x = 2 * linia_wertykalna - vertex.x()
        new_y = vertex.y()
        odbicie.append(QgsPointXY(new_x, new_y))
    new_geom = QgsGeometry.fromPolygonXY([odbicie])
    return new_geom

odbity_poligon = odbicie(poligon, 5)

# wizualizacja
def geometry_to_coords(geometry):
    if isinstance(geometry, str):
        geometry = QgsGeometry.fromWkt(geometry)
    
    geom_type = geometry.type().name
    
    points = geometry.asPolygon()
    for p in points:
        x, y = zip(*p)
    return x, y

x1 = geometry_to_coords(poligon)[0]
y1 = geometry_to_coords(poligon)[1]
x2 = geometry_to_coords(obrocony_poligon)[0]
y2 = geometry_to_coords(obrocony_poligon)[1]

plt.figure(figsize = (4, 3))
plt.plot(x1, y1, color = "grey", linestyle = "dashed", zorder = 1)
plt.fill(x2, y2, color = "blue", zorder = 2)
plt.show()

x2 = geometry_to_coords(odbity_poligon)[0]
y2 = geometry_to_coords(odbity_poligon)[1]

plt.figure(figsize = (4, 3))
plt.plot(x1, y1, color = "grey", linestyle = "dashed", zorder = 1)
plt.fill(x2, y2, color = "blue", zorder = 2)
plt.show()
